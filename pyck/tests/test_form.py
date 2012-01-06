import unittest

class TestForm(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_it(self):
        from .views import my_view
        request = testing.DummyRequest()
        info = my_view(request)
        self.assertEqual(info['one'].name, 'one')
        self.assertEqual(info['project'], 'newapp')
