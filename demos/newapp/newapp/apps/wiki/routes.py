from controllers.views import WikiCRUDController
from pyck.controllers import add_crud_handler

from . import APP_NAME, PROJECT_NAME, APP_BASE

def application_routes(config):
    config.add_route(APP_NAME + '.home', '/')
    config.add_static_view('static', 'static', cache_max_age=3600)
    
    add_crud_handler(config, APP_NAME + '.', '/crud', WikiCRUDController)
    
    