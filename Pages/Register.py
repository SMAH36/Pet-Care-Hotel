
import tkinter as tk
from tkinter import*

import os
import sys
import inspect
current_dir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import database
from database import database_connection

def idVaildetor(id):
    b = int(id)
    id = str(id)
    if(len(id) != 9 and b.isnumeric()):
        return False
    sum, x, counter = 0, 0, 0
    for d in id:
        x = int(i) * ((counter % 2)+1)
        counter += 1
        if x > 9:
            sum += x-9
        else:
            sum += x
    return sum % 10 == 0


def Emailvaildetor(email):
    if(email.find('@') == -1):
        return False
    elif(email.find('.') == -1):
        return FALSE
    elif(len(email) < 9):
        return False
    return True


def Passwordvaildetor(password):
    bigLet, SmallLet, digit = 0, 0, 0
    for _ in range(len(password)):
        if(password[_] <= 'Z' and password[_] >= 'A'):
            bigLet += 1
        if(password[_] <= 'z' and password[_] >= 'a'):
            SmallLet += 1
        if(password[_] <= '9' and password[_] >= '0'):
            digit += 1
    sum = bigLet+SmallLet+digit
    if(bigLet >= 1 and SmallLet >= 1 and digit >= 1 and sum >= 8):
        return True
    else:
        return False


def agevaildetor(age):
    if(len(age) == 0):
        return False
    age = int(age)
    if 18 <= age <= 120:
        return True
    return False


def phoneCheck(phonenumber):
    digits = 0
    flag = 1
    if(len(phonenumber) == 0):
        return False
    phonenumber = str(phonenumber)
    for i in range(len(phonenumber)):
        if(phonenumber[i] >= '0' and phonenumber[i] <= '9'):
            digits += 1
        else:
            flag = 0
    if digits == 10 and flag == 1:
        return True
    return False


root = Tk()
root.geometry('500x500')
root.title("Registration Form")

label_0 = Label(root, text="Registration form", width=20, font=("bold", 20))
label_0.place(x=90, y=53)

label_name = Label(root, text="Name", width=20, font=("bold", 10))
label_name.place(x=80, y=130)

text_name = Entry(root)
text_name.place(x=240, y=130)

label_lastName = Label(root, text="Last Name", width=20, font=("bold", 10))
label_lastName.place(x=80, y=160)

text_lastName = Entry(root)
text_lastName.place(x=240, y=160)

label_id = Label(root, text="Id", width=20, font=("bold", 10))
label_id.place(x=68, y=190)


def idChecker(var):
    content = var.get()
    if len(content) == 9:
        print(idVaildetor(content))


var = StringVar()
var.trace("w", lambda name, index, mode, var=var: idChecker(var))
text_id = Entry(root, textvariable=var)
text_id.pack()
text_id.place(x=240, y=190)

label_email = Label(root, text="Email", width=20, font=("bold", 10))
label_email.place(x=68, y=210)

text_email = Entry(root)
text_email.place(x=240, y=210)

label_password = Label(root, text="Password", width=20, font=("bold", 10))
label_password.place(x=68, y=230)

text_password = Entry(root)
text_password.place(x=240, y=230)

label_gender = Label(root, text="Gender", width=20, font=("bold", 10))
label_gender.place(x=70, y=250)
var = IntVar()
Radiobutton(root, text="Male", padx=5, variable=var,
            value=1).place(x=235, y=250)
Radiobutton(root, text="Female", padx=20,
            variable=var, value=2).place(x=290, y=250)

label_age = Label(root, text="Age:", width=20, font=("bold", 10))
label_age.place(x=70, y=300)


entry_age = Entry(root)
entry_age.place(x=240, y=300)

label_phone = Label(root, text="Phone Number", width=20, font=("bold", 10))
label_phone.place(x=68, y=330)

text_phone = Entry(root)
text_phone.place(x=240, y=330)


def popupmsg(msg):
    popup = tk.Toplevel()
    popup.title("!")
    label = tk.Label(popup, text=msg)  # Can add a font arg here
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()


def buttonClick():
    flag = True
    if len(text_name.get()) < 3:
        flag = False
        popupmsg('Name must be at least 3 letters . . . ')
    if len(text_lastName.get()) < 3 and flag == True:
        flag = False
        popupmsg('Lastname must be at least 3 letters . . . ')
    if(Emailvaildetor(text_email.get()) == False and flag == True):
        # data base<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
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
        popupmsg('You have been successfuly registered :)')


x = Button(root, command=buttonClick, text='Submit', width=20, bg='brown',
           fg='white').place(x=180, y=380)

# it is use for display the registration form on the window
root.mainloop()
print("registration form  seccussfully created...")
