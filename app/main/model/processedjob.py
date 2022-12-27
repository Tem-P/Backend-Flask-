
from .document import Document
from .. import config

class ProcessedJob(Document):
    def __init__(self):
        super().__init__('job')
    def get(query):
        docs = config.mongo.db['job'].find(query)
        jobs = []
        for doc in docs:
            j = ProcessedJob()
            j.load(doc)
            jobs.append(j)
        if len(jobs)==0:
            return None
        return jobs
    
    def __str__(self):
        return super().__str__()
