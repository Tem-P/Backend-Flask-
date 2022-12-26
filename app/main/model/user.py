from .document import Document
from .. import config

class User(Document):
    def __init__(self):
        super().__init__('user')
    
    def get(query):
        data = config.mongo.db['user'].find(query)
        users = []
        for d in data:
            u = User()
            u.load(d)
            users.append(u)
        if len(users)==0:
            return None
        return users
    
    def __str__(self):
        return super().__str__()
