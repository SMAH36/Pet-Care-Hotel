from tkinter import *
from functools import partial
root = Tk()

class User:
    def __init__(self,rank,name):
        self.name = name
        self.rank = rank

    def checkRank(self):
        return self.rank
USER=User("None","None")

def idVaildetor(id):
    #ID check
    b = int(id)
    id = str(id)
    if(len(id) != 9 and b.isnumeric()):
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
    #Email check
    if(email.find('@')==-1):
        return False
    elif(email.find('.')==-1):
        return FALSE
    elif(len(email)<9):
        return False
    return True

def Passwordvaildetor(password):
    #password Check
    bigLet,SmallLet,digit=0,0,0
    for _ in range(len(password)):
        if(password[_]<='Z' and password[_]>='A'):
            bigLet+=1
        if(password[_]<='z' and password[_]>='a'):
            SmallLet+=1
        if(password[_]<='9' and password[_]>='0'):
            digit+=1
    sum=bigLet+SmallLet+digit    
    if(bigLet>=1 and SmallLet>=1 and digit>=1 and sum>=8):
        return True
    else: return False

def agevaildetor(age):
    #Age check
    if(len(age)==0):
        return False
    age=int(age)
    if 18<=age<=120:
        return True
    return False

def phoneCheck(phonenumber):
    #Phone check
    digits=0
    flag=1
    if(len(phonenumber)==0):
        return False
    phonenumber=str(phonenumber)
    for i in range(len(phonenumber)):
        if(phonenumber[i]>='0' and phonenumber[i]<='9'):
            digits+=1
            print(i)
        else:
            flag=0
    if digits==10 and flag==1:
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

def signUp(a):
    print(f"{a}")
    tktk= Toplevel(root)
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
    Radiobutton(tktk, text="Male", padx=5, variable=var,value=1).place(x=235, y=250)
    Radiobutton(tktk, text="Female", padx=20,variable=var, value=2).place(x=290, y=250)

    label_age = Label(tktk, text="Age:", width=20, font=("bold", 10))
    label_age.place(x=70, y=300)


    entry_age = Entry(tktk)
    entry_age.place(x=240, y=300)

    label_phone = Label(tktk, text="Phone Number", width=20, font=("bold", 10))
    label_phone.place(x=68, y=330)

    text_phone = Entry(tktk)
    text_phone.place(x=240, y=330)

    import tkinter as tk

    

    def popupmsg(msg):
        popup = tk.Toplevel()
        popup.title("!")
        label = tk.Label(popup, text=msg) #Can add a font arg here
        label.pack(side="top", fill="x", pady=10)
        B1 = tk.Button(popup, text="Okay", command = popup.destroy)
        B1.pack()
        


    def buttonClick():
        flag=True
        if len(text_name.get()) < 3:
            flag=False
            popupmsg('Name must be at least 3 letters . . . ')
        if len(text_lastName.get()) < 3:
            flag=False
            popupmsg('Lastname must be at least 3 letters . . . ')
        if(Emailvaildetor(text_email.get())==False):
            #data base<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
            flag=False
            popupmsg('invaild email ! ! !')
        if (Passwordvaildetor(text_password.get())==False):
            popupmsg('Password must include at least 1 (Bigletter,Smallletter,digit) and 8 letters at least ')
            flag=False
        if(var.get()==0):
            flag=False
            popupmsg('Must choose gender ! ! !')
        if(agevaildetor(entry_age.get())==False):
            flag=False
            popupmsg('Must fill age (at least 18)! ! !')
        if(phoneCheck(text_phone.get())==False):
            flag=False
            popupmsg('incorect phone number (must be 10 digits!)')
        elif(flag==1):
            popupmsg('You have been successfuly registered :)')


        
        


    x = Button(tktk, command=buttonClick, text='Submit', width=20, bg='brown',
            fg='white').place(x=180, y=380)

    # it is use for display the registration form on the window
    tktk.mainloop()
    print("registration form  seccussfully created...")









def login(a):
    print(f"{a}")
    tkWindow = Toplevel(root)
    tkWindow.title("Log in")
    tkWindow.geometry('400x150')  
    #username label and text entry box
    usernameLabel = Label(tkWindow, text="User Name").grid(row=10, column=10)
    username = StringVar()
    usernameEntry = Entry(tkWindow, textvariable=username).grid(row=10, column=13)  

    #password label and password entry box
    passwordLabel = Label(tkWindow,text="Password").grid(row=14, column=10)  
    password = StringVar()
    passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=14, column=13)  

    def afterlogin():
        #DAta base<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        USER=User("admen","saher")
        # tkWindow.destroy()
        


    #login button
    loginButton = Button(tkWindow, text="Login", command=afterlogin).grid(row=17, column=13)  

    tkWindow.mainloop()

