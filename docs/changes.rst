.. _changes:

Changes
============

This document lists the changes as versions progress

Whats new in 0.5.1
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


Whats new in 0.5
----------------

* Automatic Admin Interface - Enables automatic Admin interface generation from database models. The :class:`pyck.ext.admin_controller.AdminController` allows you to quickly enable Admin interface for any number of database models you like. To use AdminController at minimum these steps must be followed.
    
    
    1. In your application's routes settings, specify the url where the Admin interface should be displayed. You can use the :func:`pyck.ext.admin_controller.add_admin_handler` function for it. For example in your __init__.py; put code like::
    
        from pyck.ext import AdminController, add_admin_handler
        from pyck.lib import get_models
        # Place this with the config.add_route calls
        add_admin_handler(config, db_session, get_models(myapplicationpackagenamehere), 'admin', '/admin', AdminController)
    
    and that's all you need to do to get a fully operation Admin interface.
    
Whats new in 0.4.3
------------------

* Updates to the CRUDController for better template integration

Whats new in 0.4.2
------------------

* Pagination fixes for limiting the number of pages displayed

Whats new in 0.4.1
------------------

* Fixed edit interface bug in CRUDController
* Added instructions for setting up pyck with Apache+mod_wsgi 

Whats new in 0.4
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


Whats new in 0.3
----------------

* Model Forms - Ability to generate forms automatically from database models. We now have a :func:`pyck.forms.model_form` function that behaves exactly like :func:`wtforms.ext.sqlalchemy.orm.model_form` but uses :class:`pyck.forms.Form` as its base class. The benefit is that you get all the features present in pyck forms in your model form (like, as_p and as_table rendering of your form and CSRF protection). Using a model form is quite easy, for example::

    from pyck.forms import model_form
    from myapp.models import User
    UserForm = model_form(User)

  Of course, you can then sub-class this UserForm class to add further validators or modifications if you like. Later in a view (considering you've not subclassed UserForm) you can use this form as::
  
    f = UserForm(request.POST, request_obj=request, use_csrf_protection=True)
  
  and it will work exactly like a normal pyck Form.

* A more operational blog app in the newapp given in demos that uses the model_form feature to add blog posts.

Whats new in 0.2.4
------------------

* Automated CSRF Protection in forms. While disabled by default (to maintain compatibility with WTForms), CSRF protection can be enabled for a form by passing the form two extra keyword arguments **request_obj** and **use_csrf_protection** set to **True** when initializing it. For example::

    f = ContactForm(request.POST, request_obj=request, use_csrf_protection=True)

* Form objects now have an as_table :func:`pyck.forms.Form.as_table` method that allows displaying the form in a table similar to the :func:`pyck.forms.Form.as_p` method added in previous release. This method also accepts labels and errors positions (left, right, top, bottom) and optionally allows you to insert the html <table> tag within the method instead of putting it in your template by setting **include_table_tag parameter** to **True**

Whats new in 0.2.3
------------------

Till now almost all updates were to the scaffold generated by a PyCK project, so in a sense till now PyCK could be considered another scraffold for Pyramid. With this version, things are starting to change a bit.

* A new package :mod:`pyck.forms` that serves as a wrapper on top of WTForms (will try to maintain code usage compatibility with wtforms) so instead of using normal **wtforms.Form** class instances, PyCK developers can use :class:`pyck.forms.Form` instances in the same way. But these forms come with some additional features

    * Currently the form can be display using html p tags using :func:`pyck.forms.Form.as_p` method. This method supports displaying labels and validation errors on either direction of the field control (top, bottom, left, right).
    
    * The associated sample app code has been updated along with new app scaffold to use pyck.forms, the code already has become much simpler.
    
    * It is important to note that these forms can be used in the same way as WTForms so if you want to layout your form the way you want (as you normally do in WTForms); you are still able to do it.

* Basic tests have been implemented for :mod:`pyck.forms` and nosetests are being used for automated testing. Keeping the code quality high is one of the aims here so I'll try to write tests for all of the additions to pyck itself.



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

