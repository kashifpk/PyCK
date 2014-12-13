from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    )
from sqlalchemy import ForeignKey
from sqlalchemy.orm import backref, relationship

from . import db, Base


# RBAC models
class Permission(Base):
    "Permissions/Roles"

    __tablename__ = 'permissions'

    permission = Column(Unicode(100), primary_key=True)
    description = Column(Unicode(250))


class RoutePermission(Base):
    "Permissions for a specific route/url"

    __tablename__ = 'route_permissions'

    route_name = Column(Unicode(200), primary_key=True)
    method = Column(Unicode(30), default=u'ALL', primary_key=True)
    permission = Column(Unicode(100), ForeignKey(Permission.permission), primary_key=True)


class User(Base):
    "Users that are allowed login"

    __tablename__ = 'users'

    user_id = Column(Unicode(100), primary_key=True)
    password = Column(Unicode(40))


class UserPermission(Base):
    "Permissions/Roles that a user has"

    __tablename__ = 'user_permissions'

    user_id = Column(Unicode(100), ForeignKey(User.user_id), primary_key=True)
    permission = Column(Unicode(100), ForeignKey(Permission.permission), primary_key=True)

    user = relationship(User, backref=backref('permissions'))
