import os
from flask import jsonify, request,redirect
from flask_restful import Resource
from werkzeug.utils import secure_filename
from flask import current_app as app


class VideoServeAPI(Resource):
    'route: /api/v1/download' 

    def get(self,id):
        "take id=output video id "
        "extract path from database for that id"
        "redirect to video file"
        "return"