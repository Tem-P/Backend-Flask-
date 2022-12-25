import os
from flask import jsonify, request,redirect
from flask_restful import Resource
from werkzeug.utils import secure_filename
from flask import current_app as app
from .. import jobqueue

Job = jobqueue.Job

class VideoUploaderAPI(Resource):
    'route: /api/v1/upload' 

    def options(self):
        pass
    
    def post(self):
        # set config = conf
        #app.logger.info(request.headers)
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            app.logger.info('No selected file')
            return redirect(request.url)
        else:
            filename = secure_filename(file.filename)
            filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            a,b = 1,10
            i = 2
            from random import randint
            if os.path.exists(filename):
                filename,ext = os.path.splitext(filename)
                while os.path.exists(filename+'_{}'.format(i)+ext):
                    a,b = b,b*10
                    i = randint(a,b)
                filename = filename+'_{}'.format(i)+ext
                
            file.save(filename)
            job = Job(filename)
            'TODO : create a Job object from jobqueue.py'
            if jobqueue.jobqueue:
                jobqueue.jobqueue.add(job)
            return jsonify({'id':job.id})
            #print('upload_video filename: ' + filename)
            #return jsonify({'status':'uploaded {}'.format(filename)})
