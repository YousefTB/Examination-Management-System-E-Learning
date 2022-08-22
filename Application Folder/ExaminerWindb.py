# ----------------------
# database functions Module
# ----------------------

import sqlite3

DB_FILENAME = 'Exam system db.db'

################## To get personal info field ######################


def personInfo_examiner(examiner_id):
    conn = sqlite3.connect(DB_FILENAME)
    res = conn.execute(
        f"""select examiner.examiner_id, examiner.examiner_name, examiner.examiner_num
        , examiner.examiner_gen, examiner.examiner_email, examiner.examiner_phone, department.dep_name 
        from examiner, department  where examiner_id = {examiner_id} and examiner.dep_id = department.dep_id
        """)
    res = list(res)
    conn.close()
    return res[0]


################## Exams management field ######################

# To get exams froma database
def get_exams(examiner_id):
    conn = sqlite3.connect(DB_FILENAME)
    res = conn.execute(
        f"""select * from exam where examiner_id = {examiner_id}
        """)
    res = list(res)
    conn.close()
    return res


def insert_exams(exam_name, exam_beg_date, exam_beg_time, exam_end_date, exam_end_time, total_deg, examiner_id):
    conn = sqlite3.connect(DB_FILENAME)
    conn.execute(
        f"""
        insert into exam (exam_name, beg_dat, beg_time, fin_dat, fin_time, total_deg, examiner_id) 
        values ('{exam_name}', '{exam_beg_date}','{exam_beg_time}','{exam_end_date}','{exam_end_time}','{total_deg}',{examiner_id})
        """)
    conn.commit()
    conn.close()

# insert_exams("Algorithm midterm", "09/12/22", "01:00", "09/12/22", "03:00", 15, 1)


def update_exams(exam_id, exam_name, exam_beg_date, exam_beg_time, exam_end_date, exam_end_time, total_deg, examiner_id):
    conn = sqlite3.connect(DB_FILENAME)
    conn.execute(
        f"""
        update exam set exam_name = '{exam_name}' , beg_dat = '{exam_beg_date}', beg_time = '{exam_beg_time}'
        , fin_dat = '{exam_end_date}', fin_time = '{exam_end_time}', total_deg = '{total_deg}', examiner_id = {examiner_id}
        where exam_id = {exam_id}
        """)
    conn.commit()
    conn.close()


# update_exams(5, "Linear algebra midterm", "10/12/22","09:00", "10/12/22", "012:00", 40, 1)

def delete_exams(exam_id):
    conn = sqlite3.connect(DB_FILENAME)
    conn.execute(
        f"""
        delete from exam
        where exam_id = {exam_id}
        """)
    conn.commit()
    conn.close()

# delete_exams(5)

################## Question management field ######################


# Exams for combobox
ex_in_list = []
ex_in_dic = {}


def get_exams_combo(ex_in_list, ex_in_dic, examiner_id):
    conn = sqlite3.connect(DB_FILENAME)
    res = conn.execute(
        f"select * from exam where examiner_id = {examiner_id} ")
    res = list(res)
    conn.close()
    for e in res:
        ex_in_list.append(e[1])

    for e in res:
        ex_in_dic[e[1]] = e[0]


def get_question(exam_id):
    conn = sqlite3.connect(DB_FILENAME)
    res = conn.execute(
        f"""
        select * from question where ex_id = {exam_id}
        """)
    res = list(res)
    conn.close()
    return res


def insert_question(name, ans1, ans2, ans3, ans4, correct_ans, deg, exam_id):
    conn = sqlite3.connect(DB_FILENAME)
    conn.execute(
        f"""
        insert into question (q_name, ans1, ans2, ans3, ans4, correct_ans, q_deg, ex_id) 
        values ('{name}', '{ans1}','{ans2}','{ans3}','{ans4}','{correct_ans}',{deg},{exam_id})
        """)
    conn.commit()
    conn.close()


#insert_question("What is time complexity ?", "Its an algorithm", "Analysis method", "none of them", "both of them",               "Analysis method", 15, 4)

def update_question(id, name, ans1, ans2, ans3, ans4, correct_ans, deg, exam_id):
    conn = sqlite3.connect(DB_FILENAME)
    conn.execute(
        f"""
        update question set  q_name = '{name}', ans1 = '{ans1}', ans2 = '{ans2}', ans3 = '{ans3}'
        , ans4 = '{ans4}', correct_ans = '{correct_ans}', q_deg = {deg}, ex_id = {exam_id} 
        where q_id = {id}
        """)
    conn.commit()
    conn.close()


#update_question(11, "What is time complexity ?", "Its an algorithm","Analysis method", "none of them", "both of them", "Analysis method", 10, 4)


def delete_question(id):
    conn = sqlite3.connect(DB_FILENAME)
    conn.execute(
        f"""
        delete from question
        where q_id = {id}
        """)
    conn.commit()
    conn.close()


def get_total_question_degrees(exam_id):
    conn = sqlite3.connect(DB_FILENAME)
    res = conn.execute(
        f"""
        select * from question where ex_id = {exam_id}
        """)
    res = list(res)
    conn.close()
    deg_list = []
    for q in res:
        deg_list.append(q[7])
    return sum(deg_list)

##################### Student exams frame ########################


def get_questions_ids(exam_id):
    conn = sqlite3.connect(DB_FILENAME)
    res = conn.execute(
        f"""
        select * from question where ex_id = {exam_id}
        """)
    res = list(res)
    conn.close()
    id_list = []
    for q in res:
        id_list.append(q[0])
    return id_list


def get_students_v2(examiner_id):
    conn = sqlite3.connect(DB_FILENAME)
    res = conn.execute(
        f"""select *
        from examiner where examiner_id = {examiner_id}
        """)
    res = list(res)
    dep = (res[0])[6]
    conn.close()

    conn = sqlite3.connect(DB_FILENAME)
    res2 = conn.execute(
        f"""
        select student.stu_id, student.stu_name 
        from student
        where dep_id = {dep}
        order by student.stu_name
        """)
    res2 = list(res2)
    conn.close()
    return res2


def get_students_exams(exam_id):
    conn = sqlite3.connect(DB_FILENAME)
    res = conn.execute(
        f"""select studentExam.exam_id , exam.exam_name, studentExam.stu_id, student.stu_name
        , studentExam.status, studentExam.stu_deg
        from studentExam, student, exam
        where studentExam.exam_id = exam.exam_id
        and studentExam.stu_id = student.stu_id
        and studentExam.exam_id = {exam_id}
        order by studentExam.status , student.stu_name
        """)
    res = list(res)
    conn.close()
    return res


def insert_exam_to_student(stu_id, exam_id):
    conn = sqlite3.connect(DB_FILENAME)
    conn.execute(
        f"""
        insert into studentExam (stu_id, exam_id) 
        values ({stu_id},{exam_id})
        """)
    conn.commit()
    conn.close()


def insert_question_to_student(stu_id, q_id):
    conn = sqlite3.connect(DB_FILENAME)
    conn.execute(
        f"""
        insert into student_question (stu_id, q_id) 
        values ({stu_id},{q_id})
        """)
    conn.commit()
    conn.close()


def delete_question_to_student(stu_id, q_id):
    conn = sqlite3.connect(DB_FILENAME)
    conn.execute(
        f"""
        delete from student_question
        where stu_id = {stu_id} and q_id = {q_id}
        """)
    conn.commit()
    conn.close()


def delete_exam_to_student(stu_id, exam_id):
    conn = sqlite3.connect(DB_FILENAME)
    conn.execute(
        f"""
        delete from studentExam  
        where stu_id = {stu_id} and exam_id = {exam_id}
        """)
    conn.commit()
    conn.close()


def get_students_exams_for_exel(exam_id):
    conn = sqlite3.connect(DB_FILENAME)
    res = conn.execute(
        f"""select studentExam.stu_id, student.stu_name
        , studentExam.stu_deg
        from studentExam, student, exam
        where studentExam.exam_id = exam.exam_id
        and studentExam.stu_id = student.stu_id
        and studentExam.exam_id = {exam_id}
        order by studentExam.status , student.stu_name
        """)
    res = list(res)
    conn.close()
    return res
