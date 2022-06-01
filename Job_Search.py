from asyncio.windows_events import NULL
from cProfile import label
from calendar import c
from faulthandler import disable
from operator import index
from cv2 import line
import pandas as pd
import numpy as np
import platform
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from tkinter import ttk

from pyparsing import null_debug_action

DIR_CSV_JOB = "Job.csv"

class JobUI():
    def __init__(self):
        self.window = Tk()
        self.action = JobSearchSystem()
        self.checkButton = Button(self.window)
        self.window.title("직업조회프로그램")
        self.window.geometry("1400x800")
        # TreeView 기본 설정
        columns = ["직업이름"]
        width = [400]
        self.Table =ttk.Treeview(self.window,columns=columns,displaycolumns=columns)
        self.Table.place(x=10,y=60)
        for i in range(len(columns)):
            self.Table.column(columns[i],width=width[i],anchor="center")
            self.Table.heading(columns[i],text=columns[i],anchor="center")
        self.Table["show"]= "headings"

        self.checkButton.config(width=56,text="선택",command=self.Checkbtn)
        self.checkButton.place(x=10,y=300)

        self.nameLabel = Label(self.window,font=("맑은고딕",20,"bold"))
        self.nameLabel.place(x=440,y=30)

        self.information = Label(self.window,text="직업정보",font=("맑은고딕",10,"bold"))
        self.information.place(x=440,y=70)

        self.informationText = Text(self.window,width=70,relief="flat",height=8,font=("맑은고딕",10))
        self.informationText.place(x=440,y=90)
        
        self.Department = Label(self.window,text="관련학과",font=("맑은고딕",10,"bold"))
        self.Department.place(x=440,y=200)

        self.DepartmentText = Label(self.window)
        self.DepartmentText.place(x=440,y=220)

        self.Spec = Label(self.window,text="관련자격증",font=("맑은고딕",10,"bold"))
        self.Spec.place(x=730,y=200)

        self.SpecText = Label(self.window)
        self.SpecText.place(x=730,y=220)

        self.money = Label(self.window,text="임금",font=("맑은고딕",10,"bold"))
        self.money.place(x=440,y=300)
        self.moneyText= Label(self.window)
        self.moneyText.place(x=440,y=320)

        self.Possibility = Label(self.window,text="발전가능성",font=("맑은고딕",10,"bold"))
        self.Possibility.place(x=620,y=300)
        self.PossibilityText = Label(self.window)
        self.PossibilityText.place(x=620,y=320)

        self.employ = Label(self.window,text="고용가능성",font=("맑은고딕",10,"bold"))
        self.employ.place(x=800,y=300)
        self.employText = Label(self.window)
        self.employText.place(x=800,y=320)

        self.view = Label(self.window,text="직업 전망",font=("맑은고딕",10,"bold"))
        self.view.place(x=440,y=400)

        self.sexLabel = Label(self.window,text="남녀 분포도",font=("맑은고딕",10,"bold"))
        self.sexLabel.place(x=960,y=70)

        self.Link = Label(self.window,text="관련 링크",font=("맑은고딕",10,"bold"))
        self.Link.place(x=960,y=440)
        self.LinkText = Text(self.window,font=("맑은고딕",10),width=57,height=2)
        self.LinkText.place(x=960,y=460)
        
        

        if platform.system() == 'Windows':
            plt.rc('font', family='Malgun Gothic')
        elif platform.system() == 'Darwin': # Mac
            plt.rc('font', family='AppleGothic')
        else: #linux
            plt.rc('font', family='NanumGothic')

        # 그래프에 마이너스 표시가 되도록 변경
        plt.rcParams['axes.unicode_minus'] = False
        
        self.fig = Figure(figsize=(7,4), dpi=70)  #그리프 그릴 창 생성

        
        self.fig2 = Figure(figsize=(5,4), dpi=80)  #그리프 그릴 창 생성
        
    def Checkbtn(self):
        index_key = self.Table.focus()
        possibility = ["보상","고용안정","발전가능성","근무여건","전문성","고용평등"]
        sexname = ["남자","여자"]
        self.informationText.delete('1.0','end')
        self.LinkText.delete('1.0','end')
        list_select = self.action.CheckClick(index_key)
        self.nameLabel.config(text=list_select[0])
        self.informationText.insert('1.0',list_select[1])
        self.SpecText.configure(text=list_select[2])
        self.DepartmentText.configure(text=list_select[4])
        list_select[5] = str(round(list_select[5]))
        self.moneyText.configure(text="평균 "+list_select[5]+"만원")
        self.PossibilityText.configure(text=list_select[6])
        self.employText.configure(text=list_select[7])
        self.LinkText.insert('1.0',list_select[10])
        list_int = list_select[8].split(",")
        self.fig.add_subplot(1,1,1).barh(possibility,list_int,color=["gold","red","blue","green","yellow","gray"])#창에 그래프 하나 추가
        canvas = FigureCanvasTkAgg(self.fig, master=self.window)
        canvas.draw()
        canvas.get_tk_widget().place(x=440,y=440)

        list_float = list_select[9].split(",")
        self.fig2.add_subplot(1,1,1).pie(list_float,labels=sexname,autopct="%.1f",colors=["red","blue"])#창에 그래프 하나 추가
        canvas2 = FigureCanvasTkAgg(self.fig2,master=self.window)
        canvas2.draw()
        canvas2.get_tk_widget().place(x=960,y=100)
        


class JobSearch(JobUI):
    def __init__(self):
        JobUI.__init__(self)
        self.Search = Entry(self.window,width=55)
        self.Search.place(x=10,y=30)
        self.SearchButton = Button(self.window,text="검색",command=self.Searchbtn)
        self.SearchButton.place(x=375,y=30)
    def Searchbtn(self):
        index_key = self.Search.get()
        self.action.SearchClick(index_key,self.Table)
        self.Search.delete("0","end")
    

class JobSearchSystem():
    def __init__(self):
        df_Job = pd.read_csv("csv/Job.csv",encoding='CP949')
        self.df_Job = df_Job.set_index('jobName',drop=False)
    def SearchClick(self,str,treeView):
        # 테이블 초기화
        for item in treeView.get_children():
            treeView.delete(item)
        df_contains = self.df_Job[self.df_Job['jobName'].str.contains(str)]
        for select_name in df_contains['jobName']:
            name= df_contains['jobName'].loc[select_name]
            treeView.insert('','end',text='',value=name,iid=name)

    def CheckClick(self,index_key):
        name = self.df_Job['jobName'].loc[index_key]
        information = self.df_Job['jobInformation'].loc[index_key]
        Certifi = self.df_Job['jobCertifi'].loc[index_key]
        Toeic = self.df_Job['jobToeic'].loc[index_key]
        Department = self.df_Job['jobDepartment'].loc[index_key]
        Wage = self.df_Job['jobWage'].loc[index_key]
        Prospect = self.df_Job['jobProspect'].loc[index_key]
        Equality = self.df_Job['jobEquality'].loc[index_key]
        View = self.df_Job['jobView'].loc[index_key]
        Sex = self.df_Job['jobSex'].loc[index_key]
        Link = self.df_Job['jobLink'].loc[index_key]
        job_add =[name,information,Certifi,Toeic,Department,Wage,Prospect,Equality,View,Sex,Link]
        return job_add