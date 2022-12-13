import os
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from .routes import create_routes

#from flask_sqlalchemy import SQLAlchemy
#from flask_bcrypt import Bcrypt

from .config import config_by_name

#db = SQLAlchemy()
#flask_bcrypt = Bcrypt()


def create_app(config_name):
    if not os.path.exists('uploads'):
        os.mkdir('uploads')
    app = Flask(__name__)
    config.app = app
    CORS(app)
    api = Api(app)
    create_routes(app,api)

    app.config.from_object(config_by_name[config_name])
    #db.init_app(app)
    #flask_bcrypt.init_app(app)

    return app