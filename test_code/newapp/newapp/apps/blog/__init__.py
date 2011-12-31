from apps import PROJECT_NAME, project_package


APP_NAME = 'blog'
APP_BASE = '%s.apps.%s' % (PROJECT_NAME, APP_NAME)

def application_routes(config):
    config.add_route(APP_NAME + '.home', '/')
    config.add_route(APP_NAME + '.about', '/about')
    
    config.add_static_view('static', 'static', cache_max_age=3600)
