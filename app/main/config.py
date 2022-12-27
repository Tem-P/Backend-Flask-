import os

# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

basedir = os.path.abspath(os.path.dirname('.'))

app = None
socketio = None
mongo = None
bcrypt = None

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'n0t_s0_secret')
    JWT_ALGO = 'HS256'
    DEBUG = False
    UPLOAD_FOLDER = os.path.join(basedir, 'uploads')
    PROC_FOLDER = os.path.join(basedir, 'processed')
    MONGO_URI = "mongodb://localhost:27017/backendDB"
    MAX_CONTENT_LENGTH = 100 * 1024 * 1024

class DevelopmentConfig(Config):
    DEBUG = True
    

class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    

class ProductionConfig(Config):
    DEBUG = False

config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY