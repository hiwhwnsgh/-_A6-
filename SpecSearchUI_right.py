from tkinter import *
from tkinter.ttk import *
import pandas as pd

class SpecSearchUI_right(Frame) :
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.controller = controller
        self.parent= parent

        jobDB = JobDB()
        self.df_Job = jobDB.get_df()

        userDB = UserDB()
        self.df_User = userDB.get_df()

        # 검색창(Entry, Button) 프레임
        job_name_frame = Frame(self.parent)

        self.JobImageLabel = Label(job_name_frame, width=5)  # 검색버튼
        self.JobImageLabel.pack(side='left')
        self.JobNameLabel = Label(job_name_frame, text = '',anchor="center",width=20)  # 검색창
        self.JobNameLabel.pack(side='left')

        job_name_frame.pack()

        self.s = Style(self).configure('self.Treeview', rowheight=80)

        # 테이블 생성
        self.SearchTable = Treeview(self.parent, selectmode='browse',height=3,style ='self.Treeview')
        self.SearchTable['columns'] = ('one','two','three')
        self.SearchTable['show'] = 'headings'

        self.SearchTable.pack(padx=20)

        # 테이블 속성 설정
        self.SearchTable.column("one", width=50,anchor='center' )
        self.SearchTable.heading("one", text="자격증", anchor="center")

        self.SearchTable.column("two", width=180, )
        self.SearchTable.heading("two", text="회원 SPEC", anchor="center")

        self.SearchTable.column("three", width=180, )
        self.SearchTable.heading("three", text="직업", anchor="center")
        # 테이블 값 입력
        job_list = [('필수','',''),
                    ('관련','',''),
                    ('TOEIC','',''),
                    ]

        for i in range(len(job_list)):
            self.SearchTable.insert('', 'end', values=job_list[i])

        #확인버튼
        self.Confirm_Button = Button(self.parent, text = '확인',width = 30,command= lambda : self.forget())
        self.Confirm_Button.pack(pady=40)

    def forget(self):
        self.parent.pack_forget()

    def modify(self,job_name,user_name):

        self.JobNameLabel.configure(text=job_name)

        for item in self.SearchTable.get_children():
            self.SearchTable.delete(item)

        # 테이블 값 입력
        job_list = [('필수',self.df_User['UserCertifi'].loc[user_name],self.df_Job['jobCertifi'].loc[job_name]),
                    ('관련',self.df_User['UserCertifi'].loc[user_name],self.df_Job['jobCertifi'].loc[job_name]),
                    ('TOEIC',self.df_User['UserToeic'].loc[user_name],self.df_Job['jobToeic'].loc[job_name]),
                    ]

        for i in range(len(job_list)):
            self.SearchTable.insert('', 'end', values=job_list[i])


class JobDB():
    def __init__(self):
        df_Job = pd.read_csv("csv/Job.csv",encoding='CP949')
        self.df_Job = df_Job.set_index('jobName',drop=False)
    def get_df(self):
        return self.df_Job

class UserDB():
    def __init__(self):
        df_User = pd.read_csv("csv/User.csv",encoding='CP949')
        self.df_User = df_User.set_index('UserName',drop=False)
    def get_df(self):
        return self.df_User