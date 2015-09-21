import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

import importlib
import hashlib
from ..apps import enabled_apps
from .. import load_project_settings

from ..models import (
    db,
    User,
    Permission,
    RoutePermission,
    UserPermission,
    Base,
    )


def usage(argv):
    cmd = os.path.basename(argv[0])
    print(('usage: %s <config_uri>\n'
          '(example: "%s development.ini")' % (cmd, cmd)))
    sys.exit(1)


def populate_auth_data():
    "Authentication related basic user and permission setup"

    users = [
        {'user_id': 'admin', 'password': hashlib.sha1('admin'.encode('utf-8')).hexdigest()}
    ]

    permissions = [
        {'permission': 'admin', 'description': 'Manage administrative section'},
    ]

    user_permissions = [
        {'user_id': 'admin', 'permission': 'admin'},
    ]

    route_permissions = [
        {'route_name': 'pyckauth_manager', 'method': 'ALL', 'permission': 'admin'},
        {'route_name': 'pyckauth_users', 'method': 'ALL', 'permission': 'admin'},
        {'route_name': 'pyckauth_permissions', 'method': 'ALL', 'permission': 'admin'},
        {'route_name': 'pyckauth_routes', 'method': 'ALL', 'permission': 'admin'},
        {'route_name': 'admin.admin_index', 'method': 'ALL', 'permission': 'admin'},
    ]

    for user in users:
        if not db.query(User).filter_by(user_id=user['user_id']).first():
            db.add(User(user_id=user['user_id'], password=user['password']))
            db.flush()

    for permission in permissions:
        if not db.query(Permission).filter_by(permission=permission['permission']).first():
            db.add(
                Permission(permission=permission['permission'],
                           description=permission['description'])
            )
            db.flush()

    for user_permission in user_permissions:
        if not db.query(UserPermission).filter_by(
                user_id=user_permission['user_id'],
                permission=user_permission['permission']).first():

            db.add(
                UserPermission(
                    user_id=user_permission['user_id'],
                    permission=user_permission['permission']
                )
            )
            db.flush()

    for route_permission in route_permissions:
        if not db.query(RoutePermission).filter_by(
                route_name=route_permission['route_name'],
                method=route_permission['method'],
                permission=route_permission['permission']).first():

            db.add(
                RoutePermission(
                    route_name=route_permission['route_name'],
                    method=route_permission['method'],
                    permission=route_permission['permission']
                )
            )
            db.flush()


def main(argv=sys.argv):
    if len(argv) != 2:
        usage(argv)

    load_project_settings()

    config_uri = argv[1]
    setup_logging(config_uri)
    settings = get_appsettings(config_uri)
    engine = engine_from_config(settings, 'sqlalchemy.')
    db.configure(bind=engine)
    db.autoflush = True
    Base.metadata.create_all(engine)
    with transaction.manager:

        #Authentication related basic user and permission setup
        populate_auth_data()
        db.flush()

    #populate application models
    for app in enabled_apps:
        app_name = app.APP_NAME
        app_module = importlib.import_module("apps.%s.scripts.populate" % app_name)
        #print("App Module: %s\n" % app_module.__name__)

        try:
            app_module.populate_app(engine, db)
        except Exception as e:
            print((repr(e)))
