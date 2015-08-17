# This list contains all the enabled apps for the project, when you add a new app, add it to this list
# to make it accessible by the project.

import importlib

PROJECT_NAME = 'pycktestproject'
project_package = importlib.import_module("pycktestproject")

def has_app(app_name):
    "Checks if a given app is available in project's enabled apps"

    for app in enabled_apps:
        if app_name == app.__name__.split('.')[-1]:
            return True

    return False

from . import app1, app2
enabled_apps = [app1, app2]

#enabled_apps = []

