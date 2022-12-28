import os
import time
from flask import jsonify, request,redirect
from flask_restful import Resource
from werkzeug.utils import secure_filename
from flask import current_app as app
from flask_socketio import emit,send

from .. import jobqueue

class StatusAPI(Resource):
    'route: /api/v1/status'
    'make socket connection with above route'
    'emit status id '
    'sends completed:True/False'
    'if completed:True also sends path to output file '

    def __init__(self,socketio):
        pass

    def connected(self):
        app.logger.info("client connected through socket")
        #emit('connected','You are connected to socket')
    
    def disconnected(self):
        app.logger.info("client disconnected!")
        #emit('connected','You are connected to socket')

    def get_status(self,id_str):
        "get status of given id in message and emit it "
        #print("get_status(self,message):",id_str)
        id = id_str
        # try:
        #     id = int(id_str)
        # except ValueError:
        #     emit('error',id_str)
        #     return
        jq = jobqueue.jobqueue
        '''
        if id not in jq.comp_dic:
            emit('status',{'completed':False})
        else:
            emit('status',{'completed':True,'path':jq.comp_dic[id].pathout})
        '''
        if id in jq.jobs_in_proc:
            job = jq.jobs_in_proc[id]
            if job.asked_status:
                app.logger.info("repeated status request from frontend")
                return
            else:
                app.logger.info("first status request from frontend")
                job.asked_status = True
        while id in jq.jobs_in_proc:
            time.sleep(0.1)
        if id not in jq.comp_dic:
            return
        emit('status',{'completed':True,'path':jq.comp_dic[id].pathout})
        emit('completed',{'completed':True,'path':jq.comp_dic[id].pathout})
        del(jq.comp_dic[id])

    def send_completed(self):
        pass

status = None