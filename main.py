from tkinter import *
from tkinter import ttk
import functions
frm = ttk.Frame(functions.root, padding=100)
frm.grid()

ttk.Button(frm, text="Quit", command=functions.root.destroy).grid(column=0, row=2)
if(functions.USER.checkRank()=="None"):
    ttk.Button(frm, text="Sign Up", command=lambda :functions.signUp("a")).grid(column=0, row=1)
    ttk.Button(frm, text="sign in", command=lambda:functions.login("a")).grid(column=0, row=0)
#while(functions.USER.CheckRank()=="admin"):

functions.root.mainloop()
