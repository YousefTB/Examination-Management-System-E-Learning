# ----------------------
# Exame Module
# ----------------------

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from examDb import *


def gone_question_frame(exam_id, q_list, seq_of_ans, id, ques_num):
    # Create The exame window
    exame = Tk()
    exame.config(bg="#0066CC")

    # Change exame window title
    exame.title("Exam page")

    # Make window icon
    icon = PhotoImage(file="exam.icon.png")
    exame.iconphoto(False, icon)

    # To make the window appear at the center of the screen

    def set_size(root, width, height):
        screen_width = root.winfo_screenwidth()
        secreem_height = root.winfo_screenheight()
        x = int((screen_width - width)/2)
        y = int((secreem_height-height)/2)
        root.geometry(f'{width}x{height}+{x}+{y}')

    # Set Dimensions
    # exame.geometry("960x710")
    set_size(exame, 960, 710)
    exame.resizable(False, False)

    # Create main frame
    frame = Frame(exame, width=900, height=650, bg="White")
    frame.place(x=30, y=30)

    # Prepare the required question
    ques_det = q_list[ques_num - 1][:]

    # Variables part
    question_id = StringVar()
    question = StringVar()
    ans1 = StringVar()
    ans2 = StringVar()
    ans3 = StringVar()
    ans4 = StringVar()
    answer = StringVar()
    question_id.set(ques_det[8])
    question.set(ques_det[1])
    ans1.set(ques_det[2])
    ans2.set(ques_det[3])
    ans3.set(ques_det[4])
    ans4.set(ques_det[5])
    answer.set(seq_of_ans[ques_num - 1][0])

    # Qusetion ID labels
    ques_id_lbl = Label(frame, text="Question id :",
                        height=2, font=("Arial", 15), bg="White")

    ques_id_lbl.place(x=15, y=10)

    ques_id_var_lbl = Label(frame, textvariable=question_id,
                            height=2, font=("Arial", 15), bg="White")

    ques_id_var_lbl.place(x=140, y=10)

    star_lbl = Label(frame, text="*",
                     height=2, font=("Arial", 15), bg="White")

    star_lbl.place(x=30, y=60)

    question_lbl = Label(frame, textvariable=question,
                         height=2, font=("Arial", 15), bg="White")

    question_lbl.place(x=55, y=60)

    ans1_lbl = Label(frame, textvariable=ans1,
                     height=2, font=("Arial", 13), bg="White")

    ans1_lbl.place(x=70, y=110)

    ans2_lbl = Label(frame, textvariable=ans2,
                     height=2, font=("Arial", 13), bg="White")

    ans2_lbl.place(x=70, y=150)

    ans3_lbl = Label(frame, textvariable=ans3,
                     height=2, font=("Arial", 13), bg="White")

    ans3_lbl.place(x=70, y=190)

    ans4_lbl = Label(frame, textvariable=ans4,
                     height=2, font=("Arial", 13), bg="White")

    ans4_lbl.place(x=70, y=230)

    answer_lbl = Label(frame, text="Your answer is :",
                       height=2, font=("Arial", 14, "bold"), fg="#858DFF", bg="White")

    answer_lbl.place(x=15, y=350)

    answer_var_lbl = Label(frame, textvariable=answer,
                           height=2, font=("Tahoma", 15), bg="White")

    answer_var_lbl.place(x=200, y=348)

    # Choose options using radiobuttons
    def selected_ans1():
        answer.set(ans1.get())

    def selected_ans2():
        answer.set(ans2.get())

    def selected_ans3():
        answer.set(ans3.get())

    def selected_ans4():
        answer.set(ans4.get())

    choice = IntVar()

    ans1_rb = Radiobutton(frame, text="", variable=choice,
                          value=1, font=("Arial", 13), command=selected_ans1, bg="White")
    ans1_rb.place(x=40, y=120)

    ans2_rb = Radiobutton(frame, text="", variable=choice,
                          value=2, font=("Arial", 13), command=selected_ans2, bg="White")
    ans2_rb.place(x=40, y=160)

    ans3_rb = Radiobutton(frame, text="", variable=choice,
                          value=3, font=("Arial", 13), command=selected_ans3, bg="White")
    ans3_rb.place(x=40, y=200)

    ans4_rb = Radiobutton(frame, text="", variable=choice,
                          value=4, font=("Arial", 13), command=selected_ans4, bg="White")
    ans4_rb.place(x=40, y=240)

    choice.set(seq_of_ans[ques_num - 1][3])

    # Buttons functions

    def next_question():
        seq_of_ans[ques_num - 1][0] = answer.get()
        save_answers_into_db(ques_det[8], seq_of_ans[ques_num - 1], id)
        seq_of_ans[ques_num - 1][3] = choice.get()
        exame.destroy()
        import reviewExam
        reviewExam.exame_review_frame(exam_id, q_list, seq_of_ans, id)

    # Create next and back buttons
    next_btn = Button(frame, text="Ok", width=13,
                      height=1, font=("Arial", 15, 'bold'), borderwidth=0, bg="#CC0066", fg="White", command=next_question)
    next_btn.place(x=370, y=500)

    # Run app infinitely
    exame.mainloop()
