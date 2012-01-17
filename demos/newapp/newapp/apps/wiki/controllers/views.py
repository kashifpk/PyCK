from pyramid.view import view_config

from ..models import (
    DBSession,
    Page
    )

from pyck.controllers import CRUDController

from .. import APP_NAME, PROJECT_NAME, APP_BASE

@view_config(route_name=APP_NAME+'.home', renderer='%s:templates/list.mako' % APP_BASE)
def my_view(request):
    page = DBSession().query(Page).first()
    return {'APP_BASE': APP_BASE, 'page': page}

class WikiCRUDController(CRUDController):
    model = Page
    friendly_name = 'Wiki Page'
    db_session = DBSession()
    
    #list_only = ['title', 'content']
    list_exclude = ['id',]
    list_actions = [
                    {'link_text': 'Add {friendly_name}', 'link_url': 'add'},
                    {'link_text': 'CompuLife', 'link_url': 'http://www.compulife.com.pk'}
                   ]
    
