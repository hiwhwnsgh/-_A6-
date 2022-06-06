
from tkinter import messagebox
from JobDB import JobDB
from JobDB import *
from UserDB import UserDB
class User_job_recommendationSystem():
    def __init__(self,treeView,name):
        userdb = UserDB()
        jobdb = JobDB()
        userdb.set_index_key(name)
        userCertifi = userdb.get_Certifi()
        try:
            userCertifi = userCertifi.split(",")
            self.jobdb = jobdb.get_df()
            count = 0
            for item in treeView.get_children():
                treeView.delete(item)
            for i in range(len(userCertifi)):
                row = self.jobdb[self.jobdb['jobCertifi'].str.contains(userCertifi[i])]
                for select_row in row['jobName']:
                    count+=1
                    name= row['jobName'].loc[select_row]
                    treeView.insert('','end',text='',value=name,iid=name)
            if count == 0:
                messagebox.showerror('알림','등록된 자격증 중에 추천 직업이 없습니다')
        except:
            messagebox.showerror('알림','등록된 자격증 중에 추천 직업이 없습니다')
