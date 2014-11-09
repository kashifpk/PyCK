from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    )

from . import db, Base


# Create your models here.
class MyModel(Base):
    __tablename__ = 'models'

    id = Column(Integer, primary_key=True)
    name = Column(Unicode(100), unique=True)


class MySecondModel(Base):
    __tablename__ = 'models2'

    title = Column(Unicode(100), primary_key=True)
    description = Column(Unicode(100))
