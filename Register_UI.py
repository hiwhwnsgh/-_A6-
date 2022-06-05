from tkinter import *
from tkinter import messagebox
from tkinter import Button, Label, PhotoImage, font  as tkfont
import tkinter as tk

from PIL import Image
from PIL import Image,ImageTk
from matplotlib import container
### 이름 아이디 비밀번호 전화번호, 주민번호, 자격증 토익점수

class Register_UI ():

    def __init__(self) :
        self.window = Tk()
        self.window.title("회원가입")
        self.window.geometry("450x600")
        self.window.resizable(width =FALSE,height=FALSE)

        #
        self.Name_label = Label(self.window,text="이름",font=("맑은고딕",11))
        self.Name_label.place(x=30,y=15)

        self.Name_Entry = Entry(self.window)
        self.Name_Entry.place(x=30,y=40,width=390,height=27)
        #
        self.Id_Re_label = Label(self.window,text="아이디",font=("맑은고딕",11))
        self.Id_Re_label.place(x=30,y=75)

        self.Id_Re_Entry = Entry(self.window)
        self.Id_Re_Entry.place(x=30,y=100,width=390,height=27)
        #
        self.Pw_Re_label = Label(self.window,text="비밀번호",font=("맑은고딕",11))
        self.Pw_Re_label.place(x=30,y=175)

        self.Pw_Re_Entry = Entry(self.window)
        self.Pw_Re_Entry.place(x=30,y=200,width=390,height=27)
        #
        self.Phone_label = Label(self.window,text="전화번호",font=("맑은고딕",11))
        self.Phone_label.place(x=30,y=235)

        ### 전화번호 엔트리 3개로 나눔 그리고 나중에 병합
        self.Phone_Entry = Entry(self.window)
        self.Phone_Entry.place(x=30,y=260,width=100,height=27)
        self.Phone_Entry1 = Entry(self.window)
        self.Phone_Entry1.place(x=175,y=260,width=100,height=27)
        self.Phone_Entry2 = Entry(self.window)
        self.Phone_Entry2.place(x=320,y=260,width=100,height=27)
        #

        self.User_Number_label = Label(self.window,text="주민번호",font=("맑은고딕",11))
        self.User_Number_label.place(x=30,y=295)
        ### 주민번호 엔트리 2개로 나눔
        self.User_Number_Entry = Entry(self.window)
        self.User_Number_Entry.place(x=30,y=320,width=155,height=27)
        self.User_Number_Entry1 = Entry(self.window)
        self.User_Number_Entry1.place(x=265,y=320,width=155,height=27)
        #
        self.Spec_label = Label(self.window,text="자격증",font=("맑은고딕",11))
        self.Spec_label.place(x=30,y=355)

        self.Spec_Entry = Entry(self.window)
        self.Spec_Entry.place(x=30,y=380,width=390,height=27)
        #

        self.Toeic_text_label = Label(self.window,text="TOEIC 점수",font=("맑은고딕",11))
        self.Toeic_text_label.place(x=30,y=445)

        self.Toeic_Entry = Entry(self.window)
        self.Toeic_Entry.place(x=30,y=470,width=390,height=27)

        ##중복확인 버튼
        self.Id_check_button = Button(self.window,text="중복확인",bg="lightsteelblue")
        self.Id_check_button.place(x=340,y=140,width=80,height=30)

        ##자격증 찾기 버튼
        self.Spec_Search_button = Button(self.window,text="찾기",bg="lightsteelblue")
        self.Spec_Search_button.place(x=340,y=420,width=80,height=30)

        ##회원 가입 버튼
        self.Sign_Up_button = Button(self.window,text="회원가입",font=("맑은고딕",16,"bold"),\
            bg="cornflowerblue", fg="white")
        self.Sign_Up_button.place(x=30,y=518,width=390,height=60)

        self.window.mainloop()

