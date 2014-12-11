from sqlalchemy.ext.declarative import declarative_base
from zope.sqlalchemy import ZopeTransactionExtension
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

db = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

from .models import MyModel, MySecondModel
from .auth import Permission, User, UserPermission, RoutePermission

# Place additional model names here for ease of importing.
__all__ = ['db', 'Base', 'Permission', 'User', 'UserPermission', 'RoutePermission',
           'MyModel', 'MySecondModel']
