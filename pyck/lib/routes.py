"Routes related utility functions"

from collections import OrderedDict


def get_routes(request):
    """Returns OrderedDict of routes available for given request
    
    :param request: Request object (normally called from controller code)
    
    :returns: OrderedDict of routes with routename as key and route url as value
    """
    
    routes = {}
    sorted_routes = OrderedDict()
    
    for r in request.registry.introspector.get_category('routes'):
        route = r['introspectable']
        #print(R['name'] + ':' + R['pattern'])
        routes[route['name']] = route['pattern']

    for routename in sorted(routes.keys()):
        sorted_routes[routename] = routes[routename]
    
    return sorted_routes
