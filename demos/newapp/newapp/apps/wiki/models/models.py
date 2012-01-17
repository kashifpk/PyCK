from sqlalchemy import (
    Column,
    Integer,
    Text,
    Unicode
    )

from . import DBSession, Base

class Page(Base):
    __tablename__ = 'pages'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode, unique=True)
    content = Column(Text)

    def __init__(self, title='', content=''):
        self.title = title
        self.content = content

