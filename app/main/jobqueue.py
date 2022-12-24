from collections import deque
from threading import Thread
import itertools
import time
from app.main.ML.poseDet import  weight_lifting

from os import path


class Job:
    lastjobid = itertools.count(0)
    def __init__(self,pathin=''):
        self.id = next(Job.lastjobid)
        self.pathin = pathin
        fname,ext = path.splitext(pathin)
        self.pathout = fname+"_out"+ext
        self.iscorrect = None
        self.done = False
        self.created = None # create time

class JobQueue:
    def __init__(self,nthread=2):
        self.threads = []
        self.queue = deque()
        self.stop = False
        self.locked = False
        self.comp_dic = {}          # contains key=id ,value = data of completed jobs
        for i in range(nthread):
            t = Thread(target=self.processjob, args=[self.queue])
            self.threads.append(t)
        
    
    def get_queue_lock(self):
        while self.locked:
            pass
        self.locked = True

    def release_queue_lock(self):
        self.locked = False

    def add(self,job):
        self.get_queue_lock()
        self.queue.append(job)
        self.release_queue_lock()
    
    def run_threads(self):
        for t in self.threads:
            t.run()

    def processjob(self,queue):
        while not self.stop:
            if self.queue:
                self.get_queue_lock()
                job = self.queue.popleft()
                self.release_queue_lock()
                "Call ML function with args=[path,config]"
                ret_val = None
                try:
                    ret_val = weight_lifting(job.pathin,job.pathout)
                    if ret_val:
                        job.iscorrect = True
                    else:
                        job.iscorrect = False
                except Exception as e:
                    pass
                self.comp_dic[job.id] = job
            else:
                time.sleep(0.1)


# export jobqueue so it can be used
jobqueue = JobQueue(2)