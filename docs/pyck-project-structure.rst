Structure of a PyCK Project
===========================

Here is the structure of a typical PyCK project (as though of till now) assuming a project named **combined_apps** and one pluggable application named **blog** ::

    combined_apps/
    |-- CHANGES.txt
    |-- MANIFEST.in
    |-- README.txt
    |-- combined_apps
    |   |-- __init__.py
    |   
    |   |-- apps
    |   |   |-- __init__.py
    |   |   `-- blog
    |   |       |-- __init__.py
    |   |       |-- controllers
    |   |       |   |-- __init__.py
    |   |       |   |-- views.py
    |   |       |-- models
    |   |       |   |-- __init__.py
    |   |       |   |-- models.py
    |   |       |-- scripts
    |   |       |   |-- __init__.py
    |   |       |   |-- populate.py
    |   |       |-- static
    |   |       |   |-- favicon.ico
    |   |       |   |-- footerbg.png
    |   |       |   |-- headerbg.png
    |   |       |   |-- ie6.css
    |   |       |   |-- middlebg.png
    |   |       |   |-- pylons.css
    |   |       |   |-- pyramid-small.png
    |   |       |   |-- pyramid.png
    |   |       |   `-- transparent.gif
    |   |       |-- templates
    |   |       |   |-- mytemplate.mako
    |   |       `-- tests
    |   |           |-- __init__.py
    |   |           |-- tests.py
    |   |-- controllers
    |   |   |-- __init__.py
    |   |   |-- views.py
    |   |-- models
    |   |   |-- __init__.py
    |   |   |-- models.py
    |   |-- scripts
    |   |   |-- __init__.py
    |   |   |-- populate.py
    |   |-- static
    |   |   |-- favicon.ico
    |   |   |-- footerbg.png
    |   |   |-- headerbg.png
    |   |   |-- ie6.css
    |   |   |-- middlebg.png
    |   |   |-- pylons.css
    |   |   |-- pyramid-small.png
    |   |   |-- pyramid.png
    |   |   `-- transparent.gif
    |   |-- templates
    |   |   |-- mytemplate.mako
    |   `-- tests
    |       |-- __init__.py
    |       |-- tests.py
    |-- combined_apps.db
    |-- combined_apps.egg-info
    |   |-- PKG-INFO
    |   |-- SOURCES.txt
    |   |-- dependency_links.txt
    |   |-- entry_points.txt
    |   |-- not-zip-safe
    |   |-- requires.txt
    |   `-- top_level.txt
    |-- development.ini
    |-- production.ini
    |-- setup.cfg
    `-- setup.py

