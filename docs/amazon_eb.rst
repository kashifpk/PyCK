.. _amazon_eb:

Deploying to Amazon Elastic Beanstalk
=====================================



Assuming you have followed the :ref:`installation` section and created a virtualenv named pyckenv,
we'll now setup Nginx to use this virtualenv alongwith uwsgi for deploying our pyck applications.
Nginx is quite lightweight compared to apache and uwsgi offer far greater performance compared to mod_wsgi.
This document describes the most basic setup. A more high performance setup suitable for high-load sites might
include supervisord and also we may need https support. Both of this are covered in a separate document.

1. Make sure you have installed nginx and uwsgi. uwsgi can be installed even within your virtualenv::

    sudo apt-get install nginx
    pip install uwsgi       # within your virtualenv


2. In your project's development.ini or production.ini file, add a uwsgi section::
    
    
    [uwsgi]
    socket = /tmp/myapp.sock
    master = true
    processes = 5


   You can adjust the number of processes to your liking. You probably should change myapp.sock to represent
   the name of your application.
   

3. Run uswsgi::

    uwsgi --ini-paste production.ini --virtualenv /path/to/pyckenv/ --daemonize2 --

4. Make sure that the uwsgi socket is readable by nginx::

    chmod 777 /tmp/myapp.sock


4. Add a section or server for your site in nginx config. A good way to do this is to create a separate file in
   nginx's sites-available folder (normally /etc/nginx/sites-available), for example you can create a file names myapp there::

    server {
       listen 8000;
       server_name localhost;

       location / {
                include uwsgi_params;
                uwsgi_pass unix:///tmp/myapp.sock;
       }
    }

   Above is just an example, you probably would want to listen on a different port and give a different value for server_name. 

5. Enable this site by linking it to the sites-enabled folder::

    cd /etc/nginx/sites-enabled
    sudo ln -s ../sites-available/myapp .


6. Start or restart nginx::

    sudo service nginx restart


Thats all now you can test your application at: http://localhost:8000/


