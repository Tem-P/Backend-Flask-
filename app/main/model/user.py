import jwt
from functools import wraps
from flask import request,jsonify,current_app as app

from .document import Document
from .. import config

class User(Document):
    def __init__(self):
        super().__init__('user')
    
    def get(query):
        data = config.mongo.db['user'].find(query)
        users = []
        for d in data:
            u = User()
            u.load(d)
            users.append(u)
        if len(users)==0:
            return None
        return users
    
    def __str__(self):
        return super().__str__()

# wrapper function decorator that will check if token exists and is valid
def is_authenticated(func):
    @wraps(func)
    def check_token(*args, **kwargs):
        token = request.headers.get('Authorization')
        error = False
        users = None
        if not token:
            return jsonify({'error':'token not found'})
        try:
            # if token is valid
            token = token.split(' ')[1]
            data = jwt.decode(token,app.config['SECRET_KEY'],app.config['JWT_ALGOS'])
            users = User.get({'username':data['username']})
            if not users:
                error = True
        except Exception as e:
            app.logger.error('token error: {}'.format(e))
            error = True
        if not error:
            return func(users[0],*args, **kwargs)
        return jsonify({'error':'token is invalid'})
    return check_token