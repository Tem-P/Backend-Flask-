import os
from flask import jsonify, request,redirect
from flask_restful import Resource
from werkzeug.utils import secure_filename
from flask import current_app as app
from .. import config
from ..model.user import is_authenticated
from ..model.processedjob import ProcessedJob
from .. import jobqueue

Job = jobqueue.Job

class VideoUploaderAPI(Resource):
    'route: /api/v1/upload' 

    def options(self):
        pass
    
    @is_authenticated
    def post(self,user):
        # user comes from is_authenticated wrapper

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
            from random import randint
            if os.path.exists(filename):
                filename,ext = os.path.splitext(filename)
                i = randint(a,b)
                while os.path.exists(filename+'_{}'.format(i)+ext):
                    i = randint(a,b)
                    a = b
                    b = b*10
                filename = filename+'_{}'.format(i)+ext
            file.save(filename)

            job = Job(user.username,filename)
            
            pjob = ProcessedJob()
            pjob.infile = job.pathin
            pjob.outfile = job.pathout
            pjob.username = job.username
            pjob.save()
            
            pjob = ProcessedJob.get({'infile':job.pathin})[0]
            job.id = str(pjob._id)

            'TODO : create a Job object from jobqueue.py'
            if jobqueue.jobqueue:
                jobqueue.jobqueue.add(job)
                jobqueue.jobqueue.jobs_in_proc[job.id]=job
            return jsonify({'id':job.id})
