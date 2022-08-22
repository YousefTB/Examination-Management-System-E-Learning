# ----------------------
# Student Module
# ----------------------

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import *
from PIL import ImageTk, Image
from StudentDb import *
from examWin import exame_frame
import login_window


def student_module(id):
    # Create The student window
    student = Tk()
    student.config(bg="Blue")

    # Change student window title
    student.title("Student main page")

    # Make window icon
    icon = PhotoImage(file="exam.icon.png")
    student.iconphoto(False, icon)

    # To make the window appear at the center of the screen

    def set_size(root, width, height):
        screen_width = root.winfo_screenwidth()
        secreem_height = root.winfo_screenheight()
        x = int((screen_width - width)/2)
        y = int((secreem_height-height)/2)
        root.geometry(f'{width}x{height}+{x}+{y}')

    # Set Dimensions
    set_size(student, 1200, 750)
    student.resizable(False, False)

    # Create main frame
    frame1 = Frame(student, width=300, height=750, bg="Blue")
    frame1.pack(side="left")

    # To import image
    img = ImageTk.PhotoImage(Image.open("mainframe.jpg"))

    # Create a Label Widget to display the text or Image
    label = Label(frame1, image=img)
    label.pack(side="left")

    # Create the second frame
    frame2 = Frame(student, width=900, height=750, bg="White")
    frame2.pack(side="right")

    # Button functions

    def personframe():
        clear_frame()
        personal_information()

    def examesFrame():
        clear_frame()
        exames_frame()

    def logout():
        student.destroy()
        login_window.Login_win()

    # Create Buttons
    pesonal_infbtn = Button(frame1, text="Personal info", width=15, font=("Tahoma", 18),
                            height=1, borderwidth=0, bg="#FFFFFF", fg="Black", command=personframe).place(x=40, y=30)

    examesbtn = Button(frame1, text="Exams", width=15, font=("Tahoma", 18),
                       height=1, borderwidth=0, bg="#FFFFFF", fg="Black", command=examesFrame).place(x=40, y=100)

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
        # getting the information using the ID of the student
        stu_inf = student_information(id)
        student_name = StringVar()
        student_name.set(stu_inf[1])
        student_id = StringVar()
        student_id.set(stu_inf[0])
        student_gen = StringVar()
        student_gen.set(stu_inf[3])
        student_national_num = StringVar()
        student_national_num.set(str(int(stu_inf[2])))
        student_phone = StringVar()
        student_phone.set(stu_inf[5])
        student_email = StringVar()
        student_email.set(stu_inf[4])
        student_dep = StringVar()
        student_dep.set(stu_inf[6])

        # Indicator labels
        student_name_lbl = Label(frame2, text="Name :",
                                 height=2, font=("Tahoma", 18, 'bold'), bg="White").place(x=15, y=20)

        student_name_var = Label(frame2, textvariable=student_name,
                                 height=2, font=("Tahoma", 16), bg="White").place(x=250, y=24)

        student_id_lbl = Label(frame2, text="ID :",
                               height=2, font=("Tahoma", 18, 'bold'), bg="White").place(x=15, y=70)

        student_id_var = Label(frame2, textvariable=student_id,
                               height=2, font=("Tahoma", 16), bg="White").place(x=250, y=74)

        student_gender_lbl = Label(frame2, text="Gender :",
                                   height=2, font=("Tahoma", 18, 'bold'), bg="White").place(x=15, y=130)

        student_gender_var = Label(frame2, textvariable=student_gen,
                                   height=2, font=("Tahoma", 16), bg="White").place(x=250, y=134)

        student_national_number_lbl = Label(frame2, text="National number :",
                                            height=2, font=("Tahoma", 18, 'bold'), bg="White").place(x=15, y=180)

        student_national_number_var = Label(frame2, textvariable=student_national_num,
                                            height=2, font=("Tahoma", 16), bg="White").place(x=250, y=184)

        student_phone_lbl = Label(frame2, text="Phone number :",
                                  height=2, font=("Tahoma", 18, 'bold'), bg="White").place(x=15, y=230)

        student_phone_var = Label(frame2, textvariable=student_phone,
                                  height=2, font=("Tahoma", 16), bg="White").place(x=250, y=234)

        student_email_lbl = Label(frame2, text="Email :",
                                  height=2, font=("Tahoma", 18, 'bold'), bg="White").place(x=15, y=280)

        student_email_var = Label(frame2, textvariable=student_email,
                                  height=2, font=("Tahoma", 16), bg="White").place(x=250, y=284)

        student_dep_lbl = Label(frame2, text="Department :",
                                height=2, font=("Tahoma", 18, 'bold'), bg="White").place(x=15, y=330)

        student_dep_var = Label(frame2, textvariable=student_dep,
                                height=2, font=("Tahoma", 16), bg="White").place(x=250, y=334)

#############################################################################################################

    def exames_frame():
        #  Exam id variable definition
        exam_id = StringVar()

        columns = ('ex_id', 'ex_name', 'beg_dat',
                   'beg_time', 'fin_dat', 'fin_time', 'total_deg', 'status', 'your_deg')

        tree = ttk.Treeview(frame2, columns=columns,
                            show='headings', height=15)

        # define headings
        tree.heading('ex_id', text='Exam id')
        tree.heading('ex_name', text='Exam name')
        tree.heading('beg_dat', text='Beginning date')
        tree.heading('beg_time', text='Beginning time')
        tree.heading('fin_dat', text='Finish Date')
        tree.heading('fin_time', text='Finish Time')
        tree.heading('total_deg', text='Total degree')
        tree.heading('status', text='Status')
        tree.heading('your_deg', text='Your degree')

        # Create list of tuples for storing data to be displayed
        # getting all Exams on the student by his ID
        exames = student_exams(id)

        # Sorting the existed exams based on the beggining date and time
        for i in range(len(exames) - 1):
            for j in range(i + 1, len(exames)):
                if exames[i][2] < exames[j][2]:
                    exames[i], exames[j] = exames[j], exames[i]
                elif exames[i][2] == exames[j][2] and exames[i][3] > exames[j][3]:
                    exames[i], exames[j] = exames[j], exames[i]

        # To show data in the table
        for e in exames:
            tree.insert('', END, values=e)

        # Table place
        tree.place(x=50, y=10, height=350, width=800)

        # Select function
        def item_selected(event):
            selected_item = tree.selection()
            item = tree.item(selected_item)
            record = item['values']
            exam_id.set(record[0])

        tree.bind('<<TreeviewSelect>>', item_selected)

        # add a vertical scrollbar to the table
        scrollbar = ttk.Scrollbar(frame2, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.place(x=850, y=10, height=350)

        # add a horizontal scrollbar
        scrollbar3 = ttk.Scrollbar(
            frame2, orient=HORIZONTAL, command=tree.xview)
        tree.configure(xscrollcommand=scrollbar3.set)
        scrollbar3.place(x=50, y=360, height=20, width=800)

        # Exam button function

        def select():
            try:
                if exam_validation(exam_id.get(), id):
                    answer = askyesno(
                        title="Confirmation", message="Are you sure to begin your exam ?")
                    if answer:
                        messagebox.showinfo(
                            "Warning", "You are about to start the exam\nSubmit before the Finish Time")

                        student.destroy()
                        exame_frame(exam_id.get(), id)
            except:
                messagebox.showerror("Warning", "Choose a valid exam to take")

        # Exam button decleration
        select_exam_btn = Button(frame2, text="Select exam", width=14,
                                 height=2, font=("Arial", 16, 'bold'), borderwidth=0, bg="#CC0066", fg="#FFFFFF", command=select)
        select_exam_btn.place(x=345, y=480)

    student.mainloop()
