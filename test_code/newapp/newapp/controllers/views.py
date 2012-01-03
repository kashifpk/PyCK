from pyramid.view import view_config

from ..models import (
    DBSession,
    #Site,
    )

@view_config(route_name='home', renderer='home.mako')
def my_view(request):
    #one = DBSession.query(Site).filter(Site.name=='one').first()
    one=None
    return {'one':one, 'project':'newapp'}

@view_config(route_name='sample_page', renderer="sample.mako")
def sample_page(request):
    
    return {}