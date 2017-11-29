# Team-App - phase one
Flask Team-App with CRUD implementation
(Based on https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-one)

**Technologies**
* Python 3.6

**Requirements**
* Install [Python 3.6](https://www.python.org/downloads/)
* Run `pip install virtualenv` on command prompt
* Run `pip install virtualenvwrapper-win` on command prompt

**Setup**
* Open command prompt and change directory to your select directory e.g. cd c:
* Run mkvirtualenv venv
* Run workon venv
* Run `git clone` this repository and `cd` into the project root.
* Run `pip install -r requirements.txt` on command prompt
* Create the file `'instance\config.py'`
* Inside `'instance\config.py'`, create variables;
    - SECRET_KEY = 'some value'
    - SQLALCHEMY_DATABASE_URI = 'mysql://db_admin_name:db_admin_password@localhost/db_name'
* Run `set FLASK_CONFIG=production` on command prompt
* Run `set FLASK_APP=run.py` on command prompt
* Run `flask db init` on command prompt
* Run `flask db migrate` on command prompt
* Run `flask db upgrade` on command prompt
* Run `flask run` on command prompt
* View the app on `http://127.0.0.1:5000/`
* Fully setup!
