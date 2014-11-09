"""
Tests for the PyCK admin controller functionality
"""

from . import FunctionalTestBase


class TestAdminController(FunctionalTestBase):
    "Functional tests for the admin controller"

    def test_homepage(self):
        res = self.app.get('/admin/')
        self.assertEqual(res.status_int, 200)
