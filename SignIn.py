from tkinter import *
from functools import partial
from database import database_connection
import tkinter as tk
from functions import *
from HomePageADMIN import *
from HomePageCUSTOMER import *
from HomePageWORKER import *


def login():
    tkWindow = Toplevel(root)
    tkWindow.title("Log in")
    tkWindow.geometry('400x150')
    # username label and text entry box
    usernameLabel = Label(
        tkWindow, text="Email / Phone Number").grid(row=10, column=10)
    username = StringVar()
    usernameEntry = Entry(
        tkWindow, textvariable=username).grid(row=10, column=13)

    # password label and password entry box
    passwordLabel = Label(tkWindow, text="Password").grid(row=14, column=10)
    password = StringVar()
    passwordEntry = Entry(tkWindow, textvariable=password,
                          show='*').grid(row=14, column=13)

    def afterlogin():
        userinfo = database_connection.signIn(username.get(), password.get())
        print('userinfo', userinfo)
        if(userinfo != False):
            USER = User(userinfo[7], userinfo[2],
                        userinfo[1], userinfo[3], userinfo[6])
            tkWindow.destroy()
            if(USER.rank == 'admin'):
                # refreshhhhhh<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                homepageADMIN(USER)
            if(USER.rank == 'customer'):
                # refreshhhhhh<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                homepageCUSTOMER(USER)
            if(USER.rank == 'worker'):
                # refreshhhhhh<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                homepageWORKER(USER)
        else:
            popupmsg('incorrect email/phone number/password')

    # login button
    loginButton = Button(tkWindow, text="Login",
                         command=afterlogin).grid(row=17, column=13)

    tkWindow.mainloop()
