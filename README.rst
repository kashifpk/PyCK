.. _introduction:

Introduction
============

**PyCK** (Python Code Karigar); prounounced '*pick*' is/would be a web development framework
aiming to provide an easy to use yet powerful and flexible web framework for python developers.

Documentation for the project can be found at `PyCK Documentation <http://packages.python.org/PyCK/>`_

Background
----------

Of course, there are already a lot of great frameworks present for python like `Pylons <http://docs.pylonsproject.org/en/latest/docs/pylons.html>`_, `Django <https://www.djangoproject.com/>`_, `Pyramid <http://docs.pylonsproject.org/en/latest/docs/pyramid.html>`_, `BlueBream (Previously Zope) <http://bluebream.zope.org/>`_, `TurboGears2 <http://turbogears.org/>`_ that provide really cool
features for developing web applications in python, I feel like there was still something missing for my taste. So you can say that this project is starting to satisfy a personal itch.

Why Create PyCK?
*****************

Of all the frameworks mentioned above I liked some features of one framework and other features of another framework. Unfortunately I wasn't able to find all those features I like in any existing framework. For example Django probably is the most popular framework in python and for good reason, it has pluggable apps, extensible extensions like its admin panel, a lot of useful documentation and great community support. One of its biggest strengths is that a lot of apps are available for it which can be "plugged" into a new project to get things started really quickly. The problem is that django is very "opnionated", the choices like ORM, templating language, URL dispatching mechanism are all made for the developer and you are mostly stuck with them unless you are willing to put in a lot of extra effort into it.

Consider the following scenario, my favorite ORM is `SQLAlchemy <http://www.sqlalchemy.org/>`_ and for good reason. I can develop command line applications, traditional GUIs in GUI toolkits like Qt, GTK etc all using SQLAlchemy as the ORM to interact with the database. Now if I decide to use django, I need to learn and use its ORM, why can't I use the one I already am familiar and proficient with? Though I can but that breaks a lot of stuff in Django.

Pylons and Pyramid on the other hand are very "non-opinionated" frameworks. They both are very flexible and I really like the way things are done in these frameworks. I can use SQLAlchemy or any other ORM like SQLObject etc if I like. I can choose the templating language I want to use (which BTW would be `Mako <http://www.makotemplates.org/>`_). I can choose the URL handling mechanism (in Pyramid) be it URLDispatch or Traversal. But this flexiblity comes at a cost, building "ready-made" components for such frameworks isn't easily possible because we are not sure what the framework user will pick as technologies. So having pluggable apps or pre-built admin panels etc because tough.

So the solution? at least for me; I decided to build a framework based on Pyramid that makes the choices for the developers. If your choices are the same as mine, this framework would be ideal for you. Or if you are a new developer looking into python frameworks you can start here.

Discussion on various aspects of PyCK
-------------------------------------

:ref:`forms-library-choice`

:ref:`pyck-project-structure`

:ref:`pluggable-apps`

Current Features
-----------------

And what exactly are the choices?

* Uses **SQLAlchemy as the ORM**
* Uses **Mako as the templating language**
* Uses **URLDispatch as the resource location** - URL to code mapping mechanism
* Design supports **Pluggable applications** similar to Django
* Has easily **extendible components** like an admin panel, etc
* Uses `Dojo <http://dojotoolkit.org/>`_ for UI components, AJAX etc
* **Automatic form generation from database/SQLAlchemy models** (Using WTForms and custom code created on top of WTForms)

Future Plan
-----------

* Allow web applications to be easily **Themable**
* Ability to easily specify **separate view templates for mobile devices** (which may use specific libraries like Dojox.mobile)
