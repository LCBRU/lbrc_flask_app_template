# LBRC Flask App Template
This is a template for Flask applications using the NIHR Leicester Beoimedical Research Centre
theme and standard toolset.
## Cookie Cutter
This template uses cookie cutter to create the project.  See the documentation for further [details](https://cookiecutter.readthedocs.io/en/stable/index.html) about cookiecutter.
### Install Cookie Cooker
To install cookie cutter run the command:
```bash
pip3 install --user cookiecutter
```
## Generate Project from Template
There are two ways to create a project from this template.
### Download This Repository
Down this repository using the command:
```bash
gh repo clone LCBRU/lbrc_flask_app_template
```
or
```bash
git clone https://github.com/LCBRU/lbrc_flask_app_template.git
```
Then run the command:
```bash
cookiecutter lbrc_flask_app_template/
```
### Create Project from GitHub
```bash
cookiecutter gh:LCBRU/lbrc_flask_app_template
```
or
```bash
cookiecutter https://github.com/LCBRU/lbrc_flask_app_template.git
```
## Project Prerequisites
The project is dependent upon LDAP.  This is installed differently depending on the operating system.
### Linux
Run the following commands:
```bash
sudo apt-get install libldap2-dev
sudo apt-get install libsasl2-dev
```
### Windows
After the virtual environment has been created and activated in step 4 (below), run the following steps:
1. Download the appropriate wheel file from the releases page of the [https://github.com/cgohlke/python-ldap-build] repository into the project directory
2. Install the wheel file using the command `pip install python_ldap...whl`, using the name of the file downloaded.
## Setting up the new Project
1. Change directory into the project directory
2. Create a python virtual environment using the command `python3 -m venv .venv`
3. Activate the python virtual environment using the command `. .venv/bin/activate`
4. Upgrade *pip*: `pip install --upgrade pip`
5. Install *pip-tools*: `pip install pip-tools`
6. Create a requirements file from `requirements.in` by running the command: `pip-compile`
7. Install the requirements using the command: `pip install -r requirements.txt`
8. Create a blank database using the details entered into cookie cutter
9. Create test data by running `python create_test_db.py`
10. Run the application: `python app.py`
## Structure of the Created Project
### Libraries
The application uses a variety of libraries.  The main ones are listed here or in the sections below:
- [Flask](https://flask.palletsprojects.com) - web framework
- [SqlAlchemy](https://www.sqlalchemy.org) - database query and ORM tool
- [LBRC Flask](https://github.com/LCBRU/lbrc_flask) - helper library written by LBRC staff, containing helpers, utilities, templates and themes for Leicester BRC applications
- [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) - templating engine
- [HTMX](https://htmx.org/) - HTML extensions for more interactive pages
### Top Level Directory
The top level directory of the project contains files to run, configure, manage and help develop the application.

It also contains files for working with asynchronous tasks using [Celery](https://docs.celeryq.dev/en/stable/getting-started/introduction.html).

The application is run using the command `python app.py`
### Alembic Directory
This contains the database migration files that are run using the [Alembic](https://alembic.sqlalchemy.org/en/latest/) tool.
### Project Source Directory
This directory is named the same as the project directory itself.  It contains the python files to initialise and configure
the application, and also `admin.py` that congigures the admin maintenance screens that use the [Flask Admin Tool](https://flask-admin.readthedocs.io/en/latest/).

This folder will also contain subfolders to hold different modules of the application.  The default application has folders for the
program's model classes and the UI [Flask Blueprint](https://flask.palletsprojects.com/en/3.0.x/blueprints/).

Other folders may contain code for application services, APIs or other modules.

The Flask application is created and defined in the `__init__.py` file.
### UI
This folder contains the application views in the `views` folder and templates in the `templates\ui` folder.  The blueprint is setup in the `__init__.py` file.  See the [Flask Documentation](https://flask.palletsprojects.com) for information on views and templates.