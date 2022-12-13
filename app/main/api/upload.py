import os
from flask import jsonify, request,redirect
from flask_restful import Resource
from werkzeug.utils import secure_filename
from flask import current_app as app

class VideoUploader(Resource):
    'route: /upload' 

    def options(self):
        pass
    
    def post(self):
        # set config = conf
        #app.logger.info('No selected file')
        #app.logger.info(request.data)
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
            #print('upload_video filename: ' + filename)
            #return jsonify({'status':'uploaded {}'.format(filename)})
