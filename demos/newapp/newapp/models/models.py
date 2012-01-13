from sqlalchemy import (
    Column,
    Integer,
    Text,
    Unicode
    )

from . import DBSession, Base

class Site(Base):
    __tablename__ = 'site'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode, unique=True)
    value = Column(Integer)

    def __init__(self, name, value):
        self.name = name
        self.value = value

