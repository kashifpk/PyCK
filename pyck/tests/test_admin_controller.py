import unittest
from pyck.ext.admin_controller import add_admin_handler, AdminController

from pyramid import testing

from .dummy_db import db_session, db_engine, Base, User, Category, Post, Comment



class TestAdmin(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()
        self.config.include('pyramid_handlers')
        Base.metadata.create_all(db_engine)
        add_admin_handler(self.config, db_session, [User, Category, Post, Comment],
                          'admin.', '/admin', AdminController)

    def tearDown(self):
        testing.tearDown()

    def test_01_crud_controller_routes(self):
        "Test to check all CRUD routes are created correctly"

        introspector = self.config.introspector
        admin_routes = {'admin.admin_index': '/admin/',
                       'admin.UserCRUD_add': '/admin/users/add',
                       'admin.UserCRUD_edit': '/admin/users/edit/{PK}',
                       'admin.UserCRUD_details': '/admin/users/details/{PK}',
                       'admin.UserCRUD_delete': '/admin/users/delete/{PK}',
                       'admin.PostCRUD_add': '/admin/posts/add',
                       'admin.PostCRUD_edit': '/admin/posts/edit/{PK}',
                       'admin.PostCRUD_details': '/admin/posts/details/{PK}',
                       'admin.PostCRUD_delete': '/admin/posts/delete/{PK}'}

        for route_name in admin_routes:
            self.assertIsNotNone(introspector.get('routes', route_name))
            self.assertEquals(introspector.get('routes', route_name)['pattern'], admin_routes[route_name])
