import os
from flask import Flask, jsonify, request,redirect
from flask_restful import Resource, Api
from werkzeug.utils import secure_filename


# creating the flask app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(basedir, 'uploads')

app = Flask(__name__)
app.secret_key = "jtdyqokvnalw51g3s1d3654g6df45g1d3"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024


# creating an API object
api = Api(app)

class Home(Resource):
  
    def get(self):
        return jsonify({'message': 'Welcome!'})

    def post(self):
          
        data = request.get_json()     # status code
        return jsonify({'data': data}), 201
  
  
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
  

class VideoUploader(Resource):
    'route: /upload'
    def get(self):

        return jsonify({'error':'Not Accessible!'})
    def post(self):
        # set config = conf
        #
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
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
            return jsonify({'status':'uploaded {}'.format(filename)})

# adding the defined resources along with their corresponding urls
api.add_resource(Home, '/')
api.add_resource(Config, '/conf')
api.add_resource(VideoUploader, '/upload')
  
  
# driver function
if __name__ == '__main__':
    app.run(debug = True)
    #app.run(debug = False)