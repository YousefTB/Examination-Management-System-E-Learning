# ----------------------
# Reviewing exam Module
# ----------------------

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import askyesno
from examDb import *
from examDeg import exame_degrees_frame
from goneQuestion import gone_question_frame


def exame_review_frame(exam_id, q_list, seq_of_ans, id):
    # Create The exame window
    exame_review = Tk()
    exame_review.config(bg="#0066CC")

    # Change exame window title
    exame_review.title("Exam review page")

    # Make window icon
    icon = PhotoImage(file="exam.icon.png")
    exame_review.iconphoto(False, icon)

    # To make the window appear at the center of the screen

    def set_size(root, width, height):
        screen_width = root.winfo_screenwidth()
        secreem_height = root.winfo_screenheight()
        x = int((screen_width - width)/2)
        y = int((secreem_height-height)/2)
        root.geometry(f'{width}x{height}+{x}+{y}')

    # Set Dimensions
    # exame_review.geometry("1400x750")
    set_size(exame_review, 1400, 750)
    exame_review.resizable(False, False)

    # Create main frame
    frame = Frame(exame_review, width=1340, height=690, bg="White")
    frame.place(x=30, y=30)

    # Create table to show all quetions and their answers
    columns = ('q_id', 'question', 'answ1',
               'answ2', 'answ3', 'answ4', 'answer', 'q_deg')

    tree = ttk.Treeview(frame, columns=columns,
                        show='headings', height=15)

    # define headings
    tree.heading('q_id', text='question number')
    tree.heading('question', text='question')
    tree.heading('answ1', text='1st choice')
    tree.heading('answ2', text='2nd choice')
    tree.heading('answ3', text='3rd choice')
    tree.heading('answ4', text='4th choice')
    tree.heading('answer', text='Your answer')
    tree.heading('q_deg', text='degree')

    # Create list of tuples for storing data to be displayed
    ques_id = StringVar()
    questions = []
    temb_list = []
    i = 0
    for e in q_list:
        temb_list.append(list(e)[:6])
        temb_list[i].append(seq_of_ans[i][0])
        temb_list[i].append(float(seq_of_ans[i][1]))
        questions.append(tuple(temb_list[i]))
        i += 1

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

    # Select function
    def item_selected(event):
        selected_item = tree.selection()
        item = tree.item(selected_item)
        record = item['values']
        ques_id.set(record[0])

    tree.bind('<<TreeviewSelect>>', item_selected)

    # Buttons functions
    def submit_exam():
        answer = askyesno(title="Confirmation",
                          message="Are you sure to submit your exam ?")
        if answer:
            if not(check_timing(exam_id)):
                scoring(exam_id, q_list, seq_of_ans, id)
                exame_review.destroy()
                exame_degrees_frame(exam_id, id)
            else:
                scoring(exam_id, [], [], id)
                messagebox.showerror(
                    "Exam", "The exam is ran out of time\nbefore your submission")
                messagebox.showinfo(
                    "Warning", "You will get into the main page")
                exame_review.destroy()
                import StudentWin
                StudentWin.student_module(id)

    def go_question():
        if ques_id.get() != "":
            exame_review.destroy()
            gone_question_frame(exam_id, q_list, seq_of_ans,
                                id, int(ques_id.get()))
        else:
            messagebox.showerror("Warning", "Choose a valid question to go")

    # Buttons for back and next

    submit_btn = Button(frame, text="Submit", width=12,
                        height=1, font=("Arial", 14), borderwidth=0, bg="#FF0099", fg="White", command=submit_exam)
    submit_btn.place(x=1100, y=630)

    go_to_btn = Button(frame, text="Go to question", width=14,
                       height=1, font=("Arial", 15), borderwidth=0, bg="#CC0066", fg="#FFFFFF", command=go_question)
    go_to_btn.place(x=585, y=500)

    # Run app infinitely
    exame_review.mainloop()
