# ----------------------
# database functions Module
# ----------------------

import sqlite3

DB_FILENAME = 'Exam system db.db'


################## Departments field ######################
def get_all_dep():
    conn = sqlite3.connect(DB_FILENAME)
    res = conn.execute("select * from department")
    res = list(res)
    conn.close()
    return res


def add_dep(dep_name):
    conn = sqlite3.connect(DB_FILENAME)
    conn.execute(
        f"insert into department (dep_name) values ('{dep_name}')")
    conn.commit()
    conn.close()


def update_dep(dep_id, dep_name):
    conn = sqlite3.connect(DB_FILENAME)
    conn.execute(
        f"update department set dep_name = '{dep_name}' where dep_id = '{dep_id}'")
    conn.commit()
    conn.close()


def delete_dep(dep_id):
    conn = sqlite3.connect(DB_FILENAME)
    conn.execute(
        f"delete from department  where dep_id = '{dep_id}'")
    conn.commit()
    conn.close()


################## Admin field ######################
def add_admin(adm_name, adm_num, adm_gen, adm_email, adm_address, adm_phone):
    conn = sqlite3.connect(DB_FILENAME)
    conn.execute(
        f"""
        insert into admin (adm_name, adm_num, adm_gen, adm_email, adm_address,adm_phone) 
        values ('{adm_name}','{adm_num}','{adm_gen}','{adm_email}','{adm_address}','{adm_phone}')
        """)
    conn.commit()
    conn.close()

# add_admin("Yousef Elbaroudy tark", "12365478952", "Male",
#         "Elbaroudy@yahooo", "Tanta", "01207051837")


def personInfo_admin(adm_id):
    conn = sqlite3.connect(DB_FILENAME)
    res = conn.execute(f'select * from admin where adm_id = {adm_id}')
    res = list(res)
    conn.close()
    return res[0]


################## examiners field ######################
def get_examiners():
    conn = sqlite3.connect(DB_FILENAME)
    res = conn.execute(
        """
        select examiner.examiner_id, examiner.examiner_name, examiner.examiner_num
        , examiner.examiner_gen, examiner.examiner_email, examiner.examiner_phone, department.dep_name 
        from examiner, department 
        where examiner.dep_id = department.dep_id order by examiner.dep_id, examiner.examiner_name
        """)
    res = list(res)
    conn.close()
    return res


def get_examiners_with_particular_dep(dep_id):
    conn = sqlite3.connect(DB_FILENAME)
    res = conn.execute(
        f"""
        select examiner.examiner_id, examiner.examiner_name, examiner.examiner_num
        , examiner.examiner_gen, examiner.examiner_email, examiner.examiner_phone, department.dep_name 
        from examiner, department 
        where examiner.dep_id = department.dep_id and examiner.dep_id = {dep_id} order by examiner.dep_id, examiner.examiner_name
        """)
    res = list(res)
    conn.close()
    return res


def Update_examiner(id, name, num, gen, email, phone, dep_id):
    conn = sqlite3.connect(DB_FILENAME)
    conn.execute(
        f"""
        update examiner set examiner_name = '{name}' , examiner_num = {num}, examiner_gen = '{gen}'
        , examiner_email = '{email}', examiner_phone = '{phone}', dep_id = {dep_id}
        where examiner_id = {id}
        """)
    conn.commit()
    conn.close()


# For using the combo box
def get_all_depV2(dep_in_list, dep_in_dic):
    conn = sqlite3.connect(DB_FILENAME)
    res = conn.execute("select * from department")
    res = list(res)
    conn.close()
    for dep in res:
        dep_in_list.append(dep[1])

    for dep in res:
        dep_in_dic[dep[1]] = dep[0]


def add_examiner(name, num, gen, email, phone, dep_id):
    conn = sqlite3.connect(DB_FILENAME)
    conn.execute(
        f"""
        insert into examiner (examiner_name, examiner_num, examiner_gen, examiner_email, examiner_phone, dep_id) 
        values ('{name}', {num},'{gen}','{email}','{phone}',{dep_id})
        """)
    conn.commit()
    conn.close()


#Update_examiner(4, "Huda Moharm", 87465154, "Female","Yousssef@yahoo.com", "0155478965", 5)

def delete_examiner(id):
    conn = sqlite3.connect(DB_FILENAME)
    conn.execute(
        f"delete from examiner  where examiner_id = {id}")
    conn.commit()
    conn.close()


################## Students field ######################
def get_students():
    conn = sqlite3.connect(DB_FILENAME)
    res = conn.execute(
        """
        select student.stu_id, student.stu_name, student.stu_num
        , student.stu_gen, student.stu_email, student.stu_phone, department.dep_name 
        from student, department 
        where student.dep_id = department.dep_id order by student.dep_id, student.stu_name
        """)
    res = list(res)
    conn.close()
    return res


def get_students_with_particular_dep(dep_id):
    conn = sqlite3.connect(DB_FILENAME)
    res = conn.execute(
        f"""
        select student.stu_id, student.stu_name, student.stu_num
        , student.stu_gen, student.stu_email, student.stu_phone, department.dep_name 
        from student, department 
        where student.dep_id = department.dep_id and student.dep_id = {dep_id} order by student.dep_id, student.stu_name
        """)
    res = list(res)
    conn.close()
    return res


def Update_student(id, name, num, gen, email, phone, dep_id):
    conn = sqlite3.connect(DB_FILENAME)
    conn.execute(
        f"""
        update student set stu_name = '{name}' , stu_num = {num}, stu_gen = '{gen}'
        , stu_email = '{email}', stu_phone = '{phone}', dep_id = {dep_id}
        where stu_id = {id}
        """)
    conn.commit()
    conn.close()


def add_student(name, num, gen, email, phone, dep_id):
    conn = sqlite3.connect(DB_FILENAME)
    conn.execute(
        f"""
        insert into student (stu_name, stu_num, stu_gen, stu_email, stu_phone, dep_id) 
        values ('{name}', {num},'{gen}','{email}','{phone}',{dep_id})
        """)
    conn.commit()
    conn.close()


def delete_student(id):
    conn = sqlite3.connect(DB_FILENAME)
    conn.execute(
        f"delete from student  where stu_id = {id}")
    conn.commit()
    conn.close()


#Update_student(1, "Yahya Hamza", 54821, "Male", "yahoo.com", "0124578", 4)
# print(get_students_with_particular_dep(4))
