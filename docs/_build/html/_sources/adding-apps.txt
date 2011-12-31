.. _adding-apps:

Adding an Application
=====================

Once you run python setup.py develop for your new project, a new command for creating an app becomes availabe to you. Instead of copying the sample app provided and adjusting it, now the whole struture is created for you. Lets assume you have named your project **myproject**. After running::

    python setup.py develop
    
You will be able to use a new command named **myproject_newapp**. This command takes just one argument - the name of the new app and automatically creates all its structure under the apps folder. You still need to enable it by adding it to the **enabled_apps** list in **apps/__init__.py**. ::

    myproject_newapp blog

The structure created for you is ready to use as soon as you add the apps name in the enabled_apps list but you might want to create your models and add some other stuff first.

