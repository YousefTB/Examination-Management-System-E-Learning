import sqlite3
import datetime
from tkinter import messagebox
DB_FILENAME = 'Exam system db.db'


def student_information(id):
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.cursor()
    data = cur.execute(
        "select stu_id,stu_name,stu_num,stu_gen,stu_email,stu_phone,dep_name from student,department where stu_id = ? and department.dep_id = student.dep_id", (id,))
    data = list(data)
    res = []
    for i in range(7):
        res.append(data[0][i])
    cur.close()
    return res


def student_exams(id):
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.cursor()
    data = cur.execute("select studentExam.exam_id, exam_name, beg_dat, beg_time, fin_dat,fin_time, total_deg, status, studentExam.stu_deg from exam,studentExam where studentExam.stu_id = ? and exam.exam_id = studentExam.exam_id", (id,))

    data = list(data)
    for i in range(len(data)):
        data[i] = list(data[i])
        datemanip = data[i][2].split('/')
        datemanip[2] = "20" + str(datemanip[2])
        date = datetime.datetime(int(datemanip[2]), int(
            datemanip[0]), int(datemanip[1]))
        data[i][2] = date.strftime("%d/%m/%Y")
        datemanip = data[i][4].split('/')
        datemanip[2] = "20" + str(datemanip[2])
        date = datetime.datetime(int(datemanip[2]), int(
            datemanip[0]), int(datemanip[1]))
        data[i][4] = date.strftime("%d/%m/%Y")
        data[i] = tuple(data[i])

    cur.close()
    return data


def exam_validation(exam_id,id):
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.cursor()
    data = cur.execute("select beg_dat,beg_time,status,fin_dat,fin_time from studentExam,exam where stu_id = ? and studentExam.exam_id = ? and exam.exam_id = studentExam.exam_id", (str(id),exam_id))
    data = list(data)
    res = [y for x in data for y in x]
    date = datetime.datetime.now()
    datenow = date.strftime("%x")
    timenow = date.strftime("%H:%M")

    if res[2] == "The exam is done":
        messagebox.showerror("Note","The exam is taken already !")
        cur.close()
        return 0


    if datenow < res[0] or (datenow == res[0] and timenow < res[1]):
        messagebox.showerror("Note","The exam have not started yet")
        cur.close()
        return 0

    if datenow > res[3] or (datenow == res[3] and timenow >= res[4]): 
        messagebox.showerror("Note","The exam is finished")
        cur.close()
        return 0

    cur.close()
    return 1