from tkinter import *
from functools import partial

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

#window
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Log in')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=10, column=10)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=10, column=13)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=14, column=10)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=14, column=13)  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=17, column=13)  

# tkWindow.mainloop()