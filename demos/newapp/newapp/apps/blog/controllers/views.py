from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from ..models import (
    DBSession,
    Post,
    AddPostForm
    )

from .. import APP_NAME, PROJECT_NAME, APP_BASE

@view_config(route_name=APP_NAME+'.home', renderer='%s:templates/list.mako' % APP_BASE)
def my_view(request):
    posts = DBSession.query(Post).order_by(Post.id.desc()).all()
    
    return {'APP_BASE': APP_BASE, 'APP_NAME': APP_NAME, 'posts': posts}

@view_config(route_name=APP_NAME+'.add', renderer='%s:templates/add.mako' % APP_BASE)
def add_post(request):
    
    f = AddPostForm(request.POST, request_obj=request, use_csrf_protection=True)
    
    if 'POST' == request.method and 'form.submitted' in request.params:
        if f.validate():
            #TODO: Do email sending here.
            p = Post(f.title.data, f.content.data)
            DBSession.add(p)
            #DBSession.commit()
            request.session.flash("Your post has been added successfully!")
            return HTTPFound(location=request.route_url(APP_NAME + '.home'))
    
    
    
    return {'APP_BASE': APP_BASE, 'APP_NAME': APP_NAME, 'form': f}