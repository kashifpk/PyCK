"""
This module contains some database models and a database session for use with test cases
"""

from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, ForeignKey, Integer, DateTime,
                        Unicode, UnicodeText, Boolean)
from sqlalchemy.orm import backref, relationship
from sqlalchemy.orm import sessionmaker

db_engine = create_engine("sqlite://")
Base = declarative_base()

Session = sessionmaker(bind=db_engine)
db_session = Session()


class User(Base):
    "Users table"

    __tablename__ = 'users'

    user_id = Column(Unicode(100), primary_key=True)
    password = Column(Unicode(100))


class Category(Base):
    "Blog category"

    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(150), nullable=False)
    description = Column(Unicode(500), nullable=True)

    parent_category = Column(Integer, ForeignKey("categories.id"), nullable=True)


class Post(Base):
    "Holds blog posts"

    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(Unicode(150), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    body = Column(UnicodeText, nullable=False)
    view_count = Column(Integer, default=0)
    comments_allowed = Column(Boolean, default=True)

    # FKs
    user_id = Column(Unicode(100), ForeignKey(User.user_id))
    category_id = Column(Integer, ForeignKey(Category.id))

    # Relationships
    category = relationship(Category, backref=backref('blog_posts'))


class Comment(Base):
    "Holds comments for a blog post"

    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    body = Column(UnicodeText, nullable=False)
    commentor = Column(Unicode(250))

    # FKs
    post_id = Column(Integer, ForeignKey(Post.id))

    # Relationships
    post = relationship(Post, backref=backref('comments'))
