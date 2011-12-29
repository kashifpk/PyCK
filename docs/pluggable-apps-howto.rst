Pluggable application in PyCK
=============================

Pluggable apps are just like normal pyck (or pyramid) project with a few modifications. Scaffolds for generating a pluggable application structure will be coming shortly. For the time being, this page describes how a pluggable application needs to behave to be able to successfully integrated into a PyCK project with minimal effort.

Implement application_routes function in __init__.py
----------------------------------------------------

Taking a blog app as an example, in your app's __init__.py, implement a function like::

    def application_routes(config):
        config.add_route('blog.home', '/')
        config.add_route('blog.about', '/about')
        
        config.add_static_view('static', 'static', cache_max_age=3600)

And in your main project's __init__.py you can add the routes from this application using::

    config.include(application_routes, route_prefix='/blog')

This takes care of accessing your app correctly from within the main project.


Implement a populate_app function to your app's scripts/populate.py script
--------------------------------------------------------------------

This function will be called by the main project's populate script to automatically add tables and
records for the app to the project's database::

    def populate_app(engine, db_session):
    Base.metadata.create_all(engine)
    with transaction.manager:
        model = Post('Test', 'Just testing')
        db_session.add(model)
