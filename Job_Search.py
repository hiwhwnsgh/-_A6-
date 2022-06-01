from asyncio.windows_events import NULL
from cProfile import label
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

class JobSearch():
    def __init__(self):
        self.window = Tk()
        self.Table =ttk.Treeview(self.window)
        self.checkButton = Button(self.window)
        self.window.title("직업조회프로그램")
        self.window.geometry("1400x800")
        colums = ("직업이름")
        self.Table.config(columns=["직업이름"],displaycolumns=colums)
        self.Table.place(x=10,y=60)
        self.Table.column("직업이름",anchor="center")
        self.Table.heading("직업이름",text="직업이름",anchor="center")
        self.checkButton.config(width=50,text="선택")
        self.checkButton.place(x=10,y=300)

        self.nameLabel = Label(self.window,text="간호사",font=("맑은고딕",20,"bold"))
        self.nameLabel.place(x=440,y=30)

        self.information = Label(self.window,text="직업정보",font=("맑은고딕",10,"bold"))
        self.information.place(x=440,y=70)
        
        self.Department = Label(self.window,text="관련학과",font=("맑은고딕",10,"bold"))
        self.Department.place(x=440,y=200)

        self.DepartmentText = Label(self.window,text="학과없음")
        self.DepartmentText.place(x=440,y=220)

        self.Spec = Label(self.window,text="관련자격증",font=("맑은고딕",10,"bold"))
        self.Spec.place(x=730,y=200)

        self.SpecText = Label(self.window,text = "자격증없음")
        self.SpecText.place(x=730,y=220)

        self.money = Label(self.window,text="임금",font=("맑은고딕",10,"bold"))
        self.money.place(x=440,y=300)
        self.moneyText= Label(self.window,text="임금없음")
        self.moneyText.place(x=440,y=320)

        self.Possibility = Label(self.window,text="발전가능성",font=("맑은고딕",10,"bold"))
        self.Possibility.place(x=620,y=300)
        self.PossibilityText = Label(self.window,text="가능성없음")
        self.PossibilityText.place(x=620,y=320)

        self.employ = Label(self.window,text="고용가능성",font=("맑은고딕",10,"bold"))
        self.employ.place(x=800,y=300)
        self.employText = Label(self.window,text="고용가능성없음")
        self.employText.place(x=800,y=320)

        self.view = Label(self.window,text="직업 전망",font=("맑은고딕",10,"bold"))
        self.view.place(x=440,y=400)

        self.sexLabel = Label(self.window,text="남녀 분포도",font=("맑은고딕",10,"bold"))
        self.sexLabel.place(x=960,y=70)
        
        
        possibility = ["보상","고용안정","발전가능성","근무여건","전문성","고용평등"]
        values = [33,88,70,45,58,64]

        if platform.system() == 'Windows':
            plt.rc('font', family='Malgun Gothic')
        elif platform.system() == 'Darwin': # Mac
            plt.rc('font', family='AppleGothic')
        else: #linux
            plt.rc('font', family='NanumGothic')

        # 그래프에 마이너스 표시가 되도록 변경
        plt.rcParams['axes.unicode_minus'] = False
        
        fig = Figure(figsize=(7,4), dpi=70)  #그리프 그릴 창 생성
        fig.add_subplot(1,1,1).barh(possibility,values,color=["gold","red","blue","green","yellow","gray"])#창에 그래프 하나 추가
        
        canvas = FigureCanvasTkAgg(fig, master=self.window)
        canvas.draw()
        canvas.get_tk_widget().place(x=440,y=440)

        sex = [81.4,29.6]
        sexname = ["남자","여자"]
        fig2 = Figure(figsize=(5,4), dpi=80)  #그리프 그릴 창 생성
        #fig2.set_facecolor("#cdcdc")
        fig2.add_subplot(1,1,1).pie(sex,labels=sexname,autopct="%.1f",colors=["red","blue"])#창에 그래프 하나 추가
        canvas2 = FigureCanvasTkAgg(fig2,master=self.window)
        canvas2.draw()
        canvas2.get_tk_widget().place(x=960,y=100)
    def get_window(self):
        return self.window
        

class JobSearchSystem(JobSearch):
    def __init__(self):
        JobSearch.__init__(self)
        self.window = JobSearch.get_window()
        self.Search = Entry(self.window,width=30)
        self.Search.place(x=10,y=30)
        self.SearchButton = Button(self.window,text="검색")
        self.SearchButton.place(x=330,y=30)
        self.window.mainloop()

