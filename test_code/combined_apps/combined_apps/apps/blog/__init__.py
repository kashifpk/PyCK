#from pyramid.config import Configurator
#from sqlalchemy import engine_from_config
#
#from .models import DBSession

#def main(global_config, **settings):
#    """ This function returns a Pyramid WSGI application.
#    """
#    #engine = engine_from_config(settings, 'sqlalchemy.')
#    #DBSession.configure(bind=engine)
#    config = Configurator(settings=settings)
#    config.add_static_view('static', 'static', cache_max_age=3600)
#    config.add_route('home', '/')
#    config.scan()
#    return config.make_wsgi_app()

PROJECT = 'combined_apps'
APP = 'blog'

APP_BASE = '%s.apps.%s' % (PROJECT, APP)

def application_routes(config):
    config.add_route('blog.home', '/')
    config.add_route('blog.about', '/about')
    
    config.add_static_view('static', 'static', cache_max_age=3600)
