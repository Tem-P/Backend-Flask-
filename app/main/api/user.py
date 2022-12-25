import os
from flask import jsonify, request,redirect
from flask_restful import Resource
from werkzeug.utils import secure_filename
from flask import current_app as app
from ..model.user import User

class UserLoginAPI(Resource):
    'route: /api/v1/user/login'
    
    def get(self):
        'login'
        return jsonify({'get':'request','sent':'here'})

    def post(self):
        'login'
        return jsonify({'user':'abc','password':'xyz'})

class UserRegisterAPI(Resource):
    'route: /api/v1/user/register'
    
    def post(self):
        'register'
        return jsonify({'user':'abc','password':'xyz'})
