from collections import deque
from threading import Thread,Lock
#import itertools
import time
from app.main.ML.poseDet import  weight_lifting
from os import path
from flask_socketio import emit,socketio

class Job:
    #lastjobid = itertools.count(0)
    def __init__(self,username,pathin=''):
        self.id = None
        self.username = username
        self.pathin = pathin
        fname,ext = path.splitext(pathin)
        self.pathout = fname.replace('uploads','processed')+"_out"+".mkv"
        self.iscorrect = None
        self.done = False
        self.created = None # create time
        self.asked_status = False

class JobQueue:
    def __init__(self,app,nthread=2):
        self.threads = []
        self.queue = deque()
        self.stop = False
        self.queuelock = Lock()
        self.comp_dic = {}          # contains key=id ,value = data of completed jobs
        self.jobs_in_proc = {}
        self.app = app
        for i in range(nthread):
            t = Thread(target=self.processjob, args=[self.queue])
            t.daemon = True
            self.threads.append(t)
        self.run_threads()
        self.app.logger.info('{} job executor threads are starting')

    def stop_threads(self):
        self.stop = True
        for t in self.threads:
            t.join()
        
    
    def add(self,job):
        with self.queuelock:
            self.queue.append(job)
        
    def run_threads(self):
        for t in self.threads:
            t.start()

    def processjob(self,queue):
        while not self.stop:
            if self.queue:
                job = None
                with self.queuelock:
                    job = self.queue.popleft()
                self.app.logger.info('start processing job using thread')
                "Call ML function with args=[path,config]"
                ret_val = None
                try:
                    #time.sleep(5)
                    #ret_val = 1
                    ret_val = weight_lifting(job.pathin,job.pathout)
                    if ret_val:
                        job.iscorrect = True
                    else:
                        job.iscorrect = False
                except Exception as e:
                    pass
                # remove below line in future
                self.comp_dic[job.id] = job
                del(self.jobs_in_proc[job.id])
                self.app.logger.info("job {} completed result is correct = {}".format(job.id,job.iscorrect))

            else:
                time.sleep(0.1)


# export jobqueue so it can be used
# manage.py create and assigns jobqueue object
jobqueue = None