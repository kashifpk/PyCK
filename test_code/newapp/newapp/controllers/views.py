from pyramid.view import view_config

from ..models.models import (
    DBSession,
    #Site,
    )

@view_config(route_name='home', renderer='mytemplate.mako')
def my_view(request):
    #one = DBSession.query(Site).filter(Site.name=='one').first()
    one=None
    return {'one':one, 'project':'newapp'}
