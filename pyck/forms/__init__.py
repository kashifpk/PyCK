"""
.. module:: pyck.forms
    :synopsis: Wrapper on top of WTForms to further ease up forms usage

.. moduleauthor:: Kashif Iftikhar [kashif@compulife.com.pk]

The PyCK Forms Package

"""

from .form import Form
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
        if hasattr(column.type, 'length') and column.type.length:
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

    @converts('dialects.postgresql.json.JSONB', 'dialects.postgresql.json.JSON')
    def conv_JSON(self, field_args, **extra):
        self._string_common(field_args=field_args, **extra)
        field_args.setdefault('widget', dw.DojoTextArea())
        return f.DojoJSONField(**field_args)

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

    @converts('Numeric', 'Float', 'Decimal')
    def handle_decimal_types(self, column, field_args, **extra):
        places = getattr(column.type, 'scale', 2)
        if places is not None:
            field_args['places'] = places
        return f.DojoDecimalField(**field_args)

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


def dojo_model_form(model, db_session=None, base_class=Form, only=None,
                    exclude=None, field_args=None, converter=None, exclude_pk=False,
                    exclude_fk=False, type_name=None):
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
    :param exclude_pk:
        An optional boolean to force primary key exclusion.
    :param exclude_fk:
        An optional boolean to force foreign keys exclusion.
    :param type_name:
        An optional string to set returned type name.

    """

    class DojoModelForm(base_class):
        """Sets object as form attribute."""
        def __init__(self, *args, **kwargs):
            if 'obj' in kwargs:
                self._obj = kwargs['obj']
            super(DojoModelForm, self).__init__(*args, **kwargs)

    if not exclude:
        exclude = []
    model_mapper = model.__mapper__

    for prop in model_mapper.iterate_properties:
        if not hasattr(prop, 'columns'):  # ignore relationships and other non-field columns
            continue

        # if it's primary key and is not foreign key
        if 0 == len(prop.columns[0].foreign_keys) and prop.columns[0].primary_key:
            if exclude_pk:
                exclude.append(prop.key)

        # if it's foreign key but not many to many
        if len(prop.columns[0].foreign_keys) > 0 and exclude_fk:
            if not prop.is_primary():
                exclude.append(prop.key)

    type_name = type_name or str(model.__name__ + 'Form')
    converter = converter or DojoModelConverter()
    
    field_dict = model_fields(model, db_session, only, exclude, field_args, converter, exclude_pk=exclude_pk, exclude_fk=exclude_fk)
    return type(type_name, (base_class, ), field_dict)


__all__ = ['Form', 'model_form', 'dojo_model_form']
