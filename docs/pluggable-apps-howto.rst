.. _pluggable-apps:

Pluggable application in PyCK
=============================

Pluggable apps are just like normal pyck (or pyramid) project with a few modifications. The advantage
of pluggable apps is that they can be moved from one project to another (re-used) with minimal effort.

Creating a pluggable application
---------------------------------

Once you have created your project and have executed::

    python setup.py develop

A command for creating new sub-apps becomes available to you. Assuming your project is named myproj, the command would be::

    myproj_newapp name_of_new_subapp

example::

    myproj_newapp blog


Things to remember:
-------------------

* You can have many sub applications and you can choose to enable/disable them. This is done by appending the subapp's name
  in the enabled_apps list in {proj}/apps/__init__.py

* Routes for your sub-application are present in a function named application_routes within
  {proj}/apps/{subapp}/routes.py, for the above example, myproj/apps/blog/routes.py

* It is a good practice to prefix the routes of your sub-app with the sub-app name, this is already being done
  for the default routes created with the subapp.

* There is a populate_app function in your app's scripts/populate.py script. This function will be called by the
  main project's populate script to automatically add tables and records for the app to the project's database

