# Team-App
Flask Team-App with CRUD implementation

**Technologies**
* Python 3.6

**Requirements**
* Install [Python 3.6](https://www.python.org/downloads/)
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
* Run `mysql -u root -p`
    - mysql> `CREATE USER 'db_admin_name'@'localhost' IDENTIFIED BY 'db_admin_password';`
    - mysql> `CREATE DATABASE db_name;`
    - mysql> `GRANT ALL PRIVILEGES ON db_name . * TO 'db_admin_name'@'localhost';`
    - mysql> `exit`
* Run `set FLASK_CONFIG=production` on command prompt
* Run `set FLASK_APP=run.py` on command prompt
* Run `flask db init` on command prompt
* Run `flask db migrate` on command prompt
* Run `flask db upgrade` on command prompt
* Run `flask run` on command prompt
* View the app on `http://127.0.0.1:5000/`
* Fully setup!
