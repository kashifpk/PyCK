import hashlib
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from pyck.lib import get_routes

from ..models import db, Permission, User, UserPermission, RoutePermission

from ..forms import LoginForm, UserForm, PermissionForm, RoutePermissionForm
from sqlalchemy import func

import logging
log = logging.getLogger(__name__)

@view_config(route_name='pyckauth_manager', renderer='pyckauth_manager.mako')
def auth_manager(request):
    user_count = db.query(func.count(User.user_id)).scalar()
    permission_count = db.query(func.count(Permission.permission)).scalar()
    route_count = len(request.registry.introspector.get_category('routes'))

    return dict(user_count=user_count, permission_count=permission_count, route_count=route_count)


@view_config(route_name='pyckauth_users', renderer='pyckauth_users.mako')
def auth_users(request):

    action = request.GET.get('action', 'add')

    U = None
    if 'delete' == action:
        db.query(UserPermission).filter_by(user_id=request.GET['id']).delete()
        db.query(User).filter_by(user_id=request.GET['id']).delete()

        request.session.flash("User deleted!")
        return HTTPFound(location=request.route_url('pyckauth_users'))

    if 'edit' == action:
        U = db.query(User).filter_by(user_id=request.GET['id']).first()

    f = UserForm(request.POST, U)

    if 'POST' == request.method:
        if f.validate():
            if 'add' == action:
                U = User()
                f.populate_obj(U)
                U.password = hashlib.sha1(f.password.data).hexdigest()
                db.add(U)

                # Add user permissions here.
                for key in list(request.POST.keys()):
                    if key.startswith('chk_perm_'):
                        permission = request.POST[key]
                        UP = UserPermission(user_id=f.user_id.data,
                                            permission=permission)
                        db.add(UP)

                request.session.flash("User created!")
                return HTTPFound(location=request.route_url('pyckauth_users'))

            elif 'edit' == action:
                db.query(UserPermission).filter_by(user_id=request.GET['id']).delete()
                for key in list(request.POST.keys()):
                    if key.startswith('chk_perm_'):
                        permission = request.POST[key]
                        UP = UserPermission(user_id=f.user_id.data,
                                            permission=permission)
                        db.add(UP)

                f.populate_obj(U)
                U.password = hashlib.sha1(f.password.data).hexdigest()
                request.session.flash("User updated!")
                return HTTPFound(location=request.route_url('pyckauth_users'))

    permissions = db.query(Permission).order_by('permission')
    users = db.query(User).order_by('user_id')

    return dict(action=action, user_form=f, permissions=permissions, users=users, user=U)


@view_config(route_name='pyckauth_permissions', renderer='pyckauth_permissions.mako')
def auth_permissions(request):

    action = request.GET.get('action', 'add')

    P = None
    if 'delete' == action:
        db.query(UserPermission).filter_by(permission=request.GET['id']).delete()
        db.query(RoutePermission).filter_by(permission=request.GET['id']).delete()
        db.query(Permission).filter_by(permission=request.GET['id']).delete()

        request.session.flash("Permission deleted!")
        return HTTPFound(location=request.route_url('pyckauth_permissions'))

    if 'edit' == action:
        P = db.query(Permission).filter_by(permission=request.GET['id']).first()

    f = PermissionForm(request.POST, P)

    if 'POST' == request.method:
        if f.validate():
            if 'add' == action:
                P = Permission()
                f.populate_obj(P)
                db.add(P)

                request.session.flash("Permission created!")
                return HTTPFound(location=request.route_url('pyckauth_permissions'))

            elif 'edit' == action:
                if f.permission.data != P.permission:
                    # Need to update permission in UserPermission and RoutePermission records too
                    user_permissions = db.query(UserPermission).filter_by(permission=request.GET['id'])
                    for up in user_permissions:
                        up.permission = f.permission.data

                    route_permissions = db.query(RoutePermission).filter_by(permission=request.GET['id'])
                    for rp in route_permissions:
                        rp.permission = f.permission.data

                f.populate_obj(P)
                request.session.flash("Permission updated!")
                return HTTPFound(location=request.route_url('pyckauth_permissions'))

    permissions = db.query(Permission).order_by('permission')

    return dict(action=action, permission_form=f, permissions=permissions, permission=P)


@view_config(route_name='pyckauth_routes', renderer='pyckauth_routes.mako')
def auth_routes(request):
    action = request.GET.get('action', 'add')

    if 'delete' == action:
        db.query(RoutePermission).filter_by(
                route_name=request.GET['r'], method=request.GET['m'],
                permission=request.GET['p']).delete()

        request.session.flash("Route permission deleted!")
        return HTTPFound(location=request.route_url('pyckauth_routes'))

    # **** Code for setting up route permission form
    f = RoutePermissionForm(request.POST)

    routes = get_routes(request)
    for k,v in routes.items():
        routes[k] = '{} ({})'.format(k,v)
    

    permissions = []
    Ps = db.query(Permission).order_by('permission')
    for P in Ps:
        permissions.append((P.permission, P.permission))

    f.permissions.choices = permissions
    # *************************************************

    if 'POST' == request.method:
        if f.validate():
            if 'add' == action:
                routenames = []
                
                for k,v in request.POST.items():
                    if 'routenames' == k:
                        routenames.append(v)
                
                for routename in routenames:
                    for P in f.permissions.data:
                        for M in f.request_methods.data:
                            RP = RoutePermission(route_name=routename, method=M, permission=P)
                            db.add(RP)

                request.session.flash("Route permissions created!")
                return HTTPFound(location=request.route_url('pyckauth_routes'))

    route_permissions = db.query(RoutePermission).order_by(
        RoutePermission.route_name,
        RoutePermission.permission,
        RoutePermission.method)

    return dict(action=action,
                route_permissions=route_permissions,
                routes=routes,
                route_permissions_form=f)


@view_config(route_name='pyckauth_login', renderer='pyckauth_login.mako')
def login(request):

    login_form = LoginForm(request.POST)

    if 'POST' == request.method and login_form.validate():
        status, user = User.login(
            username=login_form.user_id.data.encode('utf-8'),
            password=login_form.password.data.encode('utf-8'),
            request=request
            )
        
        if "NOT FOUND" == status:
            request.session.flash("Error: Authentication failed. User not found.")

        elif "AUTH FAILED" == status:
            request.session.flash("Error: Authentication failed. Incorrect password.")

        else:

            # redirect according to the permission the user has
            if 'came_from' in request.session:
                came_from = request.session['came_from']
                log.info("Came from: " + came_from)
                del request.session['came_from']
                return HTTPFound(location=request.route_url(came_from))

            return HTTPFound(location=request.route_url('home'))

    return dict(login_form=login_form)


@view_config(route_name='pyckauth_logout')
def logout(request):
    
    if 'logged_in_user' in request.session:
        User.logout(request=request)
    
    return HTTPFound(location=request.route_url('home'))
