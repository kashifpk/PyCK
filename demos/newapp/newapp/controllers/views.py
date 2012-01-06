from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from ..models import (
    DBSession,
    #Site,
    )

from ..forms import ContactForm

@view_config(route_name='home', renderer='home.mako')
def my_view(request):
    #one = DBSession.query(Site).filter(Site.name=='one').first()
    one=None
    return {'one':one, 'project':'newapp'}

@view_config(route_name='contact', renderer="contact.mako")
def contact_form(request):
    
    f = ContactForm(request.POST)   #empty form initializes if not a POST request
    
    token = request.session.get_csrf_token()
    
    
    if 'POST' == request.method and 'form.submitted' in request.params:
        if token != request.POST['csrf_token']:
            raise ValueError('CSRF token did not match')
        
        if f.validate():
            #TODO: Do email sending here.
            
            request.session.flash("Your message has been sent!")
            return HTTPFound(location=request.route_url('home'))
    
    return {'contact_form': f, 'csrf_token': token}