from flask import Flask, jsonify, request
from flask_restful import Resource, Api
  
# creating the flask app
app = Flask(__name__)

# creating an API object
api = Api(app)
  
class Hello(Resource):
  
    def get(self):
  
        return jsonify({'message': 'hello world'})
    
    
    def post(self):
          
        data = request.get_json()     # status code
        return jsonify({'data': data}), 201
  
  
# set config
class Config(Resource):
    
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
    
    def get(self):

        return jsonify({'error':'Not Accessible!'})
    def post(self,video):
        # set config = conf
        return jsonify({'status':'uploaded'})

# adding the defined resources along with their corresponding urls
api.add_resource(Hello, '/')
api.add_resource(Config, '/conf')
api.add_resource(VideoUploader, '/upload')
  
  
# driver function
if __name__ == '__main__':
    app.run(debug = True)
    #app.run(debug = False)