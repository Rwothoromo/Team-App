"""
It is good practice to specify configurations for different environments.
We have specifed configurations for development,
which we will use while building the app and running it locally
 as well as production, which we will use when the app is deployed.
"""

class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments

class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True
    # Allowing SQLAlchemy to log errors
    # TESTING = True activates the testing mode of Flask extensions.


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
