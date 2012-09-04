from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound

from pyck.forms import model_form
from wtforms.widgets.core import Select
from wtforms import SelectField, validators

from ..models import DBSession, Category, Product

from ..forms import ContactForm

from pyck.controllers import CRUDController


class ProductCRUDController(CRUDController):
    model = Product
    db_session = DBSession
    add_edit_field_args = {
         'category_id': {'label': 'Category', 'widget': Select(), 'coerce': int, 'choices_fields': [Category.id, Category.name]}
         #'category_id': {'widget': Select(), 'coerce': int, 'choices': [(1, 'ABC'), (2, 'DEF')]}
        }

    list_field_args = {
            'category_id': {'display_field': 'category.name'}
                }


@view_config(route_name='home', renderer='home.mako')
def my_view(request):
    #one = DBSession.query(Site).filter(Site.name=='one').first()
    one = None
    return {'one': one, 'project': 'newapp'}


@view_config(route_name='contact', renderer="contact.mako")
def contact_form(request):

    #empty form initializes if not a POST request
    f = ContactForm(request.POST, request_obj=request, use_csrf_protection=True)   

    if 'POST' == request.method and 'form.submitted' in request.params:
        if f.validate():
            #TODO: Do email sending here.

            request.session.flash("Your message has been sent!")
            return HTTPFound(location=request.route_url('home'))

        #print(repr(f.errors))

    return {'contact_form': f}
