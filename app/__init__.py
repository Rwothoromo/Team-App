import os

# third-party imports
from flask import abort, Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

# local imports
from config import app_config

# db variable initialization, which we will use to interact with the database
db = SQLAlchemy()
login_manager = LoginManager()


# Given a configuration name, load the correct configuration from the config.py file,
# as well as the configurations from the instance/config.py file.
def create_app(config_name):
    if os.getenv('FLASK_CONFIG') == "production":
        app = Flask(__name__)
        app.config.update(
            SECRET_KEY=os.getenv('SECRET_KEY'),
            SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI')
        )
    else:
        # Load configurations from instance folder
        app = Flask(__name__, instance_relative_config=True)

        # Update the values from the given object
        app.config.from_object(app_config[config_name])

        # Updates the values in the config from a Python file
        # app.config.from_pyfile('config.py') # this loads 'instance/config.py'

    # set to False to avoid wasting resources
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    Bootstrap(app)

    # prep application to work with SQLAlchemy
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_message = "You must be logged in to access this page."
    login_manager.login_view = "auth.login"
    migrate = Migrate(app, db)
    # We have created a migrate object which will allow us to run migrations using Flask-Migrate

    from app import models

    # Register the blueprints on the app
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    # This means that all the views for this blueprint will be accessed in the browser with the url prefix admin

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    @app.errorhandler(403)
    def forbidden(error):
        return render_template('errors/403.html', title='Forbidden'), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html', title='Page Not Found'), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('errors/500.html', title='Server Error'), 500

    return app
