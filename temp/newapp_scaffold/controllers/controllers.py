from pyramid.view import view_config

from ..models import (
    db,
    #include your models here
    )

from .. import APP_NAME, PROJECT_NAME, APP_BASE


@view_config(route_name=APP_NAME+'.home', renderer='%s:templates/list.mako' % APP_BASE)
def app_home(request):
    return {'APP_BASE': APP_BASE}
