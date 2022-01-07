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
    tkWindow.title("Sign In")
    tkWindow.state('zoomed')
    tkWindow.configure(background='#E9E9E5')
    # username label and text entry box
    Label(
        tkWindow, text="Email / Phone Number", width=20, bg='#E9E9E5', fg='black', font=("bold", 12)).place(x=400, y=250)
    Label(tkWindow, text="Login", width=20, bg='#E9E9E5',
          fg='black', font=("Elephant", 17)).place(x=430, y=170)
    topLabel = Label(tkWindow, text='', width=90, bg='#D4D6C8',
                     fg='black', font=('Verdana Pro Black', 30))
    topLabel.pack(side=TOP)
    bottomLabel = Label(tkWindow, text='', width=90, bg='#D4D6C8',
                        fg='black', font=('Verdana Pro Black', 30))
    bottomLabel.pack(side=BOTTOM)
    username = StringVar()
    usernameEntry = Entry(
        tkWindow, textvariable=username, width=20, font=("", 15)).place(x=600, y=250)

    # password label and password entry box
    passwordLabel = Label(tkWindow, text="Password", width=20,
                          bg='#E9E9E5', fg='black', font=("bold", 12)).place(x=357, y=300)
    password = StringVar()
    passwordEntry = Entry(tkWindow, textvariable=password, width=20, font=("", 15),
                          show='*').place(x=600, y=300)

    def afterlogin():
        userinfo = database_connection.signIn(username.get(), password.get())
        # userinfo = (3, '8d6ad7c9-7a1a-42fb-bfee-2ad508749225', 'malak', 'bta', '18', 'Male', '31511122128',
        #             'worker', datetime.datetime(2021, 12, 29, 14, 26, 44, 513526, tzinfo=datetime.timezone.utc))
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
            popupmsg('Incorrect email/phone number/password')

    # login button
    loginButton = Button(tkWindow, text="Login", width=10, bg='#5C715E', fg='white', font=(
        "bold", 12), command=afterlogin).place(x=700, y=400)

    tkWindow.mainloop()
