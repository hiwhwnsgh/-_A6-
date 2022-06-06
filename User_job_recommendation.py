from JobUI import *
from User_job_recommendationSystem import User_job_recommendationSystem


class User_job_recommendation(JobUI):
    def __init__(self,name):
        JobUI.__init__(self)
        recommendation = User_job_recommendationSystem()
        recommendation.insert_treeview(self.Table,name)
        

