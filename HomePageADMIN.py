from tkinter import *
from functools import partial
from database import database_connection
import tkinter as tk
from functions import *
# ADD WORKER <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


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


def chooseWorkerRoom():
    newWindow = Toplevel(root)
    newWindow.state('zoomed')
    Label(newWindow, text="HIIIIIIIIIII").pack()
    listOfWorker = []
    for w in database_connection.getAllWorkers():
        worker = User('worker', w[0].replace('(', '').replace(')', '').split(
            ',')[1], w[0].replace('(', '').replace(')', '').split(',')[0])
        listOfWorker.append(worker)
    PetsTypes = {'Dog',
                 'Cat',
                 'Bird',
                 'Fish',
                 'Snake',
                 'Hamester'}
    tkvar = StringVar(root)
    tkvar.set('Choose Worker')

    def change_dropdown(*args):
        print(tkvar.get())
    tkvar.trace('w', change_dropdown)

    text_Type = OptionMenu(newWindow, tkvar, *listOfWorker.name)
    text_Type.place(x=240, y=160)


def homepageADMIN(USER):
    adminHomePage = Toplevel(root)
    adminHomePage.title("Home Page")
    adminHomePage.geometry("200x200")
    Button(adminHomePage, text="Quit",
           command=root.destroy).grid(column=0, row=0)
    signOut(adminHomePage)
    Button(adminHomePage, text="Add Worker",
           command=AddWorkerPage).grid(column=0, row=1)
    Button(adminHomePage, text="Delete Worker",
           command=DeleteWorkerPage).grid(column=1, row=1)
    Button(adminHomePage, text="choose worker room",
           command=chooseWorkerRoom).grid(column=1, row=1)
