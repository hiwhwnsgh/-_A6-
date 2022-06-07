import csv
from tkinter import messagebox


class JobAddSystem():
    JobName = ""
    JobInformation = ""
    JobDepartment = ""
    JobCertifi = ""
    JobToeic = ""
    JobWage = ""
    JobProsp = ""
    jobEquality = ""
    JobView = ""
    JobMale = ""
    JobLink = ""

    b = 0

    def JobCheck(JobName):
        JobNameList = []
        file = open("csv/Job.csv")
        read = csv.reader(file, delimiter=",")
        for row in read:
            JobNameList.append(row[0])
        file.close()
        a = 1
        global b
        for name in JobNameList:
            if name == JobName:
                a = 0
                b = 0
        if JobName == "":
            b = 1
        elif a == 1:
            b = 2

        if a == 0:
            messagebox.showinfo("직업 등록", "이미 존재하는 직업입니다.")
            a = 1
        elif b == 1:
            messagebox.showinfo("직업 등록", "직업 이름을 적으세요.")
            b = 0
        elif b == 2:
            messagebox.showinfo("직업 등록", "등록 가능합니다.")

    def TableLoad(JobTree):
        for item in JobTree.get_children():
            JobTree.delete(item)
        file = open("csv/Job.csv")
        read = csv.reader(file, delimiter=",")
        n = 0
        for row in read:
            if n != 0:
                JobTree.insert('', 'end', values=(row[0], row[4], row[6]))
            n += 1  # 첫 번째 항목 제외
        file.close()

    # 직업등록
    def JobAddDB(JobName, JobInformation, JobCertifi, JobToeic, JobDepartment, JobWage, JobProsp, jobEquality, JobView, JobMale, JobLink, JobTree):
        try:
            if (JobInformation == "" or JobDepartment == "" or JobCertifi == ""
                    or JobToeic == "" or JobWage == "" or JobProsp == "" or JobMale == "" or JobLink == "" or JobView == "" or jobEquality == ""):
                messagebox.showinfo("직업 등록", "빈 칸이 있습니다.")
            else:
                global b
                CheckBox = messagebox.askquestion(
                    "직업 등록", "직업을 등록하시겠습니까?")
                if CheckBox == 'yes':
                    if b == 2:
                        file = open("csv/Job.csv", "a")
                        csv_writer = csv.writer(
                            file, delimiter=",", lineterminator="\n")
                        csv_writer.writerow([JobName, JobInformation, JobCertifi, JobToeic,
                                            JobDepartment, JobWage, JobProsp,
                                            jobEquality, JobView, JobMale, JobLink])
                        messagebox.showinfo("직업 등록", "등록이 완료 되었습니다.")
                        b = 0
                        JobAddSystem.TableLoad(JobTree)  # 새로고침
                        return 1
                    else:
                        messagebox.showinfo("직업 등록", "중복확인 해주세요.")
                        return 2
                else:
                    messagebox.showinfo("직업 등록", "등록이 되지 않았습니다.")
                    return 2
        except(NameError):
            messagebox.showinfo("직업 등록", "중복확인 해주세요.")
