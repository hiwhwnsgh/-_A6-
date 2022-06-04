from tkinter import *
from tkinter.ttk import*

class JobListUI (Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("직업 목록 조회")
        self.geometry("500x300")
        self.resizable(False,False)

        self.label = Label(self,text='직억 목록 조회')
        self.label.pack(pady=10)
        #테이블과 스크롤바를 넣을 프레임 생성
        frame = Frame(self)

        #테이블 생성
        self.JobListTable = Treeview(frame, selectmode = 'browse')
        self.JobListTable['columns'] = ('one','two','three')
        self.JobListTable['show'] = 'headings'
        self.JobListTable.pack(side='left')

        #스크롤바 생성
        self.scrollbar = Scrollbar(frame,command=self.JobListTable.yview)
        self.scrollbar.pack(side='right',fill='y')
        self.JobListTable.configure(yscrollcommand=self.scrollbar.set)

        #테이블 속성 설정
        self.JobListTable.column("one",width=100,)
        self.JobListTable.heading("one",text = "직업이름",anchor="center")

        self.JobListTable.column("two",width=100,)
        self.JobListTable.heading("two",text = "관련학과",anchor="center")

        self.JobListTable.column("three",width=100,)
        self.JobListTable.heading("three",text = "전망",anchor="center")

        #테이블 값 입력
        job_list = [('웹개발자','컴퓨터공학과','증가'),
                    ('한의사','한의학과','현상유지'),
                    ('소설가','국어국문학과','감소'),
                    ('미용사','뷰티아트과','현상유지'),
                    ('스포츠강사','체육학과','현상유지'),
                    ('판사','법학과','현상유지'),
                    ('항해사','해양공학과','감소'),
                    ('웹개발자','컴퓨터공학과','증가'),
                    ('한의사','한의학과','현상유지'),
                    ('소설가','국어국문학과','감소'),
                    ('미용사','뷰티아트과','현상유지'),
                    ('스포츠강사','체육학과','현상유지'),
                    ('판사','법학과','현상유지'),
                    ('항해사','해양공학과','감소')]

        for i in range(len(job_list)):
            self.JobListTable.insert('','end',values=job_list[i])

        frame.pack(pady=10)

app = JobListUI()
app.mainloop()
