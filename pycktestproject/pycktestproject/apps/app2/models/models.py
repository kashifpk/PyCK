from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    )

from . import db, Base

class App2Table(Base):
    __tablename__ = 'table_2'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(200), unique=True)

    def __init__(self, title, content):
        self.title = title

