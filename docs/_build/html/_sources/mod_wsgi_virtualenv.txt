.. _mod_wsgi_virtualenv:

Running PyCK Applications with Apache Mod WSGI and Virtualenv
=============================================================

Assuming you have followed the :ref:`installtion` section and created a virtualenv named pyckenv, we'll now setup Apache to use this virtualenv alongwith mod_wsgi for deploying our pyck applications. You should already have installed mod_wsgi for Apache.

1. Edit Apache's mod_wsgi configuration file normally present under */etc/apache2/mods-available/wsgi.conf* and place these two lines in it::
    
    
    WSGIPythonHome /var/pyck/pyckenv
    WSGIPythonEggs /var/pyck/eggs_cache
    
   Remember to put them inside the *<IfModule mod_wsgi.c>* section and adjust the path to point to your virtualenv for pyck

2. Create the eggs_cache folder and make give it full read/write/execute permissions::

    mkdir /var/pyck/eggs_cache
    chmod 777 /var/pyck/eggs_cache

3. Restart Apache::

    sudo apache2ctl restart


4. Create your application (assuming its under /var/www)::

    pcreate -t pyck wsgi_test

5. Make it ready for deployment::

    cd wsgi_test
    python setup.py develop
    python setup.py install
    populate_wsgi_test

6. Create the wsgi file for use with mod_wsgi, lets name it **myapp.wsgi**::

    from pyramid.paster import get_app
    import os

    here = os.path.dirname(__file__)
    application = get_app(here + '/development.ini', 'main')
    #application = get_app(here + '/production.ini', 'main')  #for production

7. Make the myapp.wsgi file executable::

    chmod 755 myapp.wsgi

8. Create *.htaccess* file in your application folder and put the following contents in it::

    Options ExecCGI FollowSymLinks
    
    DirectoryIndex myapp.wsgi
    RewriteEngine on
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule ^(.*)$ myapp.wsgi/$1  [L]
    
    AddHandler cgi-script .cgi
    AddHandler wsgi-script .wsgi
    
    Order allow,deny
    Allow from all


Thats all now you can test your application at: http://localhost/wsgi_test/
 

