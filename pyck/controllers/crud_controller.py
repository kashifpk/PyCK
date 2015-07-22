import os.path
from sqlalchemy import func, or_

# for CRUD search data type matching
from sqlalchemy import (
    BIGINT, BINARY, BLOB, BOOLEAN, BigInteger, Binary, Boolean, DATE, DATETIME,
    DECIMAL, Date, DateTime, FLOAT, Float, INT, INTEGER, Integer, Interval,
    LargeBinary, NUMERIC, Numeric, REAL, SMALLINT, SmallInteger, TIME,
    TIMESTAMP, Time, VARBINARY,
    
    VARCHAR, UnicodeText, Unicode, String, TEXT, Text, NCHAR, NVARCHAR, CHAR, CLOB
    )

from sqlalchemy.exc import IntegrityError

from pyramid.response import Response
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound, HTTPNotAcceptable

from wtforms.widgets.core import Select
from wtforms import SelectField
from wtdojo.fields.core import DojoSelectField
from wtforms import validators

from pyck.forms import model_form, dojo_model_form
from pyck.lib.pagination import get_pages
from pyck.lib.models import get_columns, get_model_record_counts, models_dict_to_list
from pyck.lib import dates_and_times

import logging

log = logging.getLogger(__name__)


def add_crud_handler(config, route_name_prefix='', url_pattern_prefix='', handler_class=None):
    """
    A utility function to quickly add all crud related routes and set them to the crud handler class with one function
    call, for example::

        from pyck.controllers import add_crud_handler
        from controllers.views import WikiCRUDController
        .
        .
        .
        add_crud_handler(config, APP_NAME + '.', '/crud', WikiCRUDController)

    :param config:
        The application config object
    :param route_name_prefix:
        Optional string prefix to add to all route names. Useful if you're adding multiple CRUD controllers and want to
        avoid route name conflicts.
    :param url_pattern_prefix:
        Optional string prefix to add to all crud related url patterns
    :param handler_class:
        The handler class that is used to handle CRUD requests. Must be sub-class of :class:`pyck.controllers.CRUDController`

    """

    config.add_route(route_name_prefix + 'CRUD_list', url_pattern_prefix + '/')
    config.add_view(handler_class, attr='list',
                    route_name=route_name_prefix + 'CRUD_list',
                    renderer='pyck:templates/crud/list.mako')

    config.add_route(route_name_prefix + 'CRUD_add', url_pattern_prefix + '/add')
    config.add_view(handler_class, attr='add',
                    route_name=route_name_prefix + 'CRUD_add',
                    renderer='pyck:templates/crud/add_or_edit.mako')

    config.add_route(route_name_prefix + 'CRUD_edit', url_pattern_prefix + '/edit/{PK}')
    config.add_view(handler_class, attr='edit',
                    route_name=route_name_prefix + 'CRUD_edit',
                    renderer='pyck:templates/crud/add_or_edit.mako')

    config.add_route(route_name_prefix + 'CRUD_details', url_pattern_prefix + '/details/{PK}')
    config.add_view(handler_class, attr='details',
                    route_name=route_name_prefix + 'CRUD_details',
                    renderer='pyck:templates/crud/details.mako')

    config.add_route(route_name_prefix + 'CRUD_delete', url_pattern_prefix + '/delete/{PK}')
    config.add_view(handler_class, attr='delete', route_name=route_name_prefix + 'CRUD_delete')


class CRUDController(object):
    """
    Enables automatic CRUD interface generation from database models. The :class:`pyck.controllers.CRUDController`
    allows you to quickly enable CRUD interface for any database model you like. To use CRUD controller at minimum
    these steps must be followed.

    1. Create a sub-class of the CRUDController and set model (for which you want to have CRUD) and database session::

        from pyck.controllers import CRUDController
        from myapp.models import MyModel, db

        class MyCRUDController(CRUDController):
            model = MyModel
            db_session = db

    2. In your application's routes settings, specify the url where the CRUD interface should be displayed. You can use
       the :func:`pyck.controllers.add_crud_handler` method for it. For example in your __init__.py (if you're enabling
       CRUD for a model without your main project) or in your routes.py (if you're enabling CRUD for a model within an
       app in your project) put code like::

        from pyck.controllers import add_crud_handler
        from controllers.views import WikiCRDUController

        # Place this with the config.add_route calls
        add_crud_handler(config, 'mymodel_crud', '/mymodel', WikiCRUDController)

    and that's all you need to do to get a fully operation CRUD interface. Take a look at the newapp sample app in demos
    for a working CRUD example in the Wiki app.

    **Configuration Options**

    These parameters are to be set as class properties in a sub-class of CRUDController

    :param model: (Required) The SQLAlchemy model class for which the CRUD interface is desired

    :param db_session: (Required) The SQLAlchemy database session that should be used for operations

    :param friendly_name: A human-friendly name of the model. If given this is used in the templates instead of the model name

    :param base_template: An alternate base template to use for the CRUD handler instead of the default base template of the application

    :param list_sort_by: Sorting spec for displaying records in records list page
    
    :param add_edit_exclude: A list of fields that should not be displayed in add or edit operations

    :param add_edit_field_args: A dictionary of field arguments with field name as key and args and key-value pairs dict.

    :param list_recs_per_page: Number of records to display in a listing page. Default 10.

    :param list_max_pages: Maximum number of pages to display in page links. Default 10.

    :param list_only: List of fields that are to be displayed on listing page, all other fields are ignored.

    :param list_exclude: List of fields to be exluded in listing page

    :param list_field_args:
        arguments providing extra directions/instructions for displaying/formatting list fields

    :param list_actions:
        list of actions that are to be displayed in listing page, example::

            list_actions = [
                    {'link_text': 'Add {friendly_name}', 'link_url': 'add', 'css_class': 'btn btn-primary'},
                   ]

    :param list_per_record_actions:
        list of actions that are to be displayed for each row. These can contain a special keyword PK for referring to
        the primary key value(s) for the current record. Example::

            list_per_record_actions = [
                    {'link_text': 'Details', 'link_url': 'details/{PK}'},
                    {'link_text': 'Edit', 'link_url': 'edit/{PK}'},
                    {'link_text': 'Delete', 'link_url': 'delete/{PK}'},
                   ]

    :param detail_actions:
        list of actions to be displayed on the details page, similar to **list_per_record_actions**. Example::

            detail_actions = [
                    {'link_text': 'Edit', 'link_url': '../edit/{PK}'},
                    {'link_text': 'Delete', 'link_url': '../delete/{PK}'},
                   ]

    :param template_extra_params: A dictionary containing any other parameters required to be passed to the CRUD templates

    **TODO**

    * More documentation of various options and methods
    * A CRUDController tutorial
    * Tests for the controller
    * Add support for composite primary keys
    * Once CRDUController is complete, may be put table display login in a ModelTable component??

    """

    model = None
    friendly_name = None
    db_session = None

    
    
    #Add and edit page settings
    add_edit_exclude = None

    add_edit_field_args = {}

    #Listing page sorting
    list_sort_by = None
    
    #Listing page related settings
    list_recs_per_page = 10
    list_max_pages = 10
    list_field_args = {}
    list_only = None
    list_exclude = None
    list_actions = [
                    {'link_text': 'Add {friendly_name}', 'link_url': 'add', 'css_class': 'btn btn-success'},
                   ]

    list_per_record_actions = [
                    {'link_text': 'Details', 'link_url': 'details/{PK}'},
                    {'link_text': 'Edit', 'link_url': 'edit/{PK}'},
                    {'link_text': 'Delete', 'link_url': 'delete/{PK}', 'css_class': 'text-danger'},
                   ]

    detail_actions = [
                    {'link_text': 'Edit', 'link_url': '../edit/{PK}'},
                    {'link_text': 'Delete', 'link_url': '../delete/{PK}', 'css_class': 'btn btn-danger'},
                   ]

    base_template = '/base.mako'

    template_extra_params = {}

    fetch_record_count = False

    def __init__(self, request):
        self.request = request

        if self.db_session is None:
            raise ValueError("Must provide a SQLAlchemy database session object as db_session")

        if self.friendly_name is None:
            self.friendly_name = self.model.__tablename__.replace("_", " ").title()

    def _get_rec_from_pk_val(self):

        pk_val = self.request.matchdict.get('PK')
        pk_name = ''
        R = None

        #check to see if we have multiple primary keys or single
        primary_key_columns = list(self.model.__table__.primary_key.columns.keys())
        if len(primary_key_columns) > 1:
            #composite key processing here
            pass
        else:
            pk_name = primary_key_columns[0]
            #R = self.db_session.query(self.model).filter("%s=%s" % (pk_name, pk_val)).one()
            R = self.db_session.query(self.model).filter('%s=:pk_val' % (pk_name)).params(pk_val=pk_val).one()

        return R

    def _get_modelform_field_args(self):
        """
        Returns only the fields that can be passed on to the ModelForm constructor.
        This involves removing the choices and choices_fields keys.
        """
        form_fields = {}
        exclude_keys = ['choices', 'choices_fields']

        for field_name, field_data in list(self.add_edit_field_args.items()):
            new_dict = {}
            for k, v in list(field_data.items()):
                if k not in exclude_keys:
                    new_dict[k] = v

            form_fields[field_name] = new_dict

        return form_fields

    def _get_exclude_list(self, action_type):
        if self.add_edit_exclude:
            return self.add_edit_exclude

        log.info('determining exclude list')
        # exclude any relationships
        exclude_list = list(self.model.__mapper__.relationships.keys())
        log.info(exclude_list)

        if 'add' == action_type:
            # get the columns and add any primary key columns to the
            # exlude list if their autoincrement is True
            cols = get_columns(self.model, 'primary_key')
            for c in cols:
                if int == c.property.columns[0].type.python_type and 0 == len(c.property.columns[0].foreign_keys):
                    exclude_list.append(c.key)

        return exclude_list

    def _models_rec_count_if_needed(self):
        if self.fetch_record_count and 'models' in self.template_extra_params:
            return get_model_record_counts(self.db_session, models_dict_to_list(self.template_extra_params['models']))
        else:
            return {}
    
    def _get_search_condition(self, col, val):

        #col==new_val
        search_condition = None
        col_type = col.type.__class__

        # Make sure we only add those columns into search criteria for which the serach value is valid
        # log.warn(col_type)
        # log.warn(val)
        if col_type in (VARCHAR, UnicodeText, Unicode, String, TEXT,
                                  Text, NCHAR, NVARCHAR, CHAR, CLOB):

            search_condition = (col==val)

        elif col_type in (BOOLEAN, Boolean, Binary):
            if val.lower() in  ['0', '1', 'true', 'false']:
                search_condition = (col==val.title())

        elif col_type in (BIGINT, BigInteger, INT, INTEGER, Integer, Interval,
                          NUMERIC, Numeric, SMALLINT, SmallInteger):

            if val.isdigit():
                search_condition = (col==val)

        elif col_type in (DECIMAL, FLOAT, Float, REAL):
            if val.replace('.', '').isdigit():
                search_condition = (col==val)

        # date time will require some complex processing
        #.filter(Token.timestamp.between(*DateTime.from_string("2015-05-08 07:19:35.128909").range())
        elif col_type in (DATE, Date):
            try:
                date_val = dates_and_times.Date.from_string(val)
                search_condition = col.between(*date_val.range())
            except ValueError:
                pass

        elif col_type in (Time, TIME):
            try:
                time_val = dates_and_times.Time.from_string(val)
                search_condition = col.between(*time_val.range())
            except ValueError:
                pass
        elif col_type in (DATETIME, DateTime, TIMESTAMP):
            try:
                date_val = dates_and_times.DateTime.from_string(val)
                search_condition = col.between(*date_val.range())
            except ValueError:
                pass

        return search_condition

    def list(self):
        """
        The listing view - Lists all the records with pagination
        """

        p = int(self.request.params.get('p', '1'))

        start_idx = self.list_recs_per_page * (p - 1)

        pk_col = list(self.model.__table__.primary_key.columns.keys())[0]
        pk_col = self.model.__table__.primary_key.columns[pk_col]

        query = self.db_session.query(self.model)
        count_query = self.db_session.query(func.count(pk_col))
        #process search query if given
        if self.request.GET.get('q', ''):
            search_conditions = []
            search_term = self.request.GET['q'].strip()
            for k,v in self.request.GET.items():
                if k.startswith("_sf_"):
                    col = getattr(self.model, v)

                    #can_add, new_val = self._is_valid_comparison_value(col.type.__class__, search_term)
                    search_condition = self._get_search_condition(col, search_term)
                    log.error(search_condition)
                    if search_condition is not None:
                        search_conditions.append(search_condition)
            
            log.warn(search_conditions)
            query = query.filter(or_(*search_conditions))
            count_query = count_query.filter(or_(*search_conditions))

        sort_ascending = self.request.GET.get('sa', None)
        sort_descending = self.request.GET.get('sd', None)
        if sort_ascending:
            query = query.order_by(sort_ascending)
        elif sort_descending:
            query = query.order_by(sort_descending + " desc")
        elif self.list_sort_by is not None:
            query = query.order_by(self.list_sort_by)

        query = query.slice(start_idx, start_idx + self.list_recs_per_page)

        records = query

        columns = []

        # Determine what columns need to be displayed
        if self.list_only is not None:
            columns = self.list_only

        elif self.list_exclude is not None:
            for column in list(self.model.__table__.columns.keys()):
                if column not in self.list_exclude:
                    columns.append(column)

        else:
            columns = list(self.model.__table__.columns.keys())

        # calculate number of pages
        total_recs = count_query.scalar()

        pages = get_pages(total_recs, p, self.list_recs_per_page, self.list_max_pages)

        # determine primary key columns
        primary_key_columns = list(self.model.__table__.primary_key.columns.keys())

        ret_dict = {
            'base_template': self.base_template, 'friendly_name': self.friendly_name,
            'columns': columns, 'primary_key_columns': primary_key_columns,
            'records': records, 'pages': pages, 'current_page': p,
            'total_records': total_recs, 'records_per_page': self.list_recs_per_page,
            'list_field_args': self.list_field_args,
            'model_record_counts': self._models_rec_count_if_needed(),
            'actions': self.list_actions, 'per_record_actions': self.list_per_record_actions
        }
        
        return dict(list(ret_dict.items()) + list(self.template_extra_params.items()))

    def _get_add_edit_form(self, action_type, R=None):
        exclude_list = self._get_exclude_list(action_type)
        #print("************************")
        #print(self.add_edit_field_args)
        #print(self._get_modelform_field_args())

        cols = get_columns(self.model, 'primary_key')
        ModelForm = dojo_model_form(self.model, self.db_session, exclude=exclude_list,
                                    field_args=self._get_modelform_field_args())

        #check for field data and set proper attributes accordingly
        for field_name, field_data in list(self.add_edit_field_args.items()):
            field = getattr(ModelForm, field_name)

            if 'choices' in field_data or 'choices_fields' in field_data:
                field.field_class = DojoSelectField

        if 'edit' == action_type:
            f = ModelForm(self.request.POST, R, request_obj=self.request, use_csrf_protection=True)
        else:
            f = ModelForm(self.request.POST, request_obj=self.request, use_csrf_protection=True)

        #check for field data and set proper attributes accordingly
        for field_name, field_data in list(self.add_edit_field_args.items()):
            field = getattr(f, field_name)

            if 'choices' in field_data:
                field.coerce = int
                field.choices = field_data['choices']
                #field.validators = []

            if 'choices_fields' in field_data:
                recs = self.db_session.query(*field_data['choices_fields']).all()

                table_cols = get_columns(self.model)
                for table_col in table_cols:
                    if table_col.property.columns[0].name == field_name and \
                    table_col.property.columns[0].nullable:
                        field.validators = []
                        recs.insert(0, (None, ''))

                field.choices = recs
                #field.validators = []

        return f

    def _redirect(self, location):
        """
        If came_from is set in session, redirects to it's value otherwise
        redirects to the location passed
        """

        if self.request.session.get('came_from', None):
            return HTTPFound(location=self.request.session.get('came_from'))
        else:
            return HTTPFound(location=location)

    def add(self):
        """
        The add record view
        """

        f = self._get_add_edit_form('add')

        if 'POST' == self.request.method and 'form.submitted' in self.request.params:
            #assert False
            #if f.validate():
            if True:
                obj = self.model()
                for fname, f_field in list(f._fields.items()):
                    if hasattr(f_field, 'choices') and f_field.data in ['', 'None']:
                        f_field.data = None

                f.populate_obj(obj)
                self.db_session.add(obj)

                self.request.session.flash(self.friendly_name + " added successfully!")
                #return HTTPFound(location=os.path.dirname(self.request.current_route_url()))
                return self._redirect(os.path.dirname(self.request.current_route_url()))

        ret_dict = {'base_template': self.base_template, 'friendly_name': self.friendly_name,
                    'model_record_counts': self._models_rec_count_if_needed(),
                    'form': f, "action_type": "add"}
        return dict(list(ret_dict.items()) + list(self.template_extra_params.items()))

    def edit(self):
        """
        The edit and update record view
        """

        R = self._get_rec_from_pk_val()
        f = self._get_add_edit_form('edit', R)

        if 'POST' == self.request.method and 'form.submitted' in self.request.params:
            #if f.validate():
            if True:
                for fname, f_field in list(f._fields.items()):
                    if hasattr(f_field, 'choices') and f_field.data in ['', 'None']:
                        f_field.data = None

                f.populate_obj(R)

                self.request.session.flash(self.friendly_name + " updated successfully!")
                #return HTTPFound(location=os.path.dirname(os.path.dirname(self.request.current_route_url())))
                return self._redirect(os.path.dirname(os.path.dirname(self.request.current_route_url())))

        ret_dict = {'base_template': self.base_template,
                    'model_record_counts': self._models_rec_count_if_needed(),
                    'friendly_name': self.friendly_name, 'form': f, "action_type": "edit"}
        return dict(list(ret_dict.items()) + list(self.template_extra_params.items()))

    def delete(self):
        """
        The record delete view

        TODO:

          * Later may need to add support for composite primary keys here.
        """

        R = self._get_rec_from_pk_val()
        try:
            self.db_session.delete(R)
            self.db_session.flush()
        except IntegrityError as exp:
            return HTTPNotAcceptable(
                detail="Cannot delete category as it has dependent records\n" + str(exp))

        self.request.session.flash(self.friendly_name + " deleted successfully!")

        #return HTTPFound(location=os.path.dirname(os.path.dirname(self.request.current_route_url())))
        return self._redirect(os.path.dirname(os.path.dirname(self.request.current_route_url())))

    def details(self):
        """
        The record details view
        """

        R = self._get_rec_from_pk_val()
        columns = list(self.model.__table__.columns.keys())
        primary_key_columns = list(self.model.__table__.primary_key.columns.keys())

        ret_dict = {'base_template': self.base_template, 'R': R,
                    'friendly_name': self.friendly_name,
                    'model_record_counts': self._models_rec_count_if_needed(),
                    'columns': columns, 'primary_key_columns': primary_key_columns,
                    'actions': self.detail_actions} 
        return dict(list(ret_dict.items()) + list(self.template_extra_params.items()))

