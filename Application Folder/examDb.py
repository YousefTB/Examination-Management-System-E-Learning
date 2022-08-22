import sqlite3
import datetime

DB_FILENAME = 'Exam system db.db'


def questions_list(exam_id):
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.cursor()
    questions = cur.execute(
        "select q_name,ans1,ans2,ans3,ans4,correct_ans,q_deg,q_id from question where question.ex_id = ?", (exam_id,))
    questions = list(questions)
    cur.close()
    return questions


def scoring(exam_id, q_list, seq_of_ans, id):
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.cursor()
    total_mark = 0
    cnt = 0
    for ansr in seq_of_ans:
        if ansr[0] == ansr[2]:
            cur.execute("update student_question set deg = ? where stu_id = ? and q_id = ?",
                        (ansr[1], id, q_list[cnt][8]))
            total_mark += float(ansr[1])
        else:
            cur.execute("update student_question set deg = ? where stu_id = ? and q_id = ?",
                        (0, id, q_list[cnt][8]))
        cnt += 1

    cur.execute("update studentExam set status = 'The exam is done', stu_deg = ? where stu_id = ? and exam_id = ?",
                (total_mark, id, exam_id))
    conn.commit()
    cur.close()


def check_timing(exam_id):
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.cursor()
    fin_time = cur.execute(
        "select fin_time from exam where exam_id = ?", (exam_id,))
    fin_time = list(fin_time)
    fin_date = cur.execute(
        "select fin_dat from exam where exam_id = ?", (exam_id,))
    fin_date = list(fin_date)
    timing = datetime.datetime.now()
    time_now = timing.strftime("%H:%M")
    date_now = timing.strftime("%x")
    if date_now >= fin_date[0][0] and time_now > fin_time[0][0]:
        cur.close()
        return 1
    else:
        cur.close()
        return 0


def get_marks(exam_id, id):
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.cursor()
    res = cur.execute(
        "select q_name,correct_ans,ans,deg,q_deg from question,student_question where question.ex_id = ? and stu_id = ? and question.q_id = student_question.q_id", (exam_id, id))
    res = list(res)
    cur.close()
    return res


def get_total_marks(exam_id, id):
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.cursor()
    res = cur.execute(
        "select stu_deg,total_deg from studentExam,exam where stu_id = ? and studentExam.exam_id = ? and studentExam.exam_id = exam.exam_id", (id, exam_id))
    res = list(res)
    tot = [y for x in res for y in x]
    cur.close()
    return tot


def save_answers_into_db(question_num,seq_of_ans,id):
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.cursor()
    cur.execute("update student_question set ans = ? where stu_id = ? and q_id = ?",
                        (seq_of_ans[0], id, question_num))
    conn.commit()
    cur.close()

def retrieve_answers_from_db(exam_id,id):
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.cursor()
    res = cur.execute("select student_question.q_id,ans from student_question,question where student_question.stu_id = ? and question.ex_id = ? and student_question.q_id = question.q_id",(id,exam_id))
    res = list(res)
    answers = [x for x in res]
    cur.close()
    return answers