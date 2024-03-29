# libraries
import os
from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS
from flask_restful import Api
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt

# custom modules
from . import config
from .routes import create_routes



def create_app(config_name):
    if not os.path.exists('uploads'):
        os.mkdir('uploads')
    if not os.path.exists('processed'):
        os.mkdir('processed')
    
    app = Flask(__name__)
    app.config.from_object(config.config_by_name[config_name])
    
    config.mongo = PyMongo(app)
    socketio = SocketIO(app,cors_allowed_origins='*')
    config.socketio = socketio
    CORS(app)
    api = Api(app)
    config.bcrypt = Bcrypt(app)
    create_routes(app,api)

    return app