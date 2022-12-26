import os
from flask import jsonify, request,redirect
from flask_restful import Resource
from werkzeug.utils import secure_filename
from flask_bcrypt import generate_password_hash, check_password_hash
from flask import current_app as app
from ..model.user import User
import jwt

class UsernameCheckAPI(Resource):
    'route: /api/v1/user/checkusername'

    def get(self):
        'check if username is valid'
        username = request.args.get('username')
        users = User.get({'username':username})
        return jsonify({'valid':not bool(users)})

class UserLoginAPI(Resource):
    'route: /api/v1/user/login'

    def post(self):
        'login'
        "get data from form"
        body = request.get_json()
        attributes =  ['username','password']
        for key in attributes:
            if key not in body:
                return jsonify({'error':'{} not found in request'.format(key)})
        username = body['username']
        password = body['password']
        users = User.get({'username':username})

        if not users:
            return jsonify({'error':'username or password wrong'})
        print(users[0].password,password)
        if not check_password_hash(users[0].password, password):
            # wrong password
            print("wrong password")
            return jsonify({'error':'username or password wrong'})
        
        "generate jwt token and return it"
        token = jwt.encode({'username':username},app.config['SECRET_KEY'])
        return jsonify({'jwt':token})

class UserRegisterAPI(Resource):
    'route: /api/v1/user/register'
    
    def post(self):
        'register'
        "get data from form"
        body = request.get_json()
        attributes =  ['username','email','password','cpassword']
        for key in attributes:
            if key not in body:
                return jsonify({'error':'{} not found in request'.format(key)})
        username  = body['username']
        email     = body['email']
        password  = body['password']
        cpassword = body['cpassword']
        if password!=cpassword:
            return jsonify({'error':'{} two passwords does not match'.format(key)})
        
        "check if email valid and not already exist"
        "check if username valid and not already exist"
        users = User.get({'$or':[{'username':username},{'email':email}]})
        if users:
            return jsonify({'error':'username or email already exist'})

        "hash password"
        user = User()
        user.username = username
        user.email = email
        user.password = generate_password_hash(password).decode('utf8')
        user.save()
        token = 'token'
        return {'jwt':token}

# this class will just test the jwt token
class UserTestAPI(Resource):
    'route: /api/v1/user/test'

    def get(self):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error':'token not found'})
        try:
            token = token.split(' ')[1]
            data = jwt.decode(token,app.config['SECRET_KEY'],algorithms=['HS256'])
            return jsonify({'data':data})
        except Exception as e:
            print(e)
            return jsonify({'error':'token is invalid'})

