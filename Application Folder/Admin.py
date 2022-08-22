# ----------------------
# Admin Module
# ----------------------

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import Admindb as db
import login_window


def admin_module(adm_id):
    # Create The admin window
    admin = Tk()
    admin.config(bg="Blue")

    # Change admin window title
    admin.title("Admin main page")

    # Make window icon
    icon = PhotoImage(file="exam.icon.png")
    admin.iconphoto(False, icon)

    # To make the window appear at the center of the screen

    def set_size(root, width, height):
        screen_width = root.winfo_screenwidth()
        secreem_height = root.winfo_screenheight()
        x = int((screen_width - width)/2)
        y = int((secreem_height-height)/2)
        root.geometry(f'{width}x{height}+{x}+{y}')

    # Set Dimensions
    set_size(admin, 1200, 750)
    admin.resizable(False, False)

    # Create main frame
    frame1 = Frame(admin, width=300, height=750, bg="Blue")
    frame1.pack(side="left")

    # To import image
    img = ImageTk.PhotoImage(Image.open("mainframe.jpg"))

    # Create a Label Widget to display the text or Image
    label = Label(frame1, image=img)
    label.pack(side="left")

    # Create the second frame
    frame2 = Frame(admin, width=900, height=750, bg="White")
    frame2.pack(side="right")

    # Button functions

    def personframe():
        clear_frame()
        personal_information()

    def depframe():
        clear_frame()
        departments_frame()

    def examinerframe():
        clear_frame()
        examiners_frame()

    def studentframe():
        clear_frame()
        students_frame()

    def logout():
        admin.destroy()
        login_window.Login_win()

    # Create Buttons
    pesonal_infbtn = Button(frame1, text="Personal info", width=15, font=("Tahoma", 18),
                            height=1, borderwidth=0, bg="#FFFFFF", fg="Black", command=personframe).place(x=40, y=30)

    depbtn = Button(frame1, text="Departments", width=15, font=("Tahoma", 18),
                    height=1, borderwidth=0, bg="#FFFFFF", fg="Black", command=depframe).place(x=40, y=100)

    examinerbtn = Button(frame1, text="Examiners", width=15, font=("Tahoma", 18),
                         height=1, borderwidth=0, bg="#FFFFFF", fg="Black", command=examinerframe).place(x=40, y=170)

    studentbtn = Button(frame1, text="Students", width=15, font=("Tahoma", 18),
                        height=1, borderwidth=0, bg="#FFFFFF", fg="Black", command=studentframe).place(x=40, y=240)

    exitbtn = Button(frame1, text="Log out", width=15, font=("Tahoma", 18),
                     height=1, borderwidth=0, bg="#FF0099", fg="White", command=logout).place(x=40, y=650)

    # clear frame2 function

    def clear_frame():
        for widgets in frame2.winfo_children():
            widgets.destroy()
#############################################################################################################
    # Personal Informarion frame

    def personal_information():
        # Personal variables
        admin_name = StringVar()
        admin_id = StringVar()
        admin_gen = StringVar()
        admin_national_num = StringVar()
        admin_phone = StringVar()
        admin_email = StringVar()
        admin_address = StringVar()

        # Get personal info from database
        info = db.personInfo_admin(adm_id)
        admin_id.set(str(info[0]))
        admin_name.set(str(info[1]))
        admin_national_num.set(str(info[2]))
        admin_gen.set(str(info[3]))
        admin_email.set(str(info[4]))
        admin_address.set(str(info[5]))
        admin_phone.set(str(info[6]))

        # Indicator labels
        admin_name_lbl = Label(frame2, text="Name :",
                               height=2, font=("Tahoma", 18, 'bold'), bg="White").place(x=15, y=20)

        admin_name_var = Label(frame2, textvariable=admin_name,
                               height=2, font=("Tahoma", 16), bg="White").place(x=250, y=24)

        admin_id_lbl = Label(frame2, text="ID :",
                             height=2, font=("Tahoma", 18, 'bold'), bg="White").place(x=15, y=70)

        admin_id_var = Label(frame2, textvariable=admin_id,
                             height=2, font=("Tahoma", 16), bg="White").place(x=250, y=74)

        admin_gender_lbl = Label(frame2, text="Gender :",
                                 height=2, font=("Tahoma", 18, 'bold'), bg="White").place(x=15, y=130)

        admin_gender_var = Label(frame2, textvariable=admin_gen,
                                 height=2, font=("Tahoma", 16), bg="White").place(x=250, y=134)

        admin_national_number_lbl = Label(frame2, text="National number :",
                                          height=2, font=("Tahoma", 18, 'bold'), bg="White").place(x=15, y=180)

        admin_national_number_var = Label(frame2, textvariable=admin_national_num,
                                          height=2, font=("Tahoma", 16), bg="White").place(x=250, y=184)

        admin_phone_lbl = Label(frame2, text="Phone number :",
                                height=2, font=("Tahoma", 18, 'bold'), bg="White").place(x=15, y=230)

        admin_phone_var = Label(frame2, textvariable=admin_phone,
                                height=2, font=("Tahoma", 16), bg="White").place(x=250, y=234)

        admin_email_lbl = Label(frame2, text="Email :",
                                height=2, font=("Tahoma", 18, 'bold'), bg="White").place(x=15, y=280)

        admin_email_var = Label(frame2, textvariable=admin_email,
                                height=2, font=("Tahoma", 16), bg="White").place(x=250, y=284)

        admin_address_lbl = Label(frame2, text="Address :",
                                  height=2, font=("Tahoma", 18, 'bold'), bg="White").place(x=15, y=330)

        admin_address_var = Label(frame2, textvariable=admin_address,
                                  height=2, font=("Tahoma", 16), bg="White").place(x=250, y=334)

#############################################################################################################

    def departments_frame():
        columns = ('dep_id', 'dep_name')

        tree = ttk.Treeview(frame2, columns=columns,
                            show='headings', height=15)

        # define headings
        tree.heading('dep_id', text='Department ID')
        tree.heading('dep_name', text='Department name')

        # To show data in the table

        def show_dep(tree):
            dep_data = db.get_all_dep()
            tree.delete(*tree.get_children())
            for dep in dep_data:
                tree.insert('', END, values=dep)

        show_dep(tree)

        # Select function
        def item_selected(event):
            selected_item = tree.selection()
            item = tree.item(selected_item)
            record = item['values']
            Dep_id.set(record[0])
            Dep_name.set(record[1])

        tree.bind('<<TreeviewSelect>>', item_selected)

        # Table place
        tree.place(x=150, y=10, height=350, width=600)

        # add a scrollbar to the table
        scrollbar = ttk.Scrollbar(frame2, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.place(x=750, y=10, height=350)

        # Add labels
        depID_lbl = Label(frame2, text="Department ID :",
                          font=("Tahoma", 16, "bold"), height=2, bg="White")
        depID_lbl.place(x=25, y=375)

        depName_lbl = Label(frame2, text="Department name :",
                            font=("Tahoma", 16, "bold"), height=2, bg="White")
        depName_lbl.place(x=25, y=425)

        # Variables that hold dep name and id
        Dep_id = StringVar()
        Dep_name = StringVar()

        # Entries decleration
        Dep_id_var_label = Label(frame2, textvariable=Dep_id,
                                 font=("Tahoma", 15), height=2, bg="White")
        Dep_id_var_label.place(x=240, y=375)

        Dep_name_entry = Entry(frame2, width=40, font=(
            "Tahoma", 15), textvariable=Dep_name, border=2)
        Dep_name_entry.place(x=240, y=440)

        # To clear Entry and variable lable

        def clear():
            Dep_id.set("")
            Dep_name.set("")

        # Buttons functions
        def insert_dep():
            try:
                db.add_dep(Dep_name.get())
                messagebox.showinfo("Successful process",
                                    "Inserted successfully")
                show_dep(tree)
                clear()
            except:
                messagebox.showerror("Failed process", "Please try again")

        def update_dep():
            try:
                db.update_dep(int(Dep_id.get()), Dep_name.get())
                messagebox.showinfo("Successful process",
                                    "Updated successfully")
                show_dep(tree)
                clear()
            except:
                messagebox.showerror("Failed process", "Please try again")

        def delete_dep():
            try:
                db.delete_dep(int(Dep_id.get()))
                messagebox.showinfo("Successful process",
                                    "Deleted successfully")
                show_dep(tree)
                clear()
            except:
                messagebox.showerror("Failed process", "Please try again")

        # Add function buttons
        insert_btn = Button(frame2, text="Insert", width=12,
                            height=1, font=("Arial", 14), borderwidth=0, bg="#FF0099", fg="White", command=insert_dep)
        insert_btn.place(x=400, y=700)

        update_btn = Button(frame2, text="Update", width=12,
                            height=1, font=("Arial", 14), borderwidth=0, bg="#FF0099", fg="White", command=update_dep)
        update_btn.place(x=550, y=700)

        delete_btn = Button(frame2, text="Delete", width=12,
                            height=1, font=("Arial", 14), borderwidth=0, bg="#FF0099", fg="White", command=delete_dep)
        delete_btn.place(x=700, y=700)

#############################################################################################################

    def examiners_frame():
        columns = ('ex_id', 'ex_name', 'nation_num',
                   'gen', 'email_add', 'phone', 'dep_name')

        tree2 = ttk.Treeview(frame2, columns=columns,
                             show='headings', height=15)

        # define headings
        tree2.heading('ex_id', text='ID')
        tree2.heading('ex_name', text='Name')
        tree2.heading('nation_num', text='National num')
        tree2.heading('email_add', text='Email')
        tree2.heading('phone', text='Phone')
        tree2.heading('gen', text='Gender')
        tree2.heading('dep_name', text='Department')

        # To show data in the table in the begining
        def show_examiners(tree2):
            examiners_data = db.get_examiners()
            tree2.delete(*tree2.get_children())
            for e in examiners_data:
                tree2.insert('', END, values=e)

        show_examiners(tree2)

        # To show examiners with a particular department
        def show_examiners_with_particular_dep(tree2, department_id):
            examiners_data = db.get_examiners_with_particular_dep(
                department_id)
            tree2.delete(*tree2.get_children())
            for e in examiners_data:
                tree2.insert('', END, values=e)

        # Select function
        def item_selected(event):
            selected_item = tree2.selection()
            item = tree2.item(selected_item)
            record = item['values']
            examiner_id.set(record[0])
            examiner_name.set(record[1])
            examiner_nationnum.set(record[2])
            examiner_gen.set(record[3])
            if examiner_gen.get() == "Male":
                M_rb.select()
            else:
                F_rb.select()
            examiner_email.set(record[4])
            examiner_phone.set(record[5])
            examiner_dep.set(record[6])

        tree2.bind('<<TreeviewSelect>>', item_selected)

        # Table place
        tree2.place(x=50, y=10, height=350, width=800)

        # add a vertical scrollbar to the table
        scrollbar2 = ttk.Scrollbar(
            frame2, orient=VERTICAL, command=tree2.yview)
        tree2.configure(yscroll=scrollbar2.set)
        scrollbar2.place(x=850, y=10, height=350)

        # add a horizontal scrollbar
        scrollbar3 = ttk.Scrollbar(
            frame2, orient=HORIZONTAL, command=tree2.xview)
        tree2.configure(xscrollcommand=scrollbar3.set)
        scrollbar3.place(x=50, y=355, height=20, width=800)

        # Add labels
        examinerID_lbl = Label(frame2, text="Examiner id :",
                               font=("Tahoma", 16, "bold"), height=2, bg="White")
        examinerID_lbl.place(x=25, y=375)

        examinerName_lbl = Label(frame2, text="Examiner name :",
                                 font=("Tahoma", 16, "bold"), height=2, bg="White")
        examinerName_lbl.place(x=25, y=425)

        examinerdep_lbl = Label(frame2, text="Department :",
                                font=("Tahoma", 16, "bold"), height=2, bg="White")
        examinerdep_lbl.place(x=25, y=475)

        examineremail_lbl = Label(frame2, text="Email :",
                                  font=("Tahoma", 16, "bold"), height=2, bg="White")
        examineremail_lbl.place(x=25, y=525)

        examinerphone_lbl = Label(frame2, text="Phone num :",
                                  font=("Tahoma", 16, "bold"), height=2, bg="White")
        examinerphone_lbl.place(x=25, y=575)

        examinernationalnum_lbl = Label(frame2, text="National num :",
                                        font=("Tahoma", 16, "bold"), height=2, bg="White")
        examinernationalnum_lbl.place(x=25, y=625)

        examinergen_lbl = Label(frame2, text="Gender :",
                                font=("Tahoma", 16, "bold"), height=2, bg="White")
        examinergen_lbl.place(x=25, y=675)

        # Variables that hold examiners values
        examiner_id = StringVar()
        examiner_name = StringVar()
        examiner_dep = StringVar()
        examiner_email = StringVar()
        examiner_phone = StringVar()
        examiner_nationnum = StringVar()
        examiner_gen = StringVar()
        gen = IntVar()

        # places to show and write examiners data
        examiner_id_var_label = Label(frame2, textvariable=examiner_id,
                                      font=("Tahoma", 15), height=2, bg="White")
        examiner_id_var_label.place(x=240, y=375)

        examiner_name_entry = Entry(frame2, width=40, font=(
            "Tahoma", 15), textvariable=examiner_name, border=2)
        examiner_name_entry.place(x=240, y=440)

        examiner_email_entry = Entry(frame2, width=40, font=(
            "Tahoma", 15), textvariable=examiner_email, border=2)
        examiner_email_entry.place(x=240, y=540)

        examiner_phone_entry = Entry(frame2, width=40, font=(
            "Tahoma", 15), textvariable=examiner_phone, border=2)
        examiner_phone_entry.place(x=240, y=590)

        examiner_nationnum_entry = Entry(frame2, width=40, font=(
            "Tahoma", 15), textvariable=examiner_nationnum, border=2)
        examiner_nationnum_entry.place(x=240, y=640)

        def selected_Male():
            examiner_gen.set("Male")

        def selected_Female():
            examiner_gen.set("Female")

        M_rb = Radiobutton(frame2, text="Male", variable=gen,
                           value=1, font=("Arial", 14), command=selected_Male, bg="White")
        M_rb.place(x=220, y=680)

        F_rb = Radiobutton(frame2, text="Female", variable=gen,
                           value=2, font=("Arial", 14), command=selected_Female, bg="White")
        F_rb.place(x=290, y=680)

        dep_cbx = ttk.Combobox(frame2, width=40, textvariable=examiner_dep, font=(
            "Tahoma", 15), background="White")

        # Create a list to store combo box elemennts
        department_list = []
        department_dic = {}
        db.get_all_depV2(department_list, department_dic)
        dep_cbx['values'] = department_list
        dep_cbx['state'] = 'readonly'
        dep_cbx.bind("<<ComboboxSelected>>", lambda _: show_examiners_with_particular_dep(
            tree2, department_dic[examiner_dep.get()]))
        dep_cbx.place(x=240, y=490)

        # To clear entries
        def clear():
            examiner_id.set("")
            examiner_name.set("")
            examiner_nationnum.set("")
            examiner_email.set("")
            examiner_phone.set("")

        # Buttons functions
        def insert_examiner():
            try:
                db.add_examiner(examiner_name.get(), int(examiner_nationnum.get()), examiner_gen.get(
                ), examiner_email.get(), examiner_phone.get(), department_dic[examiner_dep.get()])
                messagebox.showinfo("Successful process",
                                    "Inserted successfully")
                show_examiners_with_particular_dep(
                    tree2, department_dic[examiner_dep.get()])
                clear()

            except:
                messagebox.showerror("Failed process", "Please try again")

        def update_examiner():
            try:
                db.Update_examiner(int(examiner_id.get()), examiner_name.get(), int(examiner_nationnum.get()), examiner_gen.get(
                ), examiner_email.get(), examiner_phone.get(), department_dic[examiner_dep.get()])
                messagebox.showinfo("Successful process",
                                    "Updated successfully")
                show_examiners_with_particular_dep(
                    tree2, department_dic[examiner_dep.get()])
                clear()

            except:
                messagebox.showerror("Failed process", "Please try again")

        def delete_examiner():
            try:
                db.delete_examiner(int(examiner_id.get()))
                messagebox.showinfo("Successful process",
                                    "Deleted successfully")
                show_examiners_with_particular_dep(
                    tree2, department_dic[examiner_dep.get()])
                clear()

            except:
                messagebox.showerror("Failed process", "Please try again")

        # Add function buttons
        insert_examiner_btn = Button(frame2, text="Insert", width=12,
                                     height=1, font=("Arial", 14), borderwidth=0, bg="#FF0099", fg="White", command=insert_examiner)
        insert_examiner_btn.place(x=400, y=700)

        update_examiner_btn = Button(frame2, text="Update", width=12,
                                     height=1, font=("Arial", 14), borderwidth=0, bg="#FF0099", fg="White", command=update_examiner)
        update_examiner_btn.place(x=550, y=700)

        delete_examiner_btn = Button(frame2, text="Delete", width=12,
                                     height=1, font=("Arial", 14), borderwidth=0, bg="#FF0099", fg="White", command=delete_examiner)
        delete_examiner_btn.place(x=700, y=700)

    #########################################################################################################

    def students_frame():
        columns = ('st_id', 'st_name', 'st_nation_num',
                   'st_gen', 'st_email_add', 'st_phone', 'st_dep_name')

        tree3 = ttk.Treeview(frame2, columns=columns,
                             show='headings', height=15)

        # define headings
        tree3.heading('st_id', text='ID')
        tree3.heading('st_name', text='Name')
        tree3.heading('st_nation_num', text='National num')
        tree3.heading('st_email_add', text='Email')
        tree3.heading('st_phone', text='Phone')
        tree3.heading('st_gen', text='Gender')
        tree3.heading('st_dep_name', text='Department')

        # To show students data
        def show_students(tree3):
            students_data = db.get_students()
            tree3.delete(*tree3.get_children())
            for s in students_data:
                tree3.insert('', END, values=s)

        show_students(tree3)

        # To show students data with particular department
        def show_students_with_particular_dep(tree3, department_id):
            students_data = db.get_students_with_particular_dep(department_id)
            tree3.delete(*tree3.get_children())
            for s in students_data:
                tree3.insert('', END, values=s)

        # Select function

        def item_selected(event):
            selected_item = tree3.selection()
            item = tree3.item(selected_item)
            record = item['values']
            student_id.set(record[0])
            student_name.set(record[1])
            student_nationnum.set(record[2])
            student_gen.set(record[3])
            if student_gen.get() == "Male":
                M_rb.select()
            else:
                F_rb.select()
            student_email.set(record[4])
            student_phone.set(record[5])
            student_dep.set(record[6])

        tree3.bind('<<TreeviewSelect>>', item_selected)

        # Table place
        tree3.place(x=50, y=10, height=350, width=800)

        # add a vertical scrollbar to the table
        scrollbar4 = ttk.Scrollbar(
            frame2, orient=VERTICAL, command=tree3.yview)
        tree3.configure(yscroll=scrollbar4.set)
        scrollbar4.place(x=850, y=10, height=350)

        # add a horizontal scrollbar
        scrollbar5 = ttk.Scrollbar(
            frame2, orient=HORIZONTAL, command=tree3.xview)
        tree3.configure(xscrollcommand=scrollbar5.set)
        scrollbar5.place(x=50, y=355, height=20, width=800)

        # Add labels
        studentID_lbl = Label(frame2, text="Student id :",
                              font=("Tahoma", 16, "bold"), height=2, bg="White")
        studentID_lbl.place(x=25, y=375)

        studentName_lbl = Label(frame2, text="Student name :",
                                font=("Tahoma", 16, "bold"), height=2, bg="White")
        studentName_lbl.place(x=25, y=425)

        studentdep_lbl = Label(frame2, text="Department :",
                               font=("Tahoma", 16, "bold"), height=2, bg="White")
        studentdep_lbl.place(x=25, y=475)

        studentemail_lbl = Label(frame2, text="Email :",
                                 font=("Tahoma", 16, "bold"), height=2, bg="White")
        studentemail_lbl.place(x=25, y=525)

        studentphone_lbl = Label(frame2, text="Phone num :",
                                 font=("Tahoma", 16, "bold"), height=2, bg="White")
        studentphone_lbl.place(x=25, y=575)

        studentnationalnum_lbl = Label(frame2, text="National num :",
                                       font=("Tahoma", 16, "bold"), height=2, bg="White")
        studentnationalnum_lbl.place(x=25, y=625)

        studentgen_lbl = Label(frame2, text="Gender :",
                               font=("Tahoma", 16, "bold"), height=2, bg="White")
        studentgen_lbl.place(x=25, y=675)

        # Variables that hold student values
        student_id = StringVar()
        student_name = StringVar()
        student_dep = StringVar()
        student_email = StringVar()
        student_phone = StringVar()
        student_nationnum = StringVar()
        student_gen = StringVar()
        gen = IntVar()

        # places to show and write students data
        student_id_var_label = Label(frame2, textvariable=student_id,
                                     font=("Tahoma", 15), height=2, bg="White")
        student_id_var_label.place(x=240, y=375)

        student_name_entry = Entry(frame2, width=40, font=(
            "Tahoma", 15), textvariable=student_name, border=2)
        student_name_entry.place(x=240, y=440)

        student_email_entry = Entry(frame2, width=40, font=(
            "Tahoma", 15), textvariable=student_email, border=2)
        student_email_entry.place(x=240, y=540)

        student_phone_entry = Entry(frame2, width=40, font=(
            "Tahoma", 15), textvariable=student_phone, border=2)
        student_phone_entry.place(x=240, y=590)

        student_nationnum_entry = Entry(frame2, width=40, font=(
            "Tahoma", 15), textvariable=student_nationnum, border=2)
        student_nationnum_entry.place(x=240, y=640)

        def selected_Male():
            student_gen.set("Male")

        def selected_Female():
            student_gen.set("Female")

        M_rb = Radiobutton(frame2, text="Male", variable=gen,
                           value=1, font=("Arial", 14), command=selected_Male, bg="White")
        M_rb.place(x=220, y=680)

        F_rb = Radiobutton(frame2, text="Female", variable=gen,
                           value=2, font=("Arial", 14), command=selected_Female, bg="White")
        F_rb.place(x=290, y=680)

        dep_cbx = ttk.Combobox(frame2, width=40, textvariable=student_dep, font=(
            "Tahoma", 15), background="White")

        # Create a list to store combo box elemennts
        department_list = []
        department_dic = {}
        db.get_all_depV2(department_list, department_dic)
        dep_cbx['values'] = department_list
        dep_cbx['state'] = 'readonly'
        dep_cbx.bind("<<ComboboxSelected>>", lambda _: show_students_with_particular_dep(
            tree3, department_dic[student_dep.get()]))
        dep_cbx.place(x=240, y=490)

        # Function to clear entries

        def clear():
            student_id.set("")
            student_email.set("")
            student_phone.set("")
            student_name.set("")
            student_nationnum.set("")

        # Buttons functions

        def insert_student():
            try:
                db.add_student(student_name.get(), int(student_nationnum.get()), student_gen.get(
                ), student_email.get(), student_phone.get(), department_dic[student_dep.get()])
                messagebox.showinfo("Successful process",
                                    "Inserted successfully")
                show_students_with_particular_dep(
                    tree3, department_dic[student_dep.get()])
                clear()

            except:
                messagebox.showerror("Failed process", "Please try again")

        def update_student():
            try:
                db.Update_student(int(student_id.get()), student_name.get(), int(student_nationnum.get()), student_gen.get(
                ), student_email.get(), student_phone.get(), department_dic[student_dep.get()])
                messagebox.showinfo("Successful process",
                                    "Updated successfully")
                show_students_with_particular_dep(
                    tree3, department_dic[student_dep.get()])
                clear()

            except:
                messagebox.showerror("Failed process", "Please try again")

        def delete_student():
            try:
                db.delete_student(int(student_id.get()))
                messagebox.showinfo("Successful process",
                                    "Deleted successfully")
                show_students_with_particular_dep(
                    tree3, department_dic[student_dep.get()])
                clear()

            except:
                messagebox.showerror("Failed process", "Please try again")

        # Add function buttons
        insert_student_btn = Button(frame2, text="Insert", width=12,
                                    height=1, font=("Arial", 14), borderwidth=0, bg="#FF0099", fg="White", command=insert_student)
        insert_student_btn.place(x=400, y=700)

        update_student_btn = Button(frame2, text="Update", width=12,
                                    height=1, font=("Arial", 14), borderwidth=0, bg="#FF0099", fg="White", command=update_student)
        update_student_btn.place(x=550, y=700)

        delete_student_btn = Button(frame2, text="Delete", width=12,
                                    height=1, font=("Arial", 14), borderwidth=0, bg="#FF0099", fg="White", command=delete_student)
        delete_student_btn.place(x=700, y=700)

    # Run app infinitely
    admin.mainloop()


# admin_module(1)
