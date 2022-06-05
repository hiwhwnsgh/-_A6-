from tkinter import *
from tkinter.ttk import *

class SpeckSearchUI_right(Frame) :
    def __init__(self,parent,controller):
        Frame.__init__(self,parent)
        self.controller = controller
        self.parent= parent

        # 검색창(Entry, Button) 프레임
        job_name_frame = Frame(self.parent)

        self.JobImageLabel = Label(job_name_frame, width=5)  # 검색버튼
        self.JobImageLabel.pack(side='left')
        self.JobNameLabel = Label(job_name_frame, text = '경호원',width=10)  # 검색창
        self.JobNameLabel.pack(side='left')

        job_name_frame.pack()

        self.s = Style(self).configure('self.Treeview', rowheight=80)

        # 테이블 생성
        self.SearchTable = Treeview(self.parent, selectmode='browse',height=3,style ='self.Treeview')
        self.SearchTable['columns'] = ('one','two','three')
        self.SearchTable['show'] = 'headings'

        self.SearchTable.pack()

        # 테이블 속성 설정
        self.SearchTable.column("one", width=50,anchor='center' )
        self.SearchTable.heading("one", text="자격증", anchor="center")

        self.SearchTable.column("two", width=150, )
        self.SearchTable.heading("two", text="회원 SPEC", anchor="center")

        self.SearchTable.column("three", width=150, )
        self.SearchTable.heading("three", text="직업", anchor="center")
        # 테이블 값 입력
        job_list = [('필수','없음','신변보호사\n(국가공인 민간)'),
                    ('관련','자동차운전면허 2종 보통\n(국가전문)','일반경비지도사\n(국가전문)\n자동차운전면허 제 1종,2종 보통\n(국가전문)'),
                    ('TOEIC','500점','700점(가산점)'),
                    ]

        for i in range(len(job_list)):
            self.SearchTable.insert('', 'end', values=job_list[i])

        #확인버튼
        self.Confirm_Button = Button(self.parent, text = '확인',width = 30)
        self.Confirm_Button.pack(pady=40)