from tkinter import *
from functools import partial
from database import database_connection

import tkinter as tk


def popupmsg(msg):
    popup = tk.Toplevel()
    popup.title("!")
    label = tk.Label(popup, text=msg)  # Can add a font arg here
    label.pack(side="top", fill="x", pady=10)
    B1 = tk.Button(popup, text="Okay", command=popup.destroy)
    B1.pack()


root = Tk()



class User:
    def __init__(self, rank, name):
        self.name = name
        self.rank = rank

    def checkRank(self):
        return self.rank


USER = User("None", "None")


def idVaildetor(id):
    # ID check
    b = int(id)
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


def openNewWindow(a):
    print(f"{a}")
    newWindow = Toplevel(root)
    newWindow.title("New Window")
    newWindow.geometry("200x200")
    Label(newWindow,
          text="This is a new window").pack()


def signUp(a):
    print(f"{a}")
    tktk = Toplevel(root)
    tktk.title("Sign Up")
    tktk.geometry("500x500")

    label_name = Label(tktk, text="Name", width=20, font=("bold", 10))
    label_name.place(x=100, y=130)

    text_name = Entry(tktk)
    text_name.place(x=240, y=130)

    label_lastName = Label(tktk, text="Last Name", width=20, font=("bold", 10))
    label_lastName.place(x=100, y=160)

    text_lastName = Entry(tktk)
    text_lastName.place(x=240, y=160)

    label_id = Label(tktk, text="Id", width=20, font=("bold", 10))
    label_id.place(x=100, y=190)
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes

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
    label_email.place(x=100, y=220)

    text_email = Entry(tktk)
    text_email.place(x=240, y=220)

    label_password = Label(tktk, text="Password", width=20, font=("bold", 10))
    label_password.place(x=100, y=250)

    text_password = Entry(tktk)
    text_password.place(x=240, y=250)

    label_gender = Label(tktk, text="Gender", width=20, font=("bold", 10))
    label_gender.place(x=100, y=280)
    var = IntVar()
<<<<<<< Updated upstream
    Radiobutton(tktk, text="Male", padx=5, variable=var,
                value=1).place(x=235, y=280)
    Radiobutton(tktk, text="Female", padx=20,
                variable=var, value=2).place(x=290, y=280)

    label_age = Label(tktk, text="Age:", width=20, font=("bold", 10))
    label_age.place(x=100, y=310)
=======
    Radiobutton(tktk, text="Male", padx=5, variable=var,value=1).place(x=235, y=280)
    Radiobutton(tktk, text="Female", padx=20,variable=var, value=2).place(x=290, y=280)

    label_age = Label(tktk, text="Age:", width=20, font=("bold", 10))
    label_age.place(x=100, y=310)

>>>>>>> Stashed changes

    entry_age = Entry(tktk)
    entry_age.place(x=240, y=310)

    label_phone = Label(tktk, text="Phone Number", width=20, font=("bold", 10))
    label_phone.place(x=100, y=340)

    text_phone = Entry(tktk)
    text_phone.place(x=240, y=340)
<<<<<<< Updated upstream
=======

    
        

>>>>>>> Stashed changes

    def buttonClick():
        flag = True
        if len(text_name.get()) < 3:
            flag = False
            popupmsg('Name must be at least 3 letters . . . ')
        if len(text_lastName.get()) < 3:
            flag = False
            popupmsg('Lastname must be at least 3 letters . . . ')
        if(Emailvaildetor(text_email.get()) == False):
            # data base<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            flag = False
            popupmsg('invaild email ! ! !')
        if (Passwordvaildetor(text_password.get()) == False):
            popupmsg(
                'Password must include at least 1 (Bigletter,Smallletter,digit) and 8 letters at least ')
            flag = False
        if(var.get() == 0):
            flag = False
            popupmsg('Must choose gender ! ! !')
        if(agevaildetor(entry_age.get()) == False):
            flag = False
            popupmsg('Must fill age (at least 18)! ! !')
        if(phoneCheck(text_phone.get()) == False):
            flag = False
            popupmsg('incorect phone number (must be 10 digits!)')
        elif(flag == 1):
            popupmsg('You have been successfuly registered :)')

    x = Button(tktk, command=buttonClick, text='Submit', width=20, bg='brown',
               fg='white').place(x=180, y=380)

    # it is use for display the registration form on the window
    tktk.mainloop()
    print("registration form  seccussfully created...")


def signOut(x):
    Button(x, text="Sign Out", command=x.destroy).grid(column=1, row=0)
    USER = None


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


def homepageADMIN():
    adminHomePage = Toplevel(root)
    adminHomePage.title("Home Page")
    adminHomePage.geometry("200x200")
    Button(adminHomePage, text="Quit",
           command=root.destroy).grid(column=0, row=0)
    signOut(adminHomePage)
    Button(adminHomePage, text="AddWorker",
           command=AddWorkerPage).grid(column=0, row=1)
    Button(adminHomePage, text="DeleteWorker",
           command=DeleteWorkerPage).grid(column=1, row=1)


def homepageCUSTOMER():
    CustomerHomePage = Toplevel(root)
    CustomerHomePage.title("Home Page")
    CustomerHomePage.geometry("200x200")
    Button(CustomerHomePage, text="Quit",
           command=root.destroy).grid(column=0, row=0)
    signOut(CustomerHomePage)


def homepageWORKER():
    workerHomePage = Toplevel(root)
    workerHomePage.title("Home Page")
    workerHomePage.geometry("200x200")
    Button(workerHomePage, text="Quit",
           command=root.destroy).grid(column=0, row=0)
    signOut(workerHomePage)


def login(a):
    print(f"{a}")
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
        if(userinfo != False):
            USER = User(userinfo[7], userinfo[2])
            tkWindow.destroy()
            if(USER.rank == 'admin'):
                # refreshhhhhh<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                homepageADMIN()
            if(USER.rank == 'customer'):
                # refreshhhhhh<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                homepageCUSTOMER()
            if(USER.rank == 'worker'):
                # refreshhhhhh<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                homepageWORKER()
        else:
            popupmsg('incorrect email/phone number/password')

    # login button
    loginButton = Button(tkWindow, text="Login",
                         command=afterlogin).grid(row=17, column=13)

    tkWindow.mainloop()
