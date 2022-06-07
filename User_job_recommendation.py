from JobUI import *
from User_job_recommendationSystem import User_job_recommendationSystem


class User_job_recommendation(JobUI):
    def __init__(self,name):
        JobUI.__init__(self)
        namelabel = Label(self.window,text=name+"님의 추천 리스트",font=("맑은고딕",16,"bold"))
        namelabel.place(x=10,y=30)
        recommendation = User_job_recommendationSystem()
        recommendation.insert_treeview(self.Table,name)
        

