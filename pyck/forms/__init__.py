"""
.. module:: pyck.forms
    :synopsis: Wrapper on top of WTForms to further ease up forms usage
    
.. moduleauthor:: Kashif Iftikhar [kashif@compulife.com.pk]

The PyCK Forms Package

"""



from form import Form
from wtforms.ext.sqlalchemy.orm import model_form as wtforms_model_form
from wtforms.ext.sqlalchemy.orm import model_fields

from pyck.forms import Form

def model_form(model, base_class=Form, only=None, exclude=None, field_args=None, converter=None):
    """
    A Wrapper around :func:`wtforms.ext.sqlalchemy.orm.model_form` function to facilitate creating model
    forms using a wtforms compatible model_form call but using :class:`pyck.forms.Form`
    Create a wtforms Form for a given SQLAlchemy model class::

        from pyck.forms import model_form
        from myapp.models import User
        UserForm = model_form(User)

    :param model:
        A SQLAlchemy mapped model class.
    :param base_class:
        Base form class to extend from. Must be a ``wtforms.Form`` subclass.
    :param only:
        An optional iterable with the property names that should be included in
        the form. Only these properties will have fields.
    :param exclude:
        An optional iterable with the property names that should be excluded
        from the form. All other properties will have fields.
    :param field_args:
        An optional dictionary of field names mapping to keyword arguments used
        to construct each field object.
    :param converter:
        A converter to generate the fields based on the model properties. If
        not set, ``ModelConverter`` is used.
    
    """
    field_dict = model_fields(model, only, exclude, field_args, converter)
    return type(model.__name__ + 'Form', (base_class, ), field_dict)




__all__ = ['Form', 'model_form']