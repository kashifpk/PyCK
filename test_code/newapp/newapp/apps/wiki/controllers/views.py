from pyramid.view import view_config

from ..models import (
    DBSession,
    Page
    )

from .. import APP_NAME, PROJECT_NAME, APP_BASE

@view_config(route_name=APP_NAME+'.home', renderer='%s:templates/list.mako' % APP_BASE)
def my_view(request):
    page = DBSession().query(Page).first()
    return {'page': page}
