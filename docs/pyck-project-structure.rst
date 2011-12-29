Structure of a PyCK Project
===========================

Here is the structure of a typical PyCK project (as though of till now) assuming a project named **combined_apps** and one pluggable application named **blog** ::

    combined_apps/
    |-- CHANGES.txt
    |-- MANIFEST.in
    |-- README.txt
    |-- combined_apps                         (The main project folder containing all the code)
    |   |-- __init__.py                   (Project's init file containing initialization code and routes)
    |   
    |   |-- apps                          (This folder contains any pluggable apps)
    |   |   |-- __init__.py               (This file contains enabled apps list and some utility stuff)
    |   |   `-- blog                      (A sample blog app that is pluggable)
    |   |       |-- __init__.py          (Apps initialization code & the application_routes function)
    |   |       |-- controllers          (The controllers folder containing all the controllers for the app)
    |   |       |   |-- __init__.py
    |   |       |-- models               (Application's models) 
    |   |       |   |-- __init__.py
    |   |       |-- scripts              (Other scripts including the populate script containing the populate_app function)
    |   |       |   |-- __init__.py
    |   |       |   |-- populate.py
    |   |       |-- static               (Application specific static media like images, css, javascript, etc)
    |   |       |-- templates            (Application's template - normally (but not compulsarily) in mako templating language) 
    |   |       `-- tests                (Application's Tests)
    |   |           |-- __init__.py
    |   |-- controllers                  (Main project's controllers)
    |   |   |-- __init__.py
    |   |-- models                       (Main project's models)
    |   |   |-- __init__.py
    |   |-- scripts                      (Main project's scripts including the populate script) 
    |   |   |-- __init__.py
    |   |   |-- populate.py
    |   |-- static                       (Main proejct's static media)
    |   |-- templates                    (Main project's templates)
    |   `-- tests                        (Main project's tests)
    |       |-- __init__.py
    |-- combined_apps.db                 (Project's DB if using sqlite)
    |-- combined_apps.egg-info           (Project's egg/setup related files)
    |-- development.ini                  (Project's configuration for development setup)
    |-- production.ini                   (Project's configuration for production deployment) 
    |-- setup.cfg                        (Configuration for the setup script)
    `-- setup.py                              (Project's setup script)

