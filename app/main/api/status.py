import os
from flask import jsonify, request,redirect
from flask_restful import Resource
from werkzeug.utils import secure_filename
from flask import current_app as app
from flask_socketio import emit,send

from .. import jobqueue

class Status(Resource):
    'route: /api/v1/status'
    'make socket connection with above route'
    'emit status id '
    'sends completed:True/False'
    'if completed:True also sends path to output file '

    def __init__(self,socketio):
        pass

    def connected(self,id_str):
        emit('connected','You are connected to socket')

    def get_status(self,id_str):
        "get status of given id in message and emit it "
        print("get_status(self,message):",id_str)
        id = 0
        try:
            id = int(id_str)
        except ValueError:
            emit('error',id_str)
            return
        jq = jobqueue.jobqueue
        if id not in jq.comp_dic:
            emit('status',{'completed':False})
        else:
            emit('status',{'completed':True,'path':jq.comp_dic[id].pathout})
            del(jq.comp_dic[id])
    def send_completed(self):
        pass

status = None