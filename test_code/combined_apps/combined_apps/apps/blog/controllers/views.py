from pyramid.view import view_config

from ..models.models import (
    DBSession,
    #MyModel,
    )

from .. import APP, PROJECT, APP_BASE

#@view_config(route_name='blog.home', renderer='combined_apps:apps/blog/templates/mytemplate.mako')
@view_config(route_name='blog.home', renderer='%s:templates/mytemplate.mako' % APP_BASE)
def my_view(request):
    #one = DBSession.query(MyModel).filter(MyModel.name=='one').first()
    one=None
    
    return {'one':one, 'project':'combined_apps'}
