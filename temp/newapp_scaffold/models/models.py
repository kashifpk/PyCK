from sqlalchemy import (
    Column,
    Integer,
    Text,
    )

from . import DBSession, Base

#class MyModel(Base):
#    __tablename__ = 'my_model'
#    id = Column(Integer, primary_key=True)
#    title = Column(Text, unique=True)
#    content = Column(Text)
#
#    def __init__(self, title, content):
#        self.title = title
#        self.content = content

