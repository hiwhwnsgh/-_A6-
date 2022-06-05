
from JobDB import JobDB

from JobDB import *
class User_job_recommendationSystem():
    def __init__(self,treeView):
        strlist = ['정보처리기능사', '산업기사']
        CheckList = []
        jobdb = JobDB()
        self.jobdb = jobdb.get_df()
        columns = self.jobdb['jobInformation']
        for item in treeView.get_children():
            treeView.delete(item)
        df_contains = self.jobdb[self.jobdb['jobName'].str.contains(strlist[0])]
        print(df_contains)
            # 테이블 초기화
