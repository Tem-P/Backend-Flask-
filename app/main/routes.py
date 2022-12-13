from flask_cors import cross_origin
from .api.home import Home
from .api.conf import Config
from .api.upload import VideoUploader



def create_routes(app,api):
    api.decorators = [cross_origin(origin='*', headers=['accept', 'Content-Type'])]
    api.add_resource(Home, '/')
    api.add_resource(Config, '/conf')
    api.add_resource(VideoUploader, '/upload')