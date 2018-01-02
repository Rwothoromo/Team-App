[![Build Status](https://travis-ci.org/Rwothoromo/Team-App.svg?branch=master)](https://travis-ci.org/Rwothoromo/Team-App)

# Team-App
Flask Team-App with CRUD implementation

**Technologies**
* Python 3.6 or 2.7

**Requirements**
* Install [Python](https://www.python.org/downloads/)
* Run `pip install virtualenv` on command prompt
* Run `pip install virtualenvwrapper-win` on command prompt
* Run `set WORKON_HOME=%USERPROFILES%\Envs` on command prompt

**Setup**
* Run `git clone` this repository and `cd` into the project root.
* Run `mkvirtualenv venv` on command prompt
* Run `workon venv` on command prompt
* Run `pip install -r requirements.txt` on command prompt
* Create the file `'instance\config.py'`
* Inside `'instance\config.py'`, create variables;
    - SECRET_KEY = 'some value'
    - SQLALCHEMY_DATABASE_URI = 'mysql://db_admin_name:db_admin_password@localhost/db_name'
* Run `mysql -u root -p` and enter your root password
    - mysql> `CREATE USER 'db_admin_name'@'localhost' IDENTIFIED BY 'db_admin_password';`
    - mysql> `CREATE DATABASE db_name;`
    - mysql> `GRANT ALL PRIVILEGES ON db_name . * TO 'db_admin_name'@'localhost';`
    - mysql> `CREATE DATABASE db_test;`
    - mysql> `GRANT ALL PRIVILEGES ON db_test . * TO 'db_admin_name'@'localhost';`
    - mysql> `exit`
* Run `set FLASK_CONFIG=development` on command prompt
* Run `set FLASK_APP=run.py` on command prompt
* Run `flask db init` on command prompt
* Run `flask db migrate` on command prompt
* Run `flask db upgrade` on command prompt
* Run `flask shell` on command prompt then type the following
    - `>>> from app.models import Employee`
    - `>>> from app import db`
    - `>>> admin = Employee(email="admin@admin.com", username="admin", password="admin2017", is_admin=True)`
    - `>>> employee1 = Employee(email="employee1@employee.com", username="employee1", password="employee12017", first_name="John", last_name="Doe")`
    - `>>> db.session.add(admin)`
    - `>>> db.session.add(employee1)`
    - `>>> db.session.commit()`
    - `>>> exit()`
* Run `flask run` on command prompt
* View the app on `http://127.0.0.1:5000/`
* Fully setup!

**Unittests**
* Run `set FLASK_CONFIG=testing` on command prompt
* Run `set FLASK_APP=run.py` on command prompt
* Run `pytest` on command prompt