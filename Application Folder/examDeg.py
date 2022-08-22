# ----------------------
# Exam degrees Module
# ----------------------

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from examDb import *


def exame_degrees_frame(exam_id, id):
    # Create The exame window
    exame_degrees = Tk()
    exame_degrees.config(bg="#0066CC")

    # Change exame window title
    exame_degrees.title("Exam degrees page")

    # Make window icon
    icon = PhotoImage(file="exam.icon.png")
    exame_degrees.iconphoto(False, icon)

    # To make the window appear at the center of the screen

    def set_size(root, width, height):
        screen_width = root.winfo_screenwidth()
        secreem_height = root.winfo_screenheight()
        x = int((screen_width - width)/2)
        y = int((secreem_height-height)/2)
        root.geometry(f'{width}x{height}+{x}+{y}')

    # Set Dimensions
    # exame_degrees.geometry("1400x750")
    set_size(exame_degrees, 1400, 750)
    exame_degrees.resizable(False, False)

    # Create main frame
    frame = Frame(exame_degrees, width=1340, height=690, bg="White")
    frame.place(x=30, y=30)

    # Create table to show all quetions and their answers
    columns = ('question', 'correctans',
               'answer', 'q_deg', 'deg')

    tree = ttk.Treeview(frame, columns=columns,
                        show='headings', height=15)

    # define headings
    tree.heading('question', text='Question')
    tree.heading('correctans', text='Correct answer')
    tree.heading('answer', text='Your answer')
    tree.heading('q_deg', text='Your mark')
    tree.heading('deg', text='Question mark')

    # Create list of tuples for storing data to be displayed
    questions = get_marks(exam_id, id)

    # To show data in the table
    for q in questions:
        tree.insert('', END, values=q)

    # Table place
    tree.place(x=20, y=10, height=450, width=1300)

    # add a vertical scrollbar to the table
    scrollbar1 = ttk.Scrollbar(
        frame, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar1.set)
    scrollbar1.place(x=1320, y=10, height=450)

    # add a horizontal scrollbar
    scrollbar2 = ttk.Scrollbar(
        frame, orient=HORIZONTAL, command=tree.xview)
    tree.configure(xscrollcommand=scrollbar2.set)
    scrollbar2.place(x=15, y=450, height=20, width=1320)

    # Variables definition
    tot = get_total_marks(exam_id, id)
    total_degree = StringVar()
    your_degree = StringVar()
    total_degree.set(str(tot[1]))
    your_degree.set(str(tot[0]))

    # Labels definition
    total_deg_lbl = Label(frame, text="Total marks of the exam :",
                          height=2, font=("Arial", 15, 'bold'), bg="White")
    total_deg_lbl.place(x=20, y=480)

    total_deg_var_lbl = Label(frame, textvariable=total_degree,
                              height=2, font=("Arial", 15), bg="White")
    total_deg_var_lbl.place(x=290, y=482)

    deg_lbl = Label(frame, text="Your total marks in the exam :",
                    height=2, font=("Arial", 15, 'bold'), bg="White", fg="#CC0066")
    deg_lbl.place(x=20, y=520)

    deg_var_lbl = Label(frame, textvariable=your_degree,
                        height=2, font=("Arial", 15))
    deg_var_lbl.place(x=320, y=522)

    # Buttons functions

    def OK_end():
        messagebox.showinfo("Warning", "You will get into the main page")
        exame_degrees.destroy()
        import StudentWin
        StudentWin.student_module(id)

    # Buttons for back and next
    ok_btn = Button(frame, text="OK", width=14,
                    height=1, font=("Arial", 15), borderwidth=0, bg="#CC0066", fg="#FFFFFF", command=OK_end)
    ok_btn.place(x=585, y=630)

    # Run app infinitely
    exame_degrees.mainloop()
