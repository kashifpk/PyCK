from pyramid.view import view_config

from ..models.models import (
    DBSession,
    #MyModel,
    )

@view_config(route_name='home', renderer='mytemplate.mako')
def my_view(request):
    #one = DBSession.query(MyModel).filter(MyModel.name=='one').first()
    one=None
    return {'one':one, 'project':'combined_apps'}
