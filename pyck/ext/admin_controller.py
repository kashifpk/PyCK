"""
PyCK Admin Extension
====================

Admin extension that automtically creates CRUD interfaces for all database models (or a selected list of models)

"""

import os.path
from pyramid_handlers import action
from pyramid.response import Response

from pyramid.httpexceptions import HTTPFound

import pyck
from pyck.forms import model_form
from pyck.controllers import CRUDController, add_crud_handler


def add_admin_handler(config, db_session, models=None, route_name_prefix='', url_pattern_prefix='', handler_class=None,
                      models_field_args={}):
    """
    A utility function to quickly add all admin related routes and set them to the admin handler class with one function
    call, for example::

        from pyck.ext import add_admin_handler, AdminController

        .
        .
        .
        add_admin_handler(config, APP_NAME + '.', '/crud', WikiCRUDController)

    :param config:
        The application config object

    :param route_name_prefix:
        Optional string prefix to add to all route names. Useful if you're adding multiple CRUD controllers and want to
        avoid route name conflicts.

    :param url_pattern_prefix:
        Optional string prefix to add to all crud related url patterns

    :param handler_class:
        The handler class that is used to handle CRUD requests. Must be sub-class of :class:`pyck.controllers.CRUDController`

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
    #>>> Product.category_id.property.columns[0].foreign_keys
-        #set([ForeignKey('categories.id')])
-        #>>> Product.name.property.columns[0].foreign_keys
-        #set([])
-        #Product.id.property.columns[0].autoincrement
-        #True
-
-        #ProductModelForm = model_form(Product, exclude=['id'], field_args = {
-        #                                                    'category_id' : {
-        #                                                    'widget' : Select()
-        #                                                    }
-        #                                                })
-        #ProductModelForm.category_id.field_class = SelectField
-        #
-        #product_form = ProductModelForm(request.POST)
-        #
-        #product_form.category_id.choices = categories
    """

    handler_class.db_session = db_session
    handler_class.models = models
    for model in models:
        tablename = model.__tablename__
        handler_class.table_models[tablename] = model

    handler_class.route_prefix = route_name_prefix

    config.add_handler(route_name_prefix + 'admin_index',
                       url_pattern_prefix + '/',
                       handler=handler_class,
                       action='index')

    if models:
        for model in models:

            CC = type(model.__name__ + 'CRUDController', (pyck.controllers.CRUDController,),
                      {'model': model, 'db_session': db_session,
                       'base_template': handler_class.base_template,
                       'template_extra_params': {'models': models, 'route_prefix': route_name_prefix}
                      }
                     )

            CC.add_edit_field_args = {}

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
        # Place this with the config.add_route calls
        add_admin_handler(config, db_session, get_models(myapplicationpackagenamehere), 'admin', '/admin',
                          AdminController)

    and that's all you need to do to get a fully operation Admin interface.

    **Configuration Options**

    These parameters are to be set as class properties in a sub-class of CRUDController

    **TODO**

    * More documentation of various options and methods
    * An AdminController tutorial
    * Tests for the controller
    * Add support for composite primary keys

    """

    models = []
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
