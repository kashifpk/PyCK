import unittest
from pyck.forms import model_form
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column,
    Integer,
    Text,
    )

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    username = Column(Text, primary_key=True, nullable=False, default='admin')
    password = Column(Text, nullable=False)

    
class TestModelForm(unittest.TestCase):
    def setUp(self):
        UserForm = model_form(User)
        self.myform = UserForm()

    def tearDown(self):
        pass

    def test_01_properties_test(self):
        assert hasattr(self.myform, 'username')
        assert hasattr(self.myform, 'password')
    
    def test_02_has_as_p(self):
        assert hasattr(self.myform, 'as_p')
        assert callable(self.myform.as_p)
    
    def test_03_has_as_table(self):
        assert hasattr(self.myform, 'as_table')
        assert callable(self.myform.as_table)
    