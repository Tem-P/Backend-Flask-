from flask_cors import cross_origin
from .api.home import Home
from .api.conf import Config
from .api.upload import VideoUploader



def create_routes(app,api):
    api.decorators = [cross_origin(origin='*', headers=['accept', 'Content-Type'])]
    api.add_resource(Home, '/api/v1/')
    api.add_resource(Config, '/api/v1/conf')
    api.add_resource(VideoUploader, '/api/v1/upload')
