.. _changes:

Changes
============

This document lists the changes as versions progress

Whats new in 0.2.2
------------------

* Sessions support - Sessions come pre-configured now with a new PyCK project and the sample included has also been updated accordingly

* Forms support - Initial support for forms using WTForms has landed. Keeping with the structure forms are defined within a forms package inside the application package.

* A newly created project (and the sample project) now contains a contact form demonstrating forms usage.

    * Additionally forms also have CSRF (Cross Site Request Forgery) protection

* Flash messaging support is also in. Look at the contact form example (specifically its template and the home and base templates) to see flash messages in action.

**Whats next?** Focus now is to make forms more easy to use within PyCK. Upcoming versions are expected to contain more enhancements related to forms.


Whats new in 0.2.1
------------------

Some code refactoring to ease up a few things

* Moved sys.path addition settings to a seperate function named load_project_settings in project's __init__.py. This function is called by __init__.py's main function to load project specific settings and also called by the populate script. So the code is at one place instead of two places.

* For apps, moved the RenameTables SQA MetaBase to the model package's __init__.py so its a bit hidden from the developer as the developer just sees::

    from . import DBSession, Base

  in the model definition files. This also makes importing these into multiple model files much easier (since again the code is at a single location now)

* In the __init__.py of every model package (apps or the main project alike), we now import the models defined by that project/app and include them in the __all__ list so that instead of importing like::

    from myapp.models.models import MyModel

  now we can use::

    from myapp.models import MyModel

Whats new in 0.2.0
------------------

* tables created from models in apps are automatically prefixed by app name. For example: if you have an app named blog and it has a model Post where you have specified::

    __tablename__ = 'posts'

  it will automatically be created as **blog_posts** in the database. Your access to the table through the model remained same without any changes.

* Once you run python setup.py develop for your new project, a new command for creating an app becomes availabe to you. Instead of copying the sample app provided and adjusting it, now the whole struture is created for you. For details see

  :ref:`adding-apps`

  This feature is the reason that the version number bumped upto 0.2 :-)


Whats new in 0.1.6
------------------

* First fully operational version with pluggable apps along with their database models etc.

