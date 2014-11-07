import unittest
from pyck.controllers.crud_controller import add_crud_handler, CRUDController
from pyramid import testing

from dummy_db import db_session, db_engine, Base, User


class UserCRUDController(CRUDController):
    model = User
    db_session = db_session


class TestCRUD(unittest.TestCase):

    def setUp(self):
        self.config = testing.setUp()
        self.config.include('pyramid_handlers')
        Base.metadata.create_all(db_engine)
        add_crud_handler(self.config, 'user', '/user', UserCRUDController)

    def tearDown(self):
        testing.tearDown()

    def test_01_crud_controller_routes(self):
        "Test to check all CRUD routes are created correctly"

        introspector = self.config.introspector
        crud_routes = {'userCRUD_list': '/user/',
                       'userCRUD_add': '/user/add',
                       'userCRUD_edit': '/user/edit/{PK}',
                       'userCRUD_details': '/user/details/{PK}',
                       'userCRUD_delete': '/user/delete/{PK}'}

        for route_name in crud_routes:
            self.assertIsNotNone(introspector.get('routes', route_name))
            self.assertEquals(introspector.get('routes', route_name)['pattern'], crud_routes[route_name])
