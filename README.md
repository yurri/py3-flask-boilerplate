py3-flask-boilerplate
=====================

A "skeleton" of a Python 3 Flask/SQLAlchemy application to be re-used when starting new quick projects

Defines project structure, controller, templates, user data model and user authentication.

DEPENDENCIES

This project uses SQLAlchemy ORM which in its current version (0.8.2) is not compatible with Python 3 (this is going to change in version 0.9 currently under development). If you install SQLAlchemy via setuptools (e.g. easy_install or pip) it will be installed as Python 2 code while you won't get any errors. To initiate automatic conversion into Python 3 code, install it from source (https://pypi.python.org/packages/source/S/SQLAlchemy/SQLAlchemy-0.8.2.tar.gz) by running "setup.py install"

This and other project depencies are listed in requirements.txt


Loosely based on https://github.com/mitsuhiko/flask/wiki/Large-app-how-to
