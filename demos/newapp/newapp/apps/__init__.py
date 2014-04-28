# This list contains all the enabled apps for the project, when you add a new app, add it to this list
# to make it accessible by the project.

import importlib

PROJECT_NAME = 'newapp'
project_package = importlib.import_module("newapp")

#from . import app1, app2
#enabled_apps = [app1, app2]

enabled_apps = []

