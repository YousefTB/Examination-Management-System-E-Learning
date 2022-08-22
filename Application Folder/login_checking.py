import sqlite3

DB_FILENAME = 'Exam system db.db'


def check_login(id, type, password):
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.cursor()
    if type == "student":
        res = cur.execute(
            "select stu_num from student where stu_id = ?", (id,))
        res = list(res)
        cur.close()
        if len(res) == 0:
            return 0
        elif res[0][0] == password:
            return 1
    elif type == "examiner":
        res = cur.execute(
            "select examiner_num from examiner where examiner_id = ?", (id,))
        res = list(res)
        cur.close()
        if len(res) == 0:
            return 0
        elif res[0][0] == password:
            return 2
    elif type == "admin":
        res = cur.execute("select adm_num from admin where adm_id = ?", (id,))
        res = list(res)
        cur.close()
        if len(res) == 0:
            return 0
        elif res[0][0] == password:
            return 3
    else:
        return 0
