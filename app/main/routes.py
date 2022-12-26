from flask_cors import cross_origin
from .api.home import HomeAPI
from .api.conf import ConfigAPI
from .api.upload import VideoUploaderAPI
from .api.status import StatusAPI
from .api.user import UserLoginAPI,UserRegisterAPI

from . import config


def create_routes(app,api):
    api.decorators = [cross_origin(origin='*', headers=['accept', 'Content-Type'])]
    api.add_resource(HomeAPI,          '/api/v1/')
    api.add_resource(ConfigAPI,        '/api/v1/conf')
    api.add_resource(VideoUploaderAPI, '/api/v1/upload')
    api.add_resource(UserLoginAPI,     '/api/v1/user/login')
    api.add_resource(UserRegisterAPI,  '/api/v1/user/register')
    # route '/api/v1/user'
    # used for login (get) and register (post)
    # api.add_resource(Status, '/api//v1/status')

    socketio = config.socketio
    status = StatusAPI(socketio)
    socketio.on_event('connect', status.connected, namespace='/api/v1/status')
    socketio.on_event('disconnect', status.disconnected, namespace='/api/v1/status')
    socketio.on_event('get_status', status.get_status, namespace='/api/v1/status')
    #socketio.on_event('message', s.handle_message, namespace='/api/v1/status')

    
    
