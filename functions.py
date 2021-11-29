from tkinter import *
from tkinter import ttk
root = Tk()
<<<<<<< HEAD
def openNewWindow():
=======


def openNewWindow(a):
    print(f"{a}")
>>>>>>> main
    newWindow = Toplevel(root)
    newWindow.title("New Window")
    newWindow.geometry("200x200")
    Label(newWindow,
          text="This is a new window").pack()
