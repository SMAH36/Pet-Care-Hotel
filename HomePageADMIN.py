from tkinter import *
from functools import partial
from database import database_connection
import tkinter as tk
from functions import *
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