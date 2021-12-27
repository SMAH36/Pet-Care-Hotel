from tkinter import *
from functools import partial
from database import database_connection
import tkinter as tk


# line 7 changed
def popupmsg(msg):
    popup = tk.Toplevel()
    popup.title("!")
    label = tk.Label(popup, text=msg)  # Can add a font arg here
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()


root = Tk()

#dsfgdsg
class User:
    def __init__(self, rank, name,userID):
        self.name = name
        self.rank = rank
        self.userID=userID

    def checkRank(self):
        return self.rank


USER = User("None", "None", "None")


def idVaildetor(id):
    # ID check
    id = str(id)
    if(len(id) != 9):
        return False
    sum, x, counter = 0, 0, 0
    for i in id:
        x = int(i) * ((counter % 2)+1)
        counter += 1
        if x > 9:
            sum += x-9
        else:
            sum += x
    return sum % 10 == 0


def Emailvaildetor(email):
    # Email check
    if(email.find('@') == -1):
        return False
    elif(email.find('.') == -1):
        return FALSE
    elif(len(email) < 9):
        return False
    return True


def Passwordvaildetor(password):
    # password Check
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
    # Age check
    if(len(age) == 0):
        return False
    age = int(age)
    if 18 <= age <= 120:
        return True
    return False


def phoneCheck(phonenumber):
    # Phone check
    digits = 0
    flag = 1
    if(len(phonenumber) == 0):
        return False
    phonenumber = str(phonenumber)
    for i in range(len(phonenumber)):
        if(phonenumber[i] >= '0' and phonenumber[i] <= '9'):
            digits += 1
            print(i)
        else:
            flag = 0
    if digits == 10 and flag == 1:
        return True
    return False

# def digitsOnly(input):

#     if input.isdigit():
#         print(input)
#         return True

#     elif input is "":
#         print(input)
#         return True

#     else:
#         print(input)
#         return False


def openNewWindow(a):
    print(f"{a}")
    newWindow = Toplevel(root)
    newWindow.title("New Window")
    newWindow.geometry("200x200")
    Label(newWindow,
          text="This is a new window").pack()
#SIGN OUT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def signOut(x):
    Button(x, text="Sign Out", command=x.destroy).grid(column=1, row=0)
    USER = User("None", "None","None")
#ADD WORKER <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def AddWorkerPage():
    AddWorker = Toplevel(root)
    AddWorker.title("Add Worker")
    AddWorker.geometry("500x500")
    Button(AddWorker, text="Quit", command=AddWorker.destroy).grid(
        column=0, row=0)
    label_email = Label(AddWorker, text="Email or Phone",
                        width=20, font=("bold", 10))
    label_email.place(x=0, y=100)
    text_email = Entry(AddWorker)
    text_email.place(x=200, y=100)

    def buttonClick():
        flag = True
        if (flag == True and database_connection.checkIfUserExist(text_email.get()) == 0):
            flag = False
            popupmsg('Email Address not Exist!')
        if (flag == True and database_connection.checkIfUserExist(text_email.get()) == 0):
            flag = False
            popupmsg('Phone Number not Exist!')
        elif(flag == True):
            database_connection.userPromotion(text_email.get())
            popupmsg('You have added ' + text_email.get() +
                     'successfuly to workers')

    Button(AddWorker, command=buttonClick, text='Submit', width=20, bg='brown',
           fg='white').place(x=90, y=120)


def DeleteWorkerPage():
    DeleteWorker = Toplevel(root)
    DeleteWorker.title("Delete Worker")
    DeleteWorker.geometry("500x500")
    Button(DeleteWorker, text="Quit",
           command=DeleteWorker.destroy).grid(column=0, row=0)
    label_email = Label(DeleteWorker, text="Email or Phone",
                        width=20, font=("bold", 10))
    label_email.place(x=0, y=100)
    text_email = Entry(DeleteWorker)
    text_email.place(x=200, y=100)

    def buttonClick():
        flag = True
        if (flag == True and database_connection.checkIfUserExist(text_email.get()) == 0):
            flag = False
            popupmsg('Email Address not Exist!')
        if (flag == True and database_connection.checkIfUserExist(text_email.get()) == 0):
            flag = False
            popupmsg('Phone Number not Exist!')
        elif(flag == True):
            database_connection.removeUser(text_email.get())
            popupmsg('You have removed ' + text_email.get() +
                     'successfuly from workers')

    Button(DeleteWorker, command=buttonClick, text='Submit', width=20, bg='brown',
           fg='white').place(x=90, y=120)










