from flask import jsonify, request,redirect
from flask_restful import Resource
from flask import current_app as app

# set config
class Config(Resource):
    'route: /config'
    def get(self):
        conf = {
            'conf1':1,
            'conf2':10,
            'conf3':0,
            'conf4':'Y',
            'conf5':1,
        }

        return jsonify(conf)
    
    def post(self,conf):
        # set config = conf
        return jsonify(conf)
  