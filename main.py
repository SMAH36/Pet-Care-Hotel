from tkinter import *
from tkinter import ttk
import functions
frm = ttk.Frame(functions.root, padding=100)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=functions.root.destroy).grid(column=1, row=0)
ttk.Button(frm, text="SignUp", command=lambda :functions.openNewWindow("a")).grid(column=2, row=0)
# ttk.Button(frm, text="sign in", command=functions.LoginPage).grid(column=3, row=0)
functions.root.mainloop()
