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
        if 0 == db.query(User).count():
            db.add(User(
                user_id='admin',
                password=hashlib.sha1('admin'.encode('utf-8')).hexdigest()))
            db.flush()

        if 0 == db.query(Permission).count():
            db.add(Permission(
                permission='admin',
                description='Manage administrative section'))
            db.flush()

        if 0 == db.query(UserPermission).count():
            db.add(UserPermission(
                user_id='admin',
                permission='admin'))
            db.flush()

        if 0 == db.query(RoutePermission).count():
            db.add(RoutePermission(
                route_name='pyckauth_manager',
                method='ALL',
                permission='admin'))
            db.flush()

    #populate application models
    for app in enabled_apps:
        app_name = app.APP_NAME
        app_module = importlib.import_module("apps.%s.scripts.populate" % app_name)
        #print("App Module: %s\n" % app_module.__name__)

        try:
            app_module.populate_app(engine, db)
        except Exception as exp:
            print(repr(exp))
