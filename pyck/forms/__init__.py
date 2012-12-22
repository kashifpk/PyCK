"""
.. module:: pyck.forms
    :synopsis: Wrapper on top of WTForms to further ease up forms usage

.. moduleauthor:: Kashif Iftikhar [kashif@compulife.com.pk]

The PyCK Forms Package

"""

from form import Form
from wtdojo import fields as f
from wtdojo import widgets as dw
from wtforms import validators
from wtforms.ext.sqlalchemy.orm import model_form as wtforms_model_form
from wtforms.ext.sqlalchemy.orm import model_fields
from wtforms.ext.sqlalchemy.orm import converts, ModelConverter, ModelConverterBase

from pyck.forms import Form


class DojoModelConverter(ModelConverter):
    def __init__(self, extra_converters=None):
        super(DojoModelConverter, self).__init__(extra_converters)

    @classmethod
    def _string_common(cls, column, field_args, **extra):
        if column.type.length:
            field_args['validators'].append(validators.Length(max=column.type.length))

    @converts('String', 'Unicode')
    def conv_String(self, field_args, **extra):
        self._string_common(field_args=field_args, **extra)
        return f.DojoStringField(**field_args)

    @converts('Text', 'UnicodeText', 'types.LargeBinary', 'types.Binary')
    def conv_Text(self, field_args, **extra):
        self._string_common(field_args=field_args, **extra)
        field_args.setdefault('widget', dw.DojoTextArea())
        return f.DojoStringField(**field_args)

    @converts('Boolean')
    def conv_Boolean(self, field_args, **extra):
        return f.DojoBooleanField(**field_args)

    @converts('Date')
    def conv_Date(self, field_args, **extra):
        return f.DojoDateField(**field_args)

    #@converts('DateTime')
    #def conv_DateTime(self, field_args, **extra):
    #    return f.DateTimeField(**field_args)

    #@converts('Enum')
    #def conv_Enum(self, column, field_args, **extra):
    #    field_args['choices'] = [(e, e) for e in column.type.enums]
    #    return f.SelectField(**field_args)

    @converts('Integer', 'SmallInteger')
    def handle_integer_types(self, column, field_args, **extra):
        unsigned = getattr(column.type, 'unsigned', False)
        if unsigned:
            field_args['validators'].append(validators.NumberRange(min=0))
        return f.DojoIntegerField(**field_args)

    #@converts('Numeric', 'Float')
    #def handle_decimal_types(self, column, field_args, **extra):
    #    places = getattr(column.type, 'scale', 2)
    #    if places is not None:
    #        field_args['places'] = places
    #    return f.DecimalField(**field_args)
    #
    #@converts('databases.mysql.MSYear')
    #def conv_MSYear(self, field_args, **extra):
    #    field_args['validators'].append(validators.NumberRange(min=1901, max=2155))
    #    return f.TextField(**field_args)
    #
    #@converts('databases.postgres.PGInet', 'dialects.postgresql.base.INET')
    #def conv_PGInet(self, field_args, **extra):
    #    field_args.setdefault('label', 'IP Address')
    #    field_args['validators'].append(validators.IPAddress())
    #    return f.TextField(**field_args)
    #
    #@converts('dialects.postgresql.base.MACADDR')
    #def conv_PGMacaddr(self, field_args, **extra):
    #    field_args.setdefault('label', 'MAC Address')
    #    field_args['validators'].append(validators.MacAddress())
    #    return f.TextField(**field_args)
    #
    #@converts('dialects.postgresql.base.UUID')
    #def conv_PGUuid(self, field_args, **extra):
    #    field_args.setdefault('label', 'UUID')
    #    field_args['validators'].append(validators.UUID())
    #    return f.TextField(**field_args)
    #
    #@converts('MANYTOONE')
    #def conv_ManyToOne(self, field_args, **extra):
    #    return QuerySelectField(**field_args)
    #
    #@converts('MANYTOMANY', 'ONETOMANY')
    #def conv_ManyToMany(self, field_args, **extra):
    #    return QuerySelectMultipleField(**field_args)


def model_form(model, db_session=None, base_class=Form, only=None,
    exclude=None, field_args=None, converter=None, exclude_pk=True,
    exclude_fk=True, type_name=None):
    #def model_form(model, base_class=Form, only=None, exclude=None, field_args=None, converter=None):
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
    field_dict = model_fields(model, db_session, only, exclude, field_args, converter)
    return type(model.__name__ + 'Form', (base_class, ), field_dict)

#
#def dojo_model_fields(model, db_session=None, only=None, exclude=None,
#                      field_args=None, converter=None):
#    """
#    Generate a dictionary of fields for a given SQLAlchemy model.
#
#    See `model_form` docstring for description of parameters.
#    """
#    if not hasattr(model, '_sa_class_manager'):
#        raise TypeError('model must be a sqlalchemy mapped model')
#
#    mapper = model._sa_class_manager.mapper
#    converter = converter or DojoModelConverter()
#    field_args = field_args or {}
#
#    properties = ((p.key, p) for p in mapper.iterate_properties)
#    if only:
#        properties = (x for x in properties if x[0] in only)
#    elif exclude:
#        properties = (x for x in properties if x[0] not in exclude)
#
#    field_dict = {}
#    for name, prop in properties:
#        field = converter.convert(model, mapper, prop,
#            field_args.get(name), db_session)
#        if field is not None:
#            field_dict[name] = field
#
#    return field_dict


def dojo_model_form(model, db_session=None, base_class=Form, only=None,
    exclude=None, field_args=None, converter=None, exclude_pk=True,
    exclude_fk=True, type_name=None):
    """
    A Wrapper around :func:`wtforms.ext.sqlalchemy.orm.model_form` function to facilitate creating model
    forms using a wtforms compatible model_form call but using :class:`pyck.forms.Form` and :module:`WTDojo`
    form components

    Create a wtforms Form for a given SQLAlchemy model class::

        from pyck.forms import dojo_model_form
        from myapp.models import User
        UserForm = dojo_model_form(User)

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
    converter = converter or DojoModelConverter()
    field_dict = model_fields(model, db_session, only, exclude, field_args, converter)
    return type(model.__name__ + 'Form', (base_class, ), field_dict)


__all__ = ['Form', 'model_form', 'dojo_model_form']