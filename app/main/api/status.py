import os
from flask import jsonify, request,redirect
from flask_restful import Resource
from werkzeug.utils import secure_filename
from flask import current_app as app
from flask_socketio import emit,send

from ..jobqueue import jobqueue

class Status(Resource):
    'route: /api/v1/status'

    def __init__(self,socketio):
        pass

    def connected(id_str):
        emit('connected','You are connected to socket')

    def get_status(id_str):
        "get status of given id in message and emit it "
        print("get_status(self,message):",id_str)
        id = 0
        try:
            id = int(id_str)
        except ValueError:
            emit('error',id_str)
            return
        if id not in jobqueue.comp_dic:
            emit('status',{'completed':False})
        else:
            emit('status',{'completed':True,'path':jobqueue.comp_dic[id].pathout})
            del(jobqueue.comp_dic[id])

status = None