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


def add_admin_handler(config, db_session, models=None, route_name_prefix='', url_pattern_prefix='', handler_class=None):
    """
    A utility function to quickly add all admin related routes and set them to the admin handler class with one function call, for example::
    
        from pyck.ext import add_admin_handler, AdminController
        
        .
        .
        .
        add_admin_handler(config, APP_NAME + '.', '/crud', WikiCRUDController)
    
    :param config:
        The application config object
    :param route_name_prefix:
        Optional string prefix to add to all route names. Useful if you're adding multiple CRUD controllers and want to avoid route name conflicts.
    :param url_pattern_prefix:
        Optional string prefix to add to all crud related url patterns
    :param handler_class:
        The handler class that is used to handle CRUD requests. Must be sub-class of :class:`pyck.controllers.CRUDController`
    
    """
    
    handler_class.db_session = db_session
    handler_class.models = models
    
    config.add_handler(route_name_prefix + 'admin_index',
                       url_pattern_prefix + '/',
                       handler=handler_class,
                       action='index')
    
    if models:
        for model in models:
            
            CC = type(model.__name__ + 'CRUDController', (pyck.controllers.CRUDController,),
                      {'model': model, 'db_session': db_session, '_base_template': 'pyck:templates/admin/admin_base.mako'})
            
            add_crud_handler(config, 'admin_' + model.__name__, url_pattern_prefix + '/' + model.__tablename__, CC)
    
class AdminController(object):
    """
    Enables automatic Admin interface generation from database models. The :class:`pyck.ext.AdminController` allows you to quickly enable Admin interface for any number of database models you like. To use AdminController at minimum these steps must be followed.
    
    
    1. In your application's routes settings, specify the url where the CRUD interface should be displayed. You can use the :func:`pyck.controllers.add_crud_handler` method for it. For example in your __init__.py (if you're enabling CRUD for a model without your main project) or in your routes.py (if you're enabling CRUD for a model within an app in your project) put code like::
    
        from pyck.ext import AdminController, add_admin_handler
        from puck.lib import get_models
        # Place this with the config.add_route calls
        add_admin_handler(config, db_session, get_models(myapplicationpackagenamehere), 'admin', '/admin', AdminController)
    
    and that's all you need to do to get a fully operation CRUD interface. Take a look at the newapp sample app in demos for a working CRUD example in the Wiki app.
    
    **Configuration Options**
    
    These parameters are to be set as class properties in a sub-class of CRUDController
    
    **TODO**
    
    * More documentation of various options and methods
    * An AdminController tutorial
    * Tests for the controller
    * Add support for composite primary keys
    
    """
    
    models = []
    db_session = None
    
    __autoexpose__ = None
    
    def __init__(self, request):
        self.request = request
        
        if self.db_session is None:
            raise ValueError("Must provide a SQLAlchemy database session object as db_session")
    
    @action(renderer='pyck:templates/admin/index.mako')
    def index(self):
        
        return {'base_template': 'admin_base.mako', 'models': self.models}
    
    
