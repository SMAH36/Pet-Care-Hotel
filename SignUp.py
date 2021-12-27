from functions import *
from tkinter import *
from functools import partial
from database import database_connection
import tkinter as tk
def signUp():
    
    tktk = Toplevel(root)
    tktk.title("Sign Up")
    tktk.geometry("500x500")

    label_name = Label(tktk, text="Name", width=20, font=("bold", 10))
    label_name.place(x=80, y=130)

    text_name = Entry(tktk)
    text_name.place(x=240, y=130)

    label_lastName = Label(tktk, text="Last Name", width=20, font=("bold", 10))
    label_lastName.place(x=80, y=160)

    text_lastName = Entry(tktk)
    text_lastName.place(x=240, y=160)

    label_id = Label(tktk, text="Id", width=20, font=("bold", 10))
    label_id.place(x=68, y=190)

    def idChecker(var):
        content = var.get()
        if len(content) == 9:
            print(idVaildetor(content))

    var = StringVar()
    var.trace("w", lambda name, index, mode, var=var: idChecker(var))
    text_id = Entry(tktk, textvariable=var)
    text_id.pack()
    text_id.place(x=240, y=190)

    label_email = Label(tktk, text="Email", width=20, font=("bold", 10))
    label_email.place(x=68, y=210)

    text_email = Entry(tktk)
    text_email.place(x=240, y=210)

    label_password = Label(tktk, text="Password", width=20, font=("bold", 10))
    label_password.place(x=68, y=230)

    text_password = Entry(tktk)
    text_password.place(x=240, y=230)

    label_gender = Label(tktk, text="Gender", width=20, font=("bold", 10))
    label_gender.place(x=70, y=250)
    var = IntVar()
    Radiobutton(tktk, text="Male", padx=5, variable=var,
                value=1).place(x=235, y=250)
    Radiobutton(tktk, text="Female", padx=20,
                variable=var, value=2).place(x=290, y=250)

    label_age = Label(tktk, text="Age:", width=20, font=("bold", 10))
    label_age.place(x=70, y=300)

    entry_age = Entry(tktk)
    entry_age.place(x=240, y=300)

    label_phone = Label(tktk, text="Phone Number", width=20, font=("bold", 10))
    label_phone.place(x=68, y=330)

    text_phone = Entry(tktk)
    text_phone.place(x=240, y=330)

    def buttonClick():
        flag = True
        if len(text_name.get()) < 3:
            flag = False
            popupmsg('Name must be at least 3 letters . . . ')
        if len(text_lastName.get()) < 3 and flag == True:
            flag = False
            popupmsg('Lastname must be at least 3 letters . . . ')
        if(Emailvaildetor(text_email.get()) == False and flag == True):
            flag = False
            popupmsg('invaild email ! ! !')
        if (Passwordvaildetor(text_password.get()) == False and flag == True):
            popupmsg(
                'Password must include at least 1 (Bigletter,Smallletter,digit) and 8 letters at least ')
            flag = False
        if(var.get() == 0 and flag == True):
            flag = False
            popupmsg('Must choose gender ! ! !')
        if(agevaildetor(entry_age.get()) == False and flag == True):
            flag = False
            popupmsg('Must fill age (at least 18)! ! !')
        if(phoneCheck(text_phone.get()) == False and flag == True):
            flag = False
            popupmsg('incorect phone number (must be 10 digits!)')
        if (flag == True and database_connection.checkIfUserExist(text_email.get()) == 1):
            flag = False
            popupmsg('Email Address Already Exist!')
        if (flag == True and database_connection.checkIfUserExist(text_phone.get()) == 1):
            flag = False
            popupmsg('Phone Number Already Exist!')
        elif(flag == True):
            if var.get() == 1:
                gender = 'male'
            else:
                gender = 'female'
            database_connection.register(text_email.get(), text_phone.get(), text_password.get(
            ), text_name.get(), text_lastName.get(), entry_age.get(), gender, text_id.get(), rank='customer')
            popupmsg('You have been successfuly registered :)')

    x = Button(tktk, command=buttonClick, text='Submit', width=20, bg='brown',
               fg='white').place(x=180, y=380)

    # it is use for display the registration form on the window
    tktk.mainloop()
    print("registration form  seccussfully created...")