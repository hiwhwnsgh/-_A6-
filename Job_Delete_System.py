import csv
from tkinter import messagebox


class JobDeleteSystem():
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

 # 직업 선택하면 빈 칸을 채워준다
    def JobLoad(value):
        Job_List = ["", "", "", "", "", "", "", "", "", "", ""]
        file = open("csv/Job.csv")
        reader = csv.reader(file, delimiter=",")
        for row in reader:
            if value == row[0]:
                Job_List[0] = row[0]
                Job_List[1] = row[1]
                Job_List[2] = row[2]
                Job_List[3] = row[3]
                Job_List[4] = row[4]
                Job_List[5] = row[5]
                Job_List[6] = row[6]
                Job_List[7] = row[7]
                Job_List[8] = row[8]
                Job_List[9] = row[9]
                Job_List[10] = row[10]
        file.close()
        return Job_List

    # 테이블 값 입력
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

    # 직업삭제
    def JobDeleteDB(JobName, JobTree):
        data = []
        file = open("csv/Job.csv", "r")
        read = csv.reader(file, delimiter=",")
        for row in read:
            if row[0] == JobName:
                pass
            else:
                data.append(row)
        file.close()

        CheckBox = messagebox.askquestion(
            "직업 삭제", "정말 삭제하시겠습니까?")
        if CheckBox == 'yes':
            file = open("csv/Job.csv", "w")
            write = csv.writer(file, delimiter=",", lineterminator="\n")
            write.writerows(data)
            file.close()
            messagebox.showinfo("직업 삭제", "삭제가 완료 되었습니다.")
            JobDeleteSystem.TableLoad(JobTree)  # 새로고침
            return 1
        else:
            messagebox.showinfo("직업 삭제", "삭제가 되지 않았습니다.")
            return 2
