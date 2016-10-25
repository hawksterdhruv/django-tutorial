.. django-tutorial documentation master file, created by
   sphinx-quickstart on Fri Oct 21 12:02:31 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to django-tutorial's documentation!
===========================================



Django Installation
-------------------

The installation is really simple::

 $ pip install django

Creating the first project
--------------------------

Create a boiler plate project
+++++++++++++++++++++++++++++

::

 $ django-admin startproject <project-name>

| Take a look at the files that have been created.
| This is the folder project file structure

::

 <project-name>
	|-- manage.py
	`-- <project-name>
	    |-- __init__.py
	    |-- settings.py
	    |-- urls.py
	    `-- wsgi.py

Running the project
+++++++++++++++++++

| Before we start we need to migrate our apps.
| To do this run the following command

::

 $ python manage.py migrate 

We can now start the devlopment server.

::

 $ python manage.py runserver

You should see the following output

::

 Performing system checks...
 
 0 errors found June 12, 2016 - 08:48:58 Django version 1.8.13, using settings '<project-name>.settings'
 Starting development server at http://127.0.0.1:8000/
 Quit the server with CTRL-BREAK.

You can now go to localhost:8000 in your browser.
you should see the following image.



