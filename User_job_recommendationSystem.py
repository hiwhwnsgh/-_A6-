
from JobDB import JobDB
from JobDB import *
class User_job_recommendationSystem():
    def __init__(self,treeView):
        strlist = ['정보처리기능사', '산업기사']
        jobdb = JobDB()
        self.jobdb = jobdb.get_df()
        for item in treeView.get_children():
            treeView.delete(item)
        row = self.jobdb[self.jobdb['jobCertifi'].str.contains(strlist[0])]
        for select_row in row['jobName']:
            name= row['jobName'].loc[select_row]
            treeView.insert('','end',text='',value=name,iid=name)
            # 테이블 초기화
