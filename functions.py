from tkinter import *
from tkinter import ttk
root = Tk()
def openNewWindow():
    print("dsanidasn")
    newWindow = Toplevel(root)
    newWindow.title("New Window")
    newWindow.geometry("200x200")
    Label(newWindow,
          text ="This is a new window").pack()