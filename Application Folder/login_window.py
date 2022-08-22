# ----------------------
# Login Module
# ----------------------

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from login_checking import *
from Admin import *
from ExaminerWin import *
from StudentWin import *


def Login_win():

    # Create The main app window
    login = Tk()

    # Change app title
    login.title("Examination System")

    # Make window icon
    icon = PhotoImage(file="exam.icon.png")
    login.iconphoto(False, icon)

    # To make the window appear at the center of the screen

    def set_size(root, width, height):
        screen_width = root.winfo_screenwidth()
        secreem_height = root.winfo_screenheight()
        x = int((screen_width - width)/2)
        y = int((secreem_height-height)/2)
        root.geometry(f'{width}x{height}+{x}+{y}')

    # Set Dimensions
    set_size(login, 950, 700)
    login.resizable(False, False)

    # Create frame
    frame = Frame(login, width=950, height=700)
    frame.pack()

    # To import image
    img = ImageTk.PhotoImage(Image.open("Logimg.jpg"))

    # Create a Label Widget to display the text or Image
    label = Label(frame, image=img)
    label.pack()

    # Write Welcome label
    welcomelbl = Label(frame, text="Welcome To\nExamination System",
                       height=2, font=("Tahoma", 28, 'bold'), bg="White").place(x=490, y=75)

    # Create Email and password labels
    emaillbl = Label(frame, text="Email",
                     height=2, font=("Arial", 16), bg="White").place(x=500, y=250)

    passwordlbl = Label(frame, text="Password",
                        height=2, font=("Arial", 16), bg="White").place(x=500, y=340)

    # Crate variables to hold email and password
    email = StringVar()
    password = StringVar()
    email.set("")
    password.set("")

    # Create an events on entries

    def clickE(event):
        email_inp.config(state=NORMAL)
        email_inp.delete(0, END)

    def clickP(event):
        password_inp.config(state=NORMAL)
        password_inp.delete(0, END)

    # Create input fields
    email_inp = Entry(frame, width=26, font=("Arial", 16),
                      textvariable=email, border=1.5)
    email_inp.insert(0, "12***@user.exam")
    email_inp.config(state=DISABLED)
    email_inp.bind("<Button-1>", clickE)
    email_inp.place(x=500, y=305)

    password_inp = Entry(frame, width=26, font=("Arial", 16),
                         textvariable=password, border=1.5, show='*')
    password_inp.insert(0, "**************")
    password_inp.config(state=DISABLED)
    password_inp.bind("<Button-1>", clickP)
    password_inp.place(x=500, y=395)

    # Login function

    def log():
        try:
            data1 = email.get()
            id = data1[:data1.index('@')]
            type = data1[data1.index('@') + 1:data1.index('.exam')]
            pasw = password.get()
            if check_login(id, type, pasw) == 1:
                login.destroy()
                student_module(id)
            elif check_login(id, type, pasw) == 2:
                login.destroy()
                examiner_module(id)
            elif check_login(id, type, pasw) == 3:
                login.destroy()
                admin_module(id)
            else:
                messagebox.showerror(
                    "Warning", "Wrong E-mail or Password\nTry Again")
        except:
            messagebox.showerror(
                "Warning", "Wrong E-mail or Password\nTry Again")

    # Create login button
    loginbtn = Button(frame, text="Login", width=26, font=("Arial", 16),
                      height=1, borderwidth=0, bg="#858DFF", fg="White", command=log).place(x=500, y=450)

    # Run app infinitely
    login.mainloop()
