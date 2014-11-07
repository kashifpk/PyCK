import unittest
from pyck.controllers.crud_controller import add_crud_handler, CRUDController
from pyramid import testing

from dummy_db import db_session, db_engine, Base, User


class UserCRUDController(CRUDController):
    model = User
    db_session = db_session


#class TestCRUD(unittest.TestCase):
#
#    def setUp(self):
#        self.config = testing.setUp()
#        self.config.include('pyramid_handlers')
#        Base.metadata.create_all(db_engine)
#        add_crud_handler(self.config, 'user', '/user', UserCRUDController)
#
#    def tearDown(self):
#        testing.tearDown()
#
#    def test_01_crud_controller(self):
#
#        pass
