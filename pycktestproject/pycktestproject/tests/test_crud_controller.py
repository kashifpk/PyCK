"""
Tests for the PyCK CRUD controller functionality that is generated via the admin controller
"""

from . import FunctionalTestBase


class TestAdminCRUDController(FunctionalTestBase):
    "Functional tests for the admin CRUD controllers"

    def test_models(self):
        for url in ['models/', 'models/add']:
            res = self.app.get('/admin/' + url)
            self.assertEqual(res.status_int, 200)

    def test_models2(self):
        for url in ['models2/', 'models2/add']:
            res = self.app.get('/admin/' + url)
            self.assertEqual(res.status_int, 200)