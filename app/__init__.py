"""
We've created a function, create_app that, given a configuration name,
loads the correct configuration from the config.py file,
as well as the configurations from the instance/config.py file.
We have also created a db object which we will use to interact with the database.
"""

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()
login_manager = LoginManager()

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    # temporary route
    # @app.route('/')
    # def hello_world():
    #     return 'Hello, World!'

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"

    migrate = Migrate(app, db)
    # We have created a migrate object which will allow us to run migrations using Flask-Migrate

    from app import models

    return app
