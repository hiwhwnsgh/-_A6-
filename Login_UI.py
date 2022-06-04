from tkinter import *
from tkinter import messagebox
from tkinter import Button, Label, PhotoImage, font  as tkfont
from Register_UI import Register_UI
'''import tkinter as tk

from PIL import Image
from PIL import Image,ImageTk
from matplotlib import container'''

class Login_UI():

    def __init__(self):
        self.window =Tk()
        self.checkbutton = Button(self.window)
        self.window.title("로그인")
        self.window.geometry("550x550")
        self.window.resizable(width =FALSE,height=FALSE)

        self.label1 = Label(self.window,text="직업",font=("맑은고딕",30,"bold"))
        self.label1.place(x=80,y=70)

        self.label2 = Label(self.window,text="관리 프로그램",font=("맑은고딕",30,"bold"))
        self.label2.place(x=80,y=120)

        self.Id_text_label = Label(self.window,text="아이디",font=("맑은고딕",11))
        self.Id_text_label.place(x=80,y=210)

        self.Id_Entry = Entry(self.window)
        self.Id_Entry.place(x=80,y=238,width=390,height=30)

        self.Pw_text_label = Label(self.window,text="비밀번호",font=("맑은고딕",11))
        self.Pw_text_label.place(x=80,y=277)

        self.Pw_Entry = Entry(self.window)
        self.Pw_Entry.place(x=80,y=305,width=390,height=30) ###

        self.Login_button = Button(self.window,text="로 그 인",bg="cornflowerblue",font=("맑은고딕",18,"bold"),\
            fg="white")
        self.Login_button.place(x=80,y=360,width=390,height=60)

        self.sign_up_button = Button(self.window,text="회원가입",bg="grey",font=("맑은고딕",13)\
            ,command= Register_UI)
        self.sign_up_button.place(x=145,y=450,width=260,height=50)


        self.window.mainloop()




abc = Login_UI()
'''
class Login(Login_UI):

    def __init__(self):
        Login_UI.__init__(self)
        self.Login_button = Button(self.window,text="로그인",command = self.Login_System)
        self.Login_button.place(x=160,y=350)

    #def Login_System(self):'''
'''
class Register_UI ():

    def __init__(self) :


    def sign_up(self):


    '''