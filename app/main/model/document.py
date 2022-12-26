from .. import config

class Document(object):
    def __init__(self,name):
        self.__dict__['name'] = name
        self.__dict__['data'] = {}
    
    def __setattr__(self, name, value):
        if name in ['data','name']:
            self.__dict__[name] = value
        self.data[name] = value

    def __getattr__(self, name):
        if name in self.data:
            return self.data[name]
    def save(self):
        config.mongo.db[self.name].insert_one(self.data)
    
    def load(self,data):
        self.data = data
        
    def __str__(self):
        return str(self.data)
