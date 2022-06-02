from tkinter import *
from tkinter import messagebox
from tkinter import Button, Label, PhotoImage, font  as tkfont
from PIL import Image
from PIL import Image,ImageTk
from matplotlib import container

class Login_UI ():

    def __init__(self) :
        self.window = Tk()
       # self.action = JobSearchSystem()
        self.checkButton = Button(self.window)
        self.window.title("로그인")
        self.window.geometry("600x500")
        self.window.resizable(width = FALSE, height=FALSE)
        self.checkButton = Button(self.window)

        self.label1 = Label(self.window, text="직업",font=("맑은고딕",30,"bold"))
        self.label1.place(x=80,y=70)

        self.label2 = Label(self.window, text="관리 프로그램",font=("맑은고딕",30,"bold"))
        self.label2.place(x=80,y=120)

        self.Id_text_label = Label(self.window,text="아이디", font=("맑은고딕",10))
        self.Id_text_label.place(x=80,y=220)

        self.Id_Entry = Entry(self.window)
        self.Id_Entry.place(x=80,y=240,width=320,height=25)

        self.Pw_text_label = Label(self.window,text="비밀번호", font=("맑은고딕",10))
        self.Pw_text_label.place(x=80,y=280)

        self.Pw_Entry = Entry(self.window)
        self.Pw_Entry.place(x=80,y=300,width=320,height=25)

        

        
        

        


        self.window.mainloop()

abc = Login_UI()

class Login(Login_UI):
    
    def __init__(self):
        Login_UI.__init__(self)
        self.Login_button = Button(self.window , text = "로그인",command=self.Login_System)
        self.Login_button.place(x=160,y=350)


    #def Login_System(self):
