import unittest
from pyck.forms import Form
from wtforms import TextField, validators

class MyForm(Form):
    name = TextField("Name", [validators.required()])
    fname = TextField("Father's Name", [validators.required()])

    
class TestForm(unittest.TestCase):
    def setUp(self):
        self.myform = MyForm()

    def tearDown(self):
        pass

    def test_01_form_creation(self):
        assert 'name' == self.myform.name.name
        assert 'fname' == self.myform.fname.name
    
    def test_02_form_as_p_top_labels(self):
        assert '<label for="name">Name</label><br /> <input id="name" name="name" type="text" value="" />' in self.myform.as_p(labels='top')
    
    def test_03_form_as_p_left_labels(self):
        assert '<label for="name">Name</label> <input id="name" name="name" type="text" value="" />' in self.myform.as_p(labels='left')
    
    def test_04_form_as_p_bottom_labels(self):
        assert '<input id="name" name="name" type="text" value="" /> <br /><label for="name">Name</label>' in self.myform.as_p(labels='bottom')
    
    def test_05_form_as_p_right_labels(self):
        assert '<input id="name" name="name" type="text" value="" /> <label for="name">Name</label>' in self.myform.as_p(labels='right')
    
    def test_06_form_as_p_top_labels_top_errors(self):
        self.myform.validate()
        assert '<label for="name">Name</label><br /> <span class="errors">This field is required.</span><br /> <input id="name" name="name" type="text" value="" />' in self.myform.as_p(labels='top', errors='top')
    
    def test_07_form_as_p_top_labels_right_errors(self):
        self.myform.validate()
        assert '<label for="name">Name</label><br /> <input id="name" name="name" type="text" value="" /> <span class="errors">This field is required.</span>' in self.myform.as_p(labels='top', errors='right')
    
    def test_08_form_as_p_bottom_labels_top_errors(self):
        self.myform.validate()
        assert '<span class="errors">This field is required.</span><br /> <input id="name" name="name" type="text" value="" /> <br /><label for="name">Name</label>' in self.myform.as_p(labels='bottom', errors='top')
    
    def test_09_form_as_p_left_labels_right_errors(self):
        self.myform.validate()
        assert '<label for="name">Name</label> <input id="name" name="name" type="text" value="" /> <span class="errors">This field is required.</span>' in self.myform.as_p(labels='left', errors='right')
    
    def test_10_form_validation(self):
        self.myform = MyForm(name='Kashif', fname='Iftikhar')
        assert self.myform.validate()
    
    def test_11_form_data(self):
        self.myform = MyForm(name='Kashif', fname='Iftikhar')
        assert 'Kashif'==self.myform.name.data
        assert 'Iftikhar'==self.myform.fname.data
