from pyramid.httpexceptions import HTTPNotFound, HTTPForbidden
from models import DBSession, Permission, User, UserPermission, RoutePermission
from pyramid.urldispatch import _compile_route
from sqlalchemy import or_, func


def authenticator(handler, registry):

    def auth_request(request):

        response = None

        # ignore static routes for authentication
        if 'static' in request.path.split('/'):
            return handler(request)

        logged_in_user = request.session.get('logged_in_user', None)

        protected_routes = []
        routes = DBSession.query(RoutePermission.route_name).distinct().all()

        for R in routes:
            protected_routes.append(R[0])

        #print(protected_routes)
        matched_routename = None

        for r in request.registry.introspector.get_category('routes'):
            R = r['introspectable']

            matcher, generator = _compile_route(R['pattern'])

            if isinstance(matcher(request.path), dict):
                #print(R['name'] + ':' + R['pattern'])
                matched_routename = R['name']
                break

        # Check routes from protected routes here.
        if matched_routename and matched_routename in protected_routes:
            # first check if there is any static permission given and if yes then validate routes against that permission
            if not logged_in_user:
                return HTTPForbidden()

            if is_allowed(request, matched_routename, ['ALL', request.method]):
                return handler(request)
            else:
                return HTTPForbidden()

        else:
            return handler(request)

    return auth_request


def is_allowed(request, routename, method='ALL'):
    """
    Given a request_object, routename and method; returns True if current user has access to that route,
    otherwise returns False.
    """

    if not isinstance(method, list):
        method = [method, ]

    user_permissions = request.session.get('auth_user_permissions', [])
    if request.session.get('auth_static_permission', None):
        user_permissions.append(request.session.get('auth_static_permission', None))

    has_permission = DBSession.query(func.count(RoutePermission.permission)).filter(
                                            RoutePermission.route_name == routename).filter(
                                            RoutePermission.method.in_(method)).filter(
                                            RoutePermission.permission.in_(user_permissions)).scalar()

    if has_permission > 0:
        return True
    else:
        return False
