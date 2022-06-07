from tkinter import *
from tkinter import ttk
from Job_Delete_System import JobDeleteSystem


class JobDeleteUI():
    def __init__(self):
        win = Tk()
        win.title("직업 삭제 화면")
        win.geometry("1050x600+520+100")
        win.resizable(0, 0)
        name = StringVar()
        information = StringVar()
        department = StringVar()
        certifi = StringVar()
        toeic = StringVar()
        wage = StringVar()
        prosp = StringVar()
        equality = StringVar()
        view = StringVar()
        sex = StringVar()
        link = StringVar()

        Label(win, text="신규 직업 삭제",
              font=("맑은고딕", 16)).place(x=30, y=2+20)
        Label(win, text="직업 이름",
              font=("맑은고딕", 12)).place(x=30, y=50+20)
        Label(win, text="직업 정보",
              font=("맑은고딕", 12)).place(x=30, y=90+20)
        Label(win, text="직업 자격증",
              font=("맑은고딕", 12)).place(x=30, y=130+20)
        Label(win, text="직업 토익 점수",
              font=("맑은고딕", 12)).place(x=30, y=170+20)
        Label(win, text="직업 관련 학과",
              font=("맑은고딕", 12)).place(x=30, y=210+20)
        Label(win, text="직업 임금",
              font=("맑은고딕", 12)).place(x=30, y=250+20)
        Label(win, text="직업 발전 가능성",
              font=("맑은고딕", 12)).place(x=30, y=290+20)
        Label(win, text="직업 고용 가능성",
              font=("맑은고딕", 12)).place(x=30, y=330+20)
        Label(win, text="직업 전망",
              font=("맑은고딕", 12)).place(x=30, y=370+20)
        Label(win, text="직업 남녀 비율",
              font=("맑은고딕", 12)).place(x=30, y=410+20)
        Label(win, text="직업 관련 링크",
              font=("맑은고딕", 12)).place(x=30, y=450+20)

        JobNameEntry = Entry(win, textvariable=name,
                             width=50, state="disable")
        JobNameEntry.place(x=160, y=50+20)

        JobInformationEntry = Entry(
            win, textvariable=information, width=50, state="disable")
        JobInformationEntry.place(x=160, y=90+20)

        JobCertifiEntry = Entry(win, textvariable=certifi,
                                width=50, state="disable")
        JobCertifiEntry.place(x=160, y=130+20)

        JobToeicEntry = Entry(win, textvariable=toeic,
                              width=50, state="disable")
        JobToeicEntry.place(x=160, y=170+20)

        JobDepartmentEntry = Entry(
            win, textvariable=department, width=50, state="disable")
        JobDepartmentEntry.place(x=160, y=210+20)

        JobWageEntry = Entry(win, textvariable=wage, width=50, state="disable")
        JobWageEntry.place(x=160, y=250+20)

        JobProspEntry = Entry(win, textvariable=prosp,
                              width=50, state="disable")
        JobProspEntry.place(x=160, y=290+20)

        JobEqualityEntry = Entry(
            win, textvariable=equality, width=50, state="disable")
        JobEqualityEntry.place(x=160, y=330+20)

        JobViewEntry = Entry(win, textvariable=view, width=50, state="disable")
        JobViewEntry.place(x=160, y=370+20)

        JobMaleEntry = Entry(win, textvariable=sex, width=50, state="disable")
        JobMaleEntry.place(x=160, y=410+20)

        JobLinkEntry = Entry(win, textvariable=link, width=50, state="disable")
        JobLinkEntry.place(x=160, y=450+20)

        # 직업 목록 테이블
        Label(win, text="직업 목록",
              font=("맑은고딕", 16)).place(x=650, y=2+20)
        JobTree = ttk.Treeview(win, selectmode='browse', height=6)
        JobTree.place(x=650, y=50+20)
        JobTree['columns'] = ('one', 'two', 'three')
        JobTree['show'] = 'headings'
        s = ttk.Style()
        s.configure('Treeview', rowheight=60)

        JobDeleteSystem.TableLoad(JobTree)

        vsb = ttk.Scrollbar(win, orient="vertical", command=JobTree.yview)
        vsb.place(x=650+300+2, y=50+20, height=390)
        JobTree.configure(yscrollcommand=vsb.set)
        JobTree.column("one", width=100)
        JobTree.heading("one", text="직업이름", anchor="center")

        JobTree.column("two", width=100)
        JobTree.heading("two", text="관련학과", anchor="center")

        JobTree.column("three", width=100)
        JobTree.heading("three", text="전망", anchor="center")

        def click_item(event):
            Job_List = []
            selectedItem = JobTree.focus()
            getValue = JobTree.item(selectedItem).get(
                'values')  # 딕셔너리의 값만 가져오기
            Job_List = JobDeleteSystem.JobLoad(getValue[0])
            name.set(Job_List[0])
            information.set(Job_List[1])
            certifi.set(Job_List[2])
            toeic.set(Job_List[3])
            department.set(Job_List[4])
            wage.set(Job_List[5])
            prosp.set(Job_List[6])
            equality.set(Job_List[7])
            view.set(Job_List[8])
            sex.set(Job_List[9])
            link.set(Job_List[10])

        JobTree.bind('<ButtonRelease-1>', click_item)

        def JobDeleteDB():
            yes = JobDeleteSystem.JobDeleteDB(JobNameEntry.get(), JobTree)
            if yes == 1:
                name.set("")
                information.set("")
                department.set("")
                certifi.set("")
                toeic.set("")
                wage.set("")
                prosp.set("")
                equality.set("")
                view.set("")
                sex.set("")
                link.set("")

        def TableLoad():
            JobDeleteSystem.TableLoad(JobTree)

        OkButton = Button(win, text="직업 삭제", font=(
            "맑은고딕", 9), width=17, height=2, command=JobDeleteDB, bg="#DAE3F3").place(x=160, y=490+20)
        ReButton = Button(win, text="새로 고침", font=(
            "맑은고딕", 9), width=17, height=2, command=TableLoad, bg="#DAE3F3").place(x=700, y=490+20)
        CancleButton = Button(win, text="닫기", font=(
            "맑은고딕", 9), width=17, height=2, command=win.destroy, bg="#DAE3F3").place(x=330, y=490+20)

        win.mainloop()


JobDeleteUI()
