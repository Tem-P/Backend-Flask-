from flask import jsonify, request,redirect
from flask_restful import Resource
from flask import current_app as app


class HomeAPI(Resource):
  
    def get(self):
        return jsonify({'Message': 'This is Home!'})

    def post(self):
          
        data = request.get_json()     # status code
        return jsonify({'data': data}), 201
