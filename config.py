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
    
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Put any configurations here that are common across all environments


class DevelopmentConfig(Config):
    """
    Development configurations
    """

    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


class TestingConfig(Config):
    """
    Testing configurations
    """

    SECRET_KEY = 'some value'
    TESTING = True


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
