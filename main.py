from tkinter import *
from tkinter import ttk
import functions
import Pages
frm = ttk.Frame(functions.root, padding=100)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=functions.root.destroy).grid(column=1, row=0)
ttk.Button(frm, text="SignUp", command=functions.openNewWindow).grid(column=2, row=0)
functions.root.mainloop()