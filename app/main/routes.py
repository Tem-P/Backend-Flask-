from flask_cors import cross_origin
from .api.home import Home
from .api.conf import Config
from .api.upload import VideoUploader
from .api.status import status,Status

from . import config


def create_routes(app,api):
    api.decorators = [cross_origin(origin='*', headers=['accept', 'Content-Type'])]
    api.add_resource(Home, '/api/v1/')
    api.add_resource(Config, '/api/v1/conf')
    api.add_resource(VideoUploader, '/api/v1/upload')
    #api.add_resource(Status, '/api//v1/status')
    
    socketio = config.socketio
    status = Status(socketio)
    socketio.on_event('connect', status.connected, namespace='/api/v1/status')
    socketio.on_event('get_status', status.get_status, namespace='/api/v1/status')
    #socketio.on_event('message', s.handle_message, namespace='/api/v1/status')

    
    
