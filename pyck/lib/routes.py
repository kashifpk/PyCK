"Routes related utility functions"

from collections import OrderedDict


def get_routes(request):
    """Returns OrderedDict of routes available for given request
    
    :param request: Request object (normally called from controller code)
    
    :returns: OrderedDict of routes with routename as key and route url as value
    """
    
    routes = {}
    sorted_routes = OrderedDict()
    
    # For the time being we are assuming that main project's route names don't contain a dot
    # While sub app routes must contain a dot as the are normally prefixed with "appname."
    
    main_routenames = []
    app_routenames = []
    
    for r in request.registry.introspector.get_category('routes'):
        route = r['introspectable']
        #print(R['name'] + ':' + R['pattern'])
        routes[route['name']] = route['pattern']
        if '.' in route['name']:
            app_routenames.append(route['name'])
        else:
            main_routenames.append(route['name'])

    for routename in sorted(main_routenames) + sorted(app_routenames):
        sorted_routes[routename] = routes[routename]
    
    return sorted_routes
