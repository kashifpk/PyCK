.. _installation:

Installation
============

Installing **PyCK** is as easy as installing any other python package using either **easy_install** or **pip**. It is a good idea to setup pyck inside a virtual environment. Here is how:

1. (optional) Install pip if you don't already have it::

    sudo easy_install pip

2. Install virtualenv if you don't have it already::

    sudo pip install virtualenv

3. Create a virtual environment for your PyCK applications::

    virtualenv --no-site-packages pyckenv

4. Activate your new virtual environment::

    source pyckenv/bin/activate

   Anytime you want to deactivate the environment just issue the command **deactivate**

5. Install pyck::

    pip install pyck

   This is the only step you actually need to do, if you already have easy_install or pip, installing pyck is as easy as **easy_install pyck** or **pip install pyck**, however using a virtual environment sandboxes the rest of the system nicely for  you.

