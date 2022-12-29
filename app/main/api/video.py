import os
from flask import jsonify, request,redirect,send_file
from flask_restful import Resource
from werkzeug.utils import secure_filename
from flask import current_app as app
from ..model.processedjob import ProcessedJob
from ..model.user import is_authenticated


class VideoServeAPI(Resource):
    'route: /api/v1/download/<id>' 

    @is_authenticated
    def get(self,user,id):
        "take id=output video id "
        "extract path from database for that id"
        from bson.objectid import ObjectId
        pjob  = ProcessedJob.get({'_id':ObjectId(id)})
        print(pjob)
        if not pjob:
            return {'error':'Not Found'},404
        pjob = pjob[0]
        if user.username != pjob.username:
            return {'error':'Access Denied'},401
        "redirect to video file"
        print(pjob.outfile)
        directory,name = os.path.split(pjob.outfile)
        return send_file(pjob.outfile,download_name=name)