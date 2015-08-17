from .. import PROJECT_NAME, project_package


APP_NAME = 'app1'
APP_BASE = '%s.apps.%s' % (PROJECT_NAME, APP_NAME)

from routes import application_routes

app_requires = ['sqlalchemy']
