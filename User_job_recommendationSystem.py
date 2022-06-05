
from JobDB import JobDB
from JobDB import *
class User_job_recommendationSystem():
    def __init__(self,treeView,name):
        self.df_User = pd.read_csv("csv/User.csv",encoding='CP949')
        self.df_User = self.df_User.set_index('UserName',drop=False)
        userCertifi = self.df_User['UserCertifi'].loc[name]
        userCertifi = userCertifi.split(",")
        jobdb = JobDB()
        self.jobdb = jobdb.get_df()
        for item in treeView.get_children():
            treeView.delete(item)
        for i in range(len(userCertifi)):
            row = self.jobdb[self.jobdb['jobCertifi'].str.contains(userCertifi[i])]
            for select_row in row['jobName']:
                name= row['jobName'].loc[select_row]
                treeView.insert('','end',text='',value=name,iid=name)
                # 테이블 초기화
