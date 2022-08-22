# ----------------------
# Exam Module
# ----------------------

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from examDb import *
import random
from reviewExam import exame_review_frame


def exame_frame(exam_id, id):
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

    # Create a canavas for a scrolling Window
    canvas = Canvas(frame,  bg="White")
    canvas.place(x=0, y=0, width=900, height=650,)

    # Make a scrollbar
    scrollbar1 = ttk.Scrollbar(frame, orient=HORIZONTAL, command=canvas.xview)
    scrollbar1.place(x=0, y=630, width=900, height=20)

    # Configure canvas
    canvas.configure(xscrollcommand=scrollbar1.set)
    canvas.bind('<Configure>', lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")))

    # Create another frame inside the canvas
    frame2 = Frame(canvas, width=2200, height=650, bg="White")

    # Add the new frame to the window in a canvas
    canvas.create_window((0, 0), window=frame2, anchor='nw')

    # Prepare Randomized Questions List and Answers using Algorithm (Random AND Search)
    question_cnt = 1
    question_list = questions_list(exam_id)
    answers = retrieve_answers_from_db(exam_id, id)
    randomized_questions = []
    seq_of_ans = []
    refr = {}

    for ques in answers:
        refr[ques[0]] = ques[1]

    temb1 = len(question_list)
    temb2 = 0
    while temb2 != temb1:
        ran_ques = random.choice(question_list)
        del question_list[question_list.index(ran_ques)]
        ran_ques = list(ran_ques)
        ran_ques.insert(0, str(temb2 + 1))
        ran_ques = tuple(ran_ques)
        seq_of_ans.append([refr[ran_ques[8]], ran_ques[7], ran_ques[6], 0])
        randomized_questions.append(ran_ques)
        temb2 += 1

    # Variables part
    question_id = StringVar()
    question_num = StringVar()
    question = StringVar()
    ans1 = StringVar()
    ans2 = StringVar()
    ans3 = StringVar()
    ans4 = StringVar()
    answer = StringVar()
    question_id.set(randomized_questions[question_cnt - 1][8])
    question_num.set(str(question_cnt))
    question.set(randomized_questions[question_cnt - 1][1])
    ans1.set(randomized_questions[question_cnt - 1][2])
    ans2.set(randomized_questions[question_cnt - 1][3])
    ans3.set(randomized_questions[question_cnt - 1][4])
    ans4.set(randomized_questions[question_cnt - 1][5])
    answer.set(seq_of_ans[question_cnt - 1][0])

    # Qusetion ID labels
    ques_id_lbl = Label(frame2, text="Question id :",
                        height=2, font=("Arial", 15), bg="White")

    ques_id_lbl.place(x=15, y=10)

    ques_id_var_lbl = Label(frame2, textvariable=question_id,
                            height=2, font=("Arial", 15), bg="White")

    ques_id_var_lbl.place(x=140, y=10)

    ques_num_lbl = Label(frame2, textvariable=question_num,
                         height=2, font=("Arial", 15), bg="White")

    ques_num_lbl.place(x=5, y=60)

    arc_lbl = Label(frame2, text=")",
                    height=2, font=("Arial", 15), bg="White")

    arc_lbl.place(x=40, y=60)

    question_lbl = Label(frame2, textvariable=question,
                         height=2, font=("Arial", 15), bg="White")

    question_lbl.place(x=55, y=60)

    ans1_lbl = Label(frame2, textvariable=ans1,
                     height=2, font=("Arial", 13), bg="White")

    ans1_lbl.place(x=70, y=110)

    ans2_lbl = Label(frame2, textvariable=ans2,
                     height=2, font=("Arial", 13), bg="White")

    ans2_lbl.place(x=70, y=150)

    ans3_lbl = Label(frame2, textvariable=ans3,
                     height=2, font=("Arial", 13), bg="White")

    ans3_lbl.place(x=70, y=190)

    ans4_lbl = Label(frame2, textvariable=ans4,
                     height=2, font=("Arial", 13), bg="White")

    ans4_lbl.place(x=70, y=230)

    answer_lbl = Label(frame2, text="Your answer is :",
                       height=2, font=("Arial", 14, "bold"), fg="#858DFF", bg="White")

    answer_lbl.place(x=15, y=350)

    answer_var_lbl = Label(frame2, textvariable=answer,
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

    ans1_rb = Radiobutton(frame2, text="", variable=choice,
                          value=1, font=("Arial", 13), command=selected_ans1, bg="White")
    ans1_rb.place(x=40, y=120)

    ans2_rb = Radiobutton(frame2, text="", variable=choice,
                          value=2, font=("Arial", 13), command=selected_ans2, bg="White")
    ans2_rb.place(x=40, y=160)

    ans3_rb = Radiobutton(frame2, text="", variable=choice,
                          value=3, font=("Arial", 13), command=selected_ans3, bg="White")
    ans3_rb.place(x=40, y=200)

    ans4_rb = Radiobutton(frame2, text="", variable=choice,
                          value=4, font=("Arial", 13), command=selected_ans4, bg="White")
    ans4_rb.place(x=40, y=240)

    # Buttons functions
    def next_question():
        nonlocal seq_of_ans
        nonlocal question_cnt

        # Getting the choosed answer to store FIRST
        seq_of_ans[question_cnt - 1][0] = answer.get()
        seq_of_ans[question_cnt - 1][3] = choice.get()
        save_answers_into_db(
            randomized_questions[question_cnt - 1][8], seq_of_ans[question_cnt - 1], id)

        # Prepare the next question and showing it
        if question_cnt < len(randomized_questions):
            question_cnt += 1
            question_id.set(randomized_questions[question_cnt - 1][8])
            question_num.set(str(question_cnt))
            question.set(randomized_questions[question_cnt - 1][1])
            ans1.set(randomized_questions[question_cnt - 1][2])
            ans2.set(randomized_questions[question_cnt - 1][3])
            ans3.set(randomized_questions[question_cnt - 1][4])
            ans4.set(randomized_questions[question_cnt - 1][5])
            answer.set(seq_of_ans[question_cnt - 1][0])
            choice.set(seq_of_ans[question_cnt - 1][3])

        else:  # After the last question
            messagebox.showinfo(
                "Warning", """The exam is about to end\nCheck your answers in next page""")
            exame.destroy()
            exame_review_frame(exam_id, randomized_questions, seq_of_ans, id)

    def back_question():
        nonlocal seq_of_ans
        nonlocal question_cnt

        # Getting the choosed answer to store FIRST
        seq_of_ans[question_cnt - 1][0] = answer.get()
        seq_of_ans[question_cnt - 1][3] = choice.get()

        if question_cnt > 1:  # Shows the question before the current one
            question_cnt -= 1
            question_id.set(randomized_questions[question_cnt - 1][8])
            question_num.set(str(question_cnt))
            question.set(randomized_questions[question_cnt - 1][1])
            ans1.set(randomized_questions[question_cnt - 1][2])
            ans2.set(randomized_questions[question_cnt - 1][3])
            ans3.set(randomized_questions[question_cnt - 1][4])
            ans4.set(randomized_questions[question_cnt - 1][5])
            answer.set(seq_of_ans[question_cnt - 1][0])
            choice.set(seq_of_ans[question_cnt - 1][3])

    # Create next and back buttons
    back_btn = Button(frame, text="Back", width=12,
                      height=1, font=("Arial", 14), borderwidth=0, bg="#FF0099", fg="White", command=back_question)
    back_btn.place(x=580, y=590)

    next_btn = Button(frame, text="Next", width=12,
                      height=1, font=("Arial", 14), borderwidth=0, bg="#FF0099", fg="White", command=next_question)
    next_btn.place(x=730, y=590)

    # Run app infinitely
    exame.mainloop()
