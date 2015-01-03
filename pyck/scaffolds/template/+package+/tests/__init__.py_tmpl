import unittest

import os.path

from pyramid import testing
from paste.deploy import appconfig
from sqlalchemy import create_engine
from webtest import TestApp

from .. import main
from ..models import db, Base

here = os.path.dirname(__file__)
if os.path.exists(os.path.join(here, '../../', 'test.ini')):
    settings = appconfig('config:' + os.path.join(here, '../../', 'test.ini'))


class TestBase(unittest.TestCase):
    "Base class for test cases (unit tests) tuned for pyck projects"

    @classmethod
    def setUpClass(cls):
        cls.engine = create_engine(settings.get('sqlalchemy.url', 'sqlite://'))
        Base.metadata.drop_all(cls.engine)
        Base.metadata.create_all(cls.engine)

    def setUp(self):
        self.config = testing.setUp()
        db.configure(bind=self.engine)

    def tearDown(self):
        db.remove()
        testing.tearDown()


class FunctionalTestBase(TestBase):

    @classmethod
    def setUpClass(cls):
        cls.app = main({}, **settings)
        super(FunctionalTestBase, cls).setUpClass()

    def setUp(self):
        self.app = TestApp(self.app)
        self.config = testing.setUp()
        super(FunctionalTestBase, self).setUp()

