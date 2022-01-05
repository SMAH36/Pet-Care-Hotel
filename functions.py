from tkinter import *
from functools import partial
from database import database_connection
import tkinter as tk


# line 7 changed
# line 8 changed

def popupmsg(msg):
    popup = tk.Toplevel()
    popup.title("!")
    label = tk.Label(popup, text=msg)  # Can add a font arg here
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()


root = Tk()

# dsfgdsg


class User:
    def __init__(self, rank, name, userID, lastName, personalId):
        self.name = name
        self.rank = rank
        self.userID = userID
        self.lastName = lastName
        self.personalId = personalId

    def checkRank(self):
        return self.rank


USER = User("None", "None", "None", "None", "None")


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

# def openNewWindow():
#     newWindow = Toplevel(root)
#     newWindow.title("New Window")
#     newWindow.geometry("200x200")
#     Label(newWindow,
#           text="This is a new window").pack()

# SIGN OUT <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


def signOut(x):
    Button(x, text="Sign Out", command=x.destroy).grid(column=1, row=0)
    USER = User("None", "None", "None", "None", "None")
