.. _changes:

Changes
============

This document lists the changes as versions progress

What's new in 0.8.2
--------------------

* Colored logging on console. Now console actions like serving through pserve  or other methods outputs log
  messages in color. INFO messages are displayed in green, DEBUG messages are in blue, WARNING messages in
  yellow and ERROR messages in red.

What's new in 0.8.1
--------------------

* Fixed issue where app created but not included in enabled_apps causes project start-up failure
* Top-level application routes now reside in routes.py instead of __init__.py similar to sub-apps.
* {projname}_initdb renamed to {projname}_populate
* Renamed DBSession to db (it's more pythonic and shorter)
* Fixed bug - admin interface causes errors with non numeric primary keys
* In sub-app initialization now using::

    from .. import PROJECT_NAME, project_package

  instead of::

    from apps import PROJECT_NAME, project_package


What's new in 0.8
------------------

* Use 127.0.0.1 as ip for development.ini. For development.ini don't use 0.0.0.0 as it causes some issues
  requiring reloading on firefox (specially when using proxies). Just use 127.0.0.1, production.ini still
  uses 0.0.0.0

* Use `waitress <http://docs.pylonsproject.org/projects/waitress/en/latest/>`_ HTTP server

* Renamed populate_projname command to projname_initdb, all commands of a project starting from the project's
  name make more sense.

* Documentation updates

What's new in 0.7.5
-------------------

* Admin Controller is enabled by default under /admin for new PyCK projects

* Links to login, logout, admin and authentication section are included in the header

* Documentation fixes

* Minor refactoring


What's new in 0.7.2
-------------------

* The default admin permission was renamed from manage to admin since this name makes more sense

* Added wtdojo to requires for new projects


What's new in 0.7.1
-------------------

* Updates to documentation

* Design changes to make the default generated application look a bit better

* Removal of the default sample app and Site Model since now the auth models already provide the sample models required

* New PyCK Logos, new style for the login page

* If AdminController is enabled then successful login redirects to admin interface if not otherwise directed by 'came_from'
  session variable

* Minor CSS fix so that footer is properly bottom-aligned in the page


What's new in 0.7
-----------------

* Static routes (routes normally used for JS, images, CSS etc) are now ignored for authentication checking. Using Javascript
  frameworks like Dojo requires accessing quite a lot of files for a page and this can slow down the application checking for
  permissions for each of the static resource. Of course, you can disable it by commenting out the relevant code in your
  project's auth.py

* The newapp script now uses argparse instead of optparse to avoid deprecation warnings.

* Minor fix to admin controller to get rid of add errors for some models.

* Inclusion of dojo from google's CDN by default into admin and application base templates.

* Admin controller

    * now ignores relationship properties of a model while display add/edit forms.

    * Add and edit forms in admin controller now display combo boxes for foreign keys instead of plain text boxes, and if
      the foreign_key column is integer then the value displayed in the combo box is from the field that comes after the
      field pointed to by the foreign key column. So if you have a foreign key product_id referring to a products table
      with fields id and name then the drop down displays product names while the backend values are prodcut ids from the
      products table

    * If there is any relationship for a foreign key field present in the current model displays the column next to the
      referenced column from the target table. So if you have a foreign key product_id referring to a products table
      with fields id and name then product names are displayed in listings


What's new in 0.6.8
-------------------

* CRUDController now uses wtdojo to display fields using dojo.
  

What's new in 0.6.6
-------------------

* Minor improvement in the authentication framework. Instead of fetching user permissions from the DB for each url request; user
  permissions are fetched only once during login time and stored in session. The auth.authenticator tween just used the list of
  user permissions present in session instead of fetching them each time.


What's new in 0.6.5
------------------

* dojo_model_forms support


What's new in 0.6.4
-------------------

* Added facility in the authentication framework for static permissions. You can use the authentication manager to give set a permission
  for a route but you don't have to assign any user to that permission. This is meant to allow authentication from user databases other
  than PyCK's users table. Developers just need to set the permission name in a request.session key named **auth_static_permission** in
  their login verification controllers. This way the users can be authenticated any way the developer wants and still their access
  to the whole application can be controlled by PyCK's authentication manager.


What's new in 0.6.3
-------------------

* Fixed minor issue with the populate script that prevented proper population of posgresql and possibly mysql databases.
  This does not seem to happen with SQLite.


What's new in 0.6
----------------

* Added support for authentication framework. PyCK now supports a graphical web based section for creating users,
  permissions and assigning them to different routes. A default login and logout route is now also present in the
  initial scaffold.
  
  Simply create a new project, run the populate script for the project and then go to::
  
    http://0.0.0.0:6543/auth
  
  to access the authentication manager.

* Minor changes to code for making it cleaner and more compliant to PEP guidelines

* Renamed controllers/views.py to controllers/controllers.py since views.py was confusing in the MVC context
  

What's new in 0.5.1
-------------------

* Update to CRUDController allowing displaying of related data from another table of a foreign key field. The *add_edit_field_args*
  property can now take values *choices* and *choices_fields* and the *list_field_args* property takes a key *display_field*, for example::
  
    class ProductCRUDController(CRUDController):
        model = Product
        db_session = DBSession
        add_edit_field_args = {
             'category_id': {'label': 'Category', 'widget': Select(), 'coerce': int,
                             'choices_fields': [Category.id, Category.name] }
             #'category_id': {'widget': Select(), 'coerce': int, 'choices': [(1, 'ABC'), (2, 'DEF')] }
            }
    
        list_field_args = {
                'category_id': {'display_field': 'category.name'}
                    }


What's new in 0.5
----------------

* Automatic Admin Interface - Enables automatic Admin interface generation from database models. The :class:`pyck.ext.admin_controller.AdminController` allows you to quickly enable Admin interface for any number of database models you like. To use AdminController at minimum these steps must be followed.
    
    
    1. In your application's routes settings, specify the url where the Admin interface should be displayed. You can use the :func:`pyck.ext.admin_controller.add_admin_handler` function for it. For example in your __init__.py; put code like::
    
        from pyck.ext import AdminController, add_admin_handler
        from pyck.lib import get_models
        # Place this with the config.add_route calls
        add_admin_handler(config, db_session, get_models(myapplicationpackagenamehere), 'admin', '/admin', AdminController)
    
    and that's all you need to do to get a fully operation Admin interface.
    
What's new in 0.4.3
------------------

* Updates to the CRUDController for better template integration

What's new in 0.4.2
------------------

* Pagination fixes for limiting the number of pages displayed

What's new in 0.4.1
------------------

* Fixed edit interface bug in CRUDController
* Added instructions for setting up pyck with Apache+mod_wsgi 

What's new in 0.4
----------------

* CRUDController - Enables automatic CRUD interface generation from database models. The :class:`pyck.controllers.CRUDController` allows you to quickly enable CRUD interface for any database model you like. To use CRUD controller at minimum these steps must be followed.
    
    1. Create a sub-class of the CRUDController and set model (for which you want to have CRUD) and database session::
    
        from pyck.controllers import CRUDController
        from myapp.models import MyModel, DBSession
        
        class MyCRUDController(CRUDController):
            model = MyModel
            db_session = DBSession()
    
    2. In your application's routes settings, specify the url where the CRUD interface should be displayed. You can use the :func:`pyck.controllers.add_crud_handler` method for it. For example in your __init__.py (if you're enabling CRUD for a model without your main project) or in your routes.py (if you're enabling CRUD for a model within an app in your project) put code like::
    
        from pyck.controllers import add_crud_handler
        from controllers.views import MyCRUDController
        
        # Place this with the config.add_route calls
        add_crud_handler(config, 'mymodel_crud', '/mymodel', MyCRUDController)
    
    and that's all you need to do to get a fully operation CRUD interface. Take a look at the newapp sample app in demos for a working CRUD example in the Wiki app.


What's new in 0.3
----------------

* Model Forms - Ability to generate forms automatically from database models. We now have a :func:`pyck.forms.model_form` function that behaves exactly like :func:`wtforms.ext.sqlalchemy.orm.model_form` but uses :class:`pyck.forms.Form` as its base class. The benefit is that you get all the features present in pyck forms in your model form (like, as_p and as_table rendering of your form and CSRF protection). Using a model form is quite easy, for example::

    from pyck.forms import model_form
    from myapp.models import User
    UserForm = model_form(User)

  Of course, you can then sub-class this UserForm class to add further validators or modifications if you like. Later in a view (considering you've not subclassed UserForm) you can use this form as::
  
    f = UserForm(request.POST, request_obj=request, use_csrf_protection=True)
  
  and it will work exactly like a normal pyck Form.

* A more operational blog app in the newapp given in demos that uses the model_form feature to add blog posts.

What's new in 0.2.4
------------------

* Automated CSRF Protection in forms. While disabled by default (to maintain compatibility with WTForms), CSRF protection can be enabled for a form by passing the form two extra keyword arguments **request_obj** and **use_csrf_protection** set to **True** when initializing it. For example::

    f = ContactForm(request.POST, request_obj=request, use_csrf_protection=True)

* Form objects now have an as_table :func:`pyck.forms.Form.as_table` method that allows displaying the form in a table similar to the :func:`pyck.forms.Form.as_p` method added in previous release. This method also accepts labels and errors positions (left, right, top, bottom) and optionally allows you to insert the html <table> tag within the method instead of putting it in your template by setting **include_table_tag parameter** to **True**

What's new in 0.2.3
------------------

Till now almost all updates were to the scaffold generated by a PyCK project, so in a sense till now PyCK could be considered another scraffold for Pyramid. With this version, things are starting to change a bit.

* A new package :mod:`pyck.forms` that serves as a wrapper on top of WTForms (will try to maintain code usage compatibility with wtforms) so instead of using normal **wtforms.Form** class instances, PyCK developers can use :class:`pyck.forms.Form` instances in the same way. But these forms come with some additional features

    * Currently the form can be display using html p tags using :func:`pyck.forms.Form.as_p` method. This method supports displaying labels and validation errors on either direction of the field control (top, bottom, left, right).
    
    * The associated sample app code has been updated along with new app scaffold to use pyck.forms, the code already has become much simpler.
    
    * It is important to note that these forms can be used in the same way as WTForms so if you want to layout your form the way you want (as you normally do in WTForms); you are still able to do it.

* Basic tests have been implemented for :mod:`pyck.forms` and nosetests are being used for automated testing. Keeping the code quality high is one of the aims here so I'll try to write tests for all of the additions to pyck itself.



What's new in 0.2.2
------------------

* Sessions support - Sessions come pre-configured now with a new PyCK project and the sample included has also been updated accordingly

* Forms support - Initial support for forms using WTForms has landed. Keeping with the structure forms are defined within a forms package inside the application package.

* A newly created project (and the sample project) now contains a contact form demonstrating forms usage.

    * Additionally forms also have CSRF (Cross Site Request Forgery) protection

* Flash messaging support is also in. Look at the contact form example (specifically its template and the home and base templates) to see flash messages in action.

**What's next?** Focus now is to make forms more easy to use within PyCK. Upcoming versions are expected to contain more enhancements related to forms.


What's new in 0.2.1
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

What's new in 0.2.0
------------------

* tables created from models in apps are automatically prefixed by app name. For example: if you have an app named blog and it has a model Post where you have specified::

    __tablename__ = 'posts'

  it will automatically be created as **blog_posts** in the database. Your access to the table through the model remained same without any changes.

* Once you run python setup.py develop for your new project, a new command for creating an app becomes availabe to you. Instead of copying the sample app provided and adjusting it, now the whole struture is created for you. For details see

  :ref:`adding-apps`

  This feature is the reason that the version number bumped upto 0.2 :-)


What's new in 0.1.6
------------------

* First fully operational version with pluggable apps along with their database models etc.

