from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from models.models import DBSession

from apps.blog import application_routes

import apps.blog

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    
    #application routes integration
    config.include(application_routes, route_prefix='/blog')
    config.scan()
    return config.make_wsgi_app()

