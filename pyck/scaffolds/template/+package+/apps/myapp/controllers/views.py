from pyramid.view import view_config

from ..models import (
    DBSession,
    Post,
    )

from .. import APP_NAME, PROJECT_NAME, APP_BASE

@view_config(route_name=APP_NAME+'.home', renderer='%s:templates/list.mako' % APP_BASE)
def my_view(request):
    first_post = DBSession.query(Post).filter(Post.title=='Test').first()
    
    return {'APP_BASE': APP_BASE, 'post': first_post}
