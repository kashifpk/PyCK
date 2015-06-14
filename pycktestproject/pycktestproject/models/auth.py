from sqlalchemy import (
    Column,
    Integer,
    Unicode,
    )
from sqlalchemy import ForeignKey
from sqlalchemy.orm import backref, relationship
import hashlib

from . import db, Base


# RBAC models
class Permission(Base):
    __tablename__ = 'permissions'

    permission = Column(Unicode(100), primary_key=True)
    description = Column(Unicode(250))


class RoutePermission(Base):
    __tablename__ = 'route_permissions'

    route_name = Column(Unicode(200), primary_key=True)
    method = Column(Unicode(30), default='ALL', primary_key=True)
    permission = Column(Unicode(100), ForeignKey(Permission.permission), primary_key=True)


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Unicode(100), primary_key=True)
    password = Column(Unicode(40))

    @classmethod
    def login(cls, username, password, request=None):
        "Find the user in the DB and validate password"
        
        user = db.query(cls).filter_by(user_id=username).first()
        if not user:
            return ("NOT FOUND", None)

        elif hashlib.sha1(password).hexdigest() != user.password:
            return ("AUTH FAILED", user)

        else:
            if request:
                request.session['logged_in_user'] = user.user_id

                # Get user permissions and store them into
                # request.session['auth_user_permissions']
                user_permissions = []
                permissions = db.query(UserPermission.permission).filter_by(
                    user_id=user.user_id).all()
    
                for permission in permissions:
                    user_permissions.append(permission[0])
    
                request.session['auth_user_permissions'] = user_permissions
            
            return ("OK", user)

    @classmethod
    def logout(cls, request):
        "Set the user as logged out"
        
        del request.session['logged_in_user']
        del request.session['auth_user_permissions']


class UserPermission(Base):
    __tablename__ = 'user_permissions'

    user_id = Column(Unicode(100), ForeignKey(User.user_id), primary_key=True)
    permission = Column(Unicode(100), ForeignKey(Permission.permission), primary_key=True)

    user = relationship(User, backref=backref('permissions'))
