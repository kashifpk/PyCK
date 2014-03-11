.. _start-project:

Starting a Project
==================

Once you have successfully installed PyCK and have optionally activated a virtaul environment, you are ready to start your first project. To start your first project, follow these steps.


1. Move to the folder where you want to create your project's base folder.

2. Create the project structure using::

    pcreate -s pyck myproject
    
   Replace myproject with the name of your project. This creates the basic structure for your project including configuration files for both development and production, adding project package and sub foldres for controllers/view, models, templates, scripts, tests etc. Your project has support for pluggable applications which can be placed in the apps folder under your project's package. The generated code already contains one app there with its basic structure ready to use. If you like, you can copy this structure to create more apps.

3. Move into your newly created project's base folder::

    cd myproject

4. Run the setup script with develop parameter to install any dependant packages if they are missing::

    python setup.py develop

5. Now you should create any database models under <yourprojectname>/models/models.py that you wish to use, once done (or even if you don't want to create any models yet), run::

    myproject_initdb development.ini

   Remember to replace myproject with the name of your project. This script automatically creates tables in the database specified in development.ini configuration file. By default a SQLite file with the same name as your project is used, you can change the **sqlalchemy.url** parameter in development.ini (or production.ini in case you're changing the backend DB for production). Remember that this populate script needs to be executed again in case you add/change your models in either your main project or in any of its sub-applications. When re-running the populate script, you may need to delete the existing records/tables from your DB for this script to execute without errors.

6. Now your application is ready to start. From now on you only need this step to start serving your application through the built-in web server provided by PyCK/Pyramid. To start serving your application run::

    pserve development.ini --reload

   You may see output similar to::

    Starting subprocess with file monitor
    Starting server in PID 8191.
    Starting HTTP server on http://0.0.0.0:6543

   Note the listening port and IP can be changed in development.ini.

7. Open your browser and type::

    http://localhost:6543
    
   and congratulations you should see the initial page saying Welcome.

From here on you can start developing your project however you like :-)
