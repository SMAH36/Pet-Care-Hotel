from functions import *
from tkinter import *
from functools import partial
from database import database_connection
import tkinter as tk
def signUp():
    
    tktk = Toplevel(root)
    tktk.title("Sign Up")
    tktk.state("zoomed")
    tktk.configure(background='#E9E9E5')
    label_name = Label(tktk, text="First Name", width=20,bg='#E9E9E5',fg='black', font=("bold", 12))
    label_name.place(x=484, y=160)

    text_name = Entry(tktk)
    text_name.place(x=650, y=160)

    label_lastName = Label(tktk, text="Last Name", width=20, bg='#E9E9E5',fg='black',font=("bold", 12))
    label_lastName.place(x=484, y=200)

    text_lastName = Entry(tktk)
    text_lastName.place(x=650, y=200)

    label_id = Label(tktk, text="ID", width=20,bg='#E9E9E5',fg='black', font=("bold", 12))
    label_id.place(x=454, y=250)

    def idChecker(var):
        content = var.get()
        if len(content) == 9:
            print(idVaildetor(content))

    var = StringVar()
    var.trace("w", lambda name, index, mode, var=var: idChecker(var))
    text_id = Entry(tktk, textvariable=var)
    text_id.pack()
    text_id.place(x=650, y=250)
    topLabel = Label(tktk,text='',width=90, bg='#D4D6C8',fg='black',font=('Verdana Pro Black',30))
    topLabel.pack(side=TOP)
    bottomLabel = Label(tktk,text='',width=90, bg='#D4D6C8',fg='black',font=('Verdana Pro Black',30))
    bottomLabel.pack(side=BOTTOM)
    label_titl = Label(tktk,text='Register',width=11, bg='#E9E9E5',fg='black',font=('Elephant',17)).place(x=570, y=60)
    label_email = Label(tktk, text="Email", width=20,bg='#E9E9E5',fg='black', font=("bold", 12))
    label_email.place(x=467, y=290)

    text_email = Entry(tktk)
    text_email.place(x=650, y=290)

    label_password = Label(tktk, text="Password", width=20,bg='#E9E9E5',fg='black', font=("bold", 12))
    label_password.place(x=482, y=340)

    text_password = Entry(tktk)
    text_password.place(x=650, y=340)

    label_gender = Label(tktk, text="Gender", width=20,bg='#E9E9E5',fg='black', font=("bold", 12))
    label_gender.place(x=473, y=380)
    var = IntVar()
    Radiobutton(tktk, text="Male", padx=5, variable=var,bg='#E9E9E5',fg='black',
                value=1).place(x=630, y=380)
    Radiobutton(tktk, text="Female", padx=20,bg='#E9E9E5',fg='black',
                variable=var, value=2).place(x=690, y=380)

    label_age = Label(tktk, text="Age", width=20,bg='#E9E9E5',fg='black', font=("bold", 12))
    label_age.place(x=467, y=420)

    entry_age = Entry(tktk)
    entry_age.place(x=650, y=420)

    label_phone = Label(tktk, text="Phone Number", width=20,bg='#E9E9E5',fg='black', font=("bold", 12))
    label_phone.place(x=500, y=460)

    text_phone = Entry(tktk)
    text_phone.place(x=650, y=460)

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
            popupmsg('Invaild email ! ! !')
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
            popupmsg('Incorect phone number (must be 10 digits!)')
        if (flag == True and database_connection.checkIfUserExist(text_email.get()) == 1):
            flag = False
            popupmsg('Email address already exist!')
        if (flag == True and database_connection.checkIfUserExist(text_phone.get()) == 1):
            flag = False
            popupmsg('Phone number already exist!')
        elif(flag == True):
            if var.get() == 1:
                gender = 'Male'
            else:
                gender = 'Female'
            database_connection.register(text_email.get(), text_phone.get(), text_password.get(
            ), text_name.get(), text_lastName.get(), entry_age.get(), gender, text_id.get(), rank='customer')
            popupmsg('You have been successfuly registered :)')

    Button(tktk, command=buttonClick, text='Submit', width=20,bg='#E9E9E5',fg='black', font=("bold", 12)).place(x=650, y=600)

    # it is use for display the registration form on the window
    tktk.mainloop()
    print("Registration form  seccussfully created...")