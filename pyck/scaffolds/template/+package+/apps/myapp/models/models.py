from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    )

from . import DBSession, Base

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(200), unique=True)
    content = Column(Text)

    def __init__(self, title, content):
        self.title = title
        self.content = content

