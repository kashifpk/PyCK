"""
PyCK Admin Extension
====================

Admin extension that automtically creates CRUD interfaces for all database models
(or a selected list of models)

"""

import os.path
from pyramid_handlers import action
from pyramid.response import Response

from pyramid.httpexceptions import HTTPFound

import pyck
from pyck.forms import model_form
from pyck.lib.models import get_columns
from pyck.controllers import CRUDController, add_crud_handler


def add_admin_handler(config, db_session, models=None, route_name_prefix='',
                      url_pattern_prefix='', handler_class=None, models_field_args={}):
    """
    A utility function to quickly add all admin related routes and set them to the admin handler class with one function
    call, for example::

        from pyck.ext import add_admin_handler, AdminController
        from pyck.lib import get_models
        import my_application_package_name_here

        # Place this with the config.add_route calls
        add_admin_handler(config, db, get_models(my_application_package_name_here), 'admin', '/admin',
                          AdminController)

    :param config:
        The application config object

    :param db:
        The database session object

    :param models:
        Note: For backward compatibility this parameter can either be a list (old) or a dictionary (new).
        List/Dictionary of models for to include in the admin panel.
        get_models funcion can be used to include all models.

    :param route_name_prefix:
        Optional string prefix to add to all route names generated inside the admin panel.

    :param url_pattern_prefix:
        Optional string prefix to add to all admin section related url patterns

    :param handler_class:
        The AdminController handler class. 

    :param models_field_args:
        A dictionary with key being the model name and value being the field args value for that model.

        Example::

        model_field_args = {'Product': {'category_id' : {
                                                            'widget' : Select()
                                                        }
                                        },
                            'Category': {'description' : {
                                                            'widget' : TextArea()
                                                        }
                                        },
                            }
    """

    handler_class.db_session = db_session
    handler_class.models = models
    all_models = []

    if dict == type(models):
        for appname, app_models in models.iteritems():
            for model in app_models:
                all_models.append(model)
                tablename = model.__tablename__
                handler_class.table_models[tablename] = model
    else:
        all_models = models
        for model in models:
            tablename = model.__tablename__
            handler_class.table_models[tablename] = model

    handler_class.route_prefix = route_name_prefix

    config.add_handler(route_name_prefix + 'admin_index',
                       url_pattern_prefix + '/',
                       handler=handler_class,
                       action='index')

    if all_models:
        for model in all_models:
            # TODO: Do model_field_args processing here.

            add_edit_field_args = {}
            list_field_args = {}
            FK_cols = get_columns(model, 'foreign_key')
            for FK in FK_cols:
                db_col = list(FK.foreign_keys)[0].column.name
                display_col = db_col

                # If target column is integer, set the column next to it as display column,
                # for non-int columns keep the display column same as the db column
                if int == list(FK.foreign_keys)[0].column.table.columns[db_col].type.python_type:
                    table_cols = list(FK.foreign_keys)[0].column.table.columns.keys()
                    d_idx = table_cols.index(db_col) + 1
                    if len(table_cols) > d_idx:
                        display_col = table_cols[d_idx]

                db_col = list(FK.foreign_keys)[0].column.table.columns[db_col]
                display_col = list(FK.foreign_keys)[0].column.table.columns[display_col]
                add_edit_field_args[FK.name] = dict(choices_fields=[db_col, display_col])

                # See if there is any relationship for current FK col, if yes, add reference to target
                # column in target table using that relationship
                for RS in model.__mapper__.relationships:
                    r_col = list(RS.local_columns)[0]
                    if r_col.name == FK.name:
                        list_field_args[FK.name] = dict(display_field="%s.%s" % (RS.key, display_col.name))
                        break

            CC = type(model.__name__ + 'CRUDController', (pyck.controllers.CRUDController,),
                      {'model': model, 'db_session': db_session,
                       'base_template': handler_class.base_template,
                       'add_edit_field_args': add_edit_field_args,
                       'list_field_args': list_field_args,
                       'template_extra_params': {'models': models, 'route_prefix': route_name_prefix}
                      }
                     )

            add_crud_handler(config, route_name_prefix + model.__name__,
                             url_pattern_prefix + '/' + model.__tablename__, CC)


class AdminController(object):
    """
    Enables automatic Admin interface generation from database models.
    The :class:`pyck.ext.admin_controller.AdminController` allows you to quickly enable Admin interface for any number
    of database models you like. To use AdminController at minimum these steps must be followed.


    1. In your application's routes settings, specify the url where the CRUD interface should be displayed. You can use
    the :func:`pyck.ext.admin_controller.add_admin_handler` function for it. For example in your __init__.py; put code
    like::

        from pyck.ext import AdminController, add_admin_handler
        from pyck.lib import get_models
        import my_application_package_name_here

        # Place this with the config.add_route calls
        add_admin_handler(config, db, get_models(my_application_package_name_here), 'admin', '/admin',
                          AdminController)

    and that's all you need to do to get a fully operation Admin interface.

    **Configuration Options**

    These parameters are to be set as class properties in a sub-class of AdminController

    ** TODO **

    * More documentation of various options and methods
    * An AdminController tutorial
    * Tests for the controller
    * Add support for composite primary keys

    """

    models = None
    table_models = {}
    db_session = None
    route_prefix = ''
    #base_template = 'admin_base.mako'
    base_template = 'pyck:templates/admin/admin_base.mako'

    __autoexpose__ = None

    def __init__(self, request):
        self.request = request

        if self.db_session is None:
            raise ValueError("Must provide a SQLAlchemy database session object as db_session")

    @action(renderer='pyck:templates/admin/index.mako')
    def index(self):

        return {'base_template': self.base_template, 'models': self.models, 'route_prefix': self.route_prefix}
