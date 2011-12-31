.. _changes:

Changes
============

This document lists the changes as versions progress

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

