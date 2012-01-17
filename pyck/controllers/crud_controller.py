from pyramid_handlers import action
from pyramid.response import Response

def add_crud_handler(config, route_name_prefix='', url_pattern_prefix='', handler_class=None):
    """
    A utility function to quickly add all crud related routes and set them to the crud handler class with one function call, for example::
    
        from pyck.controllers import add_crud_handler
        from controllers.views import WikiCRUDController
        .
        .
        .
        add_crud_handler(config, APP_NAME + '.', '/crud', WikiCRUDController)
    
    :param config:
        The application config object
    :param route_name_prefix:
        Optional string prefix to add to all route names. Useful if you're adding multiple CRUD controllers and want to avoid route name conflicts.
    :param url_pattern_prefix:
        Optional string prefix to add to all crud related url patterns
    :param exclude:
        An optional iterable with the property names that should be excluded
        from the form. All other properties will have fields.
    :param handler_class:
        The handler class that is used to handle CRUD requests. Must be sub-class of :class:`pyck.controllers.CRUDController`
    
    """
    config.add_handler(route_name_prefix + '.CRUD_list',
                       url_pattern_prefix + '/',
                       handler=handler_class,
                       action='list')
    
    config.add_handler(route_name_prefix + '.CRUD',
                       url_pattern_prefix + '/{action}',
                       handler=handler_class)
    
    config.add_handler(route_name_prefix + '.CRUD_PK',
                       url_pattern_prefix + '/{action}/{PK}',
                       handler=handler_class)

class CRUDController(object):
    """
    CRUDController class. Provides a ready to use and configurable CRUD interface for any SQLAlchemy model.
    
    TODO:
      * More documentation of various options and methods
      * A CRUDController tutorial
      * Tests for the controller
    
    """
    
    model = None
    friendly_name = None
    db_session = None
    
    __autoexpose__ = None
    
    #Listing page related settings
    list_recs_per_page = 10
    list_only = None
    list_exclude = None
    list_actions = [
                    {'link_text': 'Add {friendly_name}', 'link_url': 'add'},
                   ]
    
    list_per_record_actions = [
                    {'link_text': 'Details', 'link_url': 'details/{PK}'},
                    {'link_text': 'Edit', 'link_url': 'edit/{PK}'},
                    {'link_text': 'Delete', 'link_url': 'delete/{PK}'},
                   ]
    
    def __init__(self, request):
        self.request = request
        
        if self.db_session is None:
            raise ValueError("Must provide a SQLAlchemy database session object as db_session")
        
        if self.friendly_name is None:
            self.friendly_name = self.model.__tablename__
    
    @action(renderer='pyck:templates/crud/list.mako')
    def list(self):
        """
        The listing view - Lists all the records with pagination
        """
        
        p = int(self.request.params.get('p', '1'))
        
        start_idx = self.list_recs_per_page*(p-1)
        
        records = self.db_session.query(self.model).slice(start_idx, start_idx+self.list_recs_per_page)
        
        columns = []
        
        # Determine what columns need to be displayed
        if self.list_only is not None:
            columns = self.list_only
            
        elif self.list_exclude is not None:
            for column in self.model.__table__.columns.keys():
                if column not in self.list_exclude:
                    columns.append(column)
            
        else:
            columns = self.model.__table__.columns.keys()
        
        # calculate number of pages
        total_recs = self.db_session.query(self.model).count()
        total_pages = total_recs/self.list_recs_per_page
        
        if total_recs%self.list_recs_per_page>0:
            total_pages += 1
        
        # determine primary key columns
        primary_key_columns = self.model.__table__.primary_key.columns.keys()
        
        return {'friendly_name': self.friendly_name,
                'columns': columns, 'primary_key_columns': primary_key_columns,
                'records': records, 'pages': total_pages,
                'actions': self.list_actions, 'per_record_actions': self.list_per_record_actions}
    
    def add(self):
        """
        The add record view
        """
        return Response("Add a record Page")
    
    def edit(self):
        """
        The edit and update record view
        """
        return Response("Edit Page")
    
    def delete(self):
        """
        The record delete view
        """
        return Response("Delete Page")
    