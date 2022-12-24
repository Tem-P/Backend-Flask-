import os

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname('.'))

app = None
socketio = None

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'n0t_s0_secret')
    DEBUG = False
    UPLOAD_FOLDER = os.path.join(basedir, 'uploads')
    MAX_CONTENT_LENGTH = 100 * 1024 * 1024


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_main.db')
    #SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_test.db')
    #PRESERVE_CONTEXT_ON_EXCEPTION = False
    #SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY