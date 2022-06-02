from tkinter import *
from tkinter.ttk import*

root = Tk()
root.title("직업 목록 조회")
root.geometry("500x300")
root.resizable(False,False)

label = Label(root,text='직억 목록 조회')
label.pack(pady=10)
#테이블과 스크롤바를 넣을 프레임 생성
frame = Frame(root)

#테이블 생성
treeview = Treeview(frame, selectmode = 'browse')
treeview['columns'] = ('one','two','three')
treeview['show'] = 'headings'
treeview.pack(side='left')

#스크롤바 생성
scrollbar = Scrollbar(frame,command=treeview.yview)
scrollbar.pack(side='right',fill='y')
treeview.configure(yscrollcommand=scrollbar.set)

#테이블 속성 설정
treeview.column("one",width=100,)
treeview.heading("one",text = "직업이름",anchor="center")

treeview.column("two",width=100,)
treeview.heading("two",text = "관련학과",anchor="center")

treeview.column("three",width=100,)
treeview.heading("three",text = "전망",anchor="center")

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
    treeview.insert('','end',values=job_list[i])
    
frame.pack(pady=10)
root.mainloop()
