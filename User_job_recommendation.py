from JobUI import *
from User_job_recommendationSystem import User_job_recommendationSystem


class User_job_recommendation(JobUI):
    def __init__(self):
        JobUI.__init__(self)
        User_job_recommendationSystem.__init__(self,self.Table)
        