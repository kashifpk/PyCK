from sqlalchemy.orm import relationship, backref
from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    UnicodeText,
    ForeignKey
    )

from . import DBSession, Base


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(200), unique=True)


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey(Category.id))
    name = Column(Unicode(200), unique=True)
    description = Column(UnicodeText)

    category = relationship(Category, backref=backref("products"))
