
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
class pets:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1280x730+1+1')
        self.root.title('pets hotel')
        self.root.configure(background='#E9E9E5')
        #self.root.resizable(False,True)
        title = Label(self.root,text='...Welcome to our PETS CARE&LOVE animals hotel...',width=50, bg='#E8EAE6',fg='black',font=('Verdana Pro Black',20)).place(x=0, y=180)
        title = Label(self.root,text='',width=90, bg='#D4D6C8',fg='black',font=('Verdana Pro Black',20)).place(x=0, y=120)
        title = Label(self.root,text='',width=90, bg='#D4D6C8',fg='black',font=('Verdana Pro Black',20)).place(x=0, y=420)
        title = Label(self.root,text='PETS CARE&LOVE',width=20, bg='#CFDAC8',fg='black',font=('Verdana Pro Black',20)).place(x=930, y=120)
        title = Label(self.root,text='your pet deserves the best care\neven when you are not around.\nWill that be possible?...',width=30, bg='#CFDAC8',fg='black',font=('Verdana Pro Black',13)).place(x=960, y=160)
        title = Label(self.root,text='booking for a hotel',width=20, bg='#D4D6C8',fg='black',font=('Verdana Pro Black',13)).place(x=10, y=420)
        title = Label(self.root,text='our services',width=15, bg='#D4D6C8',fg='black',font=('Verdana Pro Black',13)).place(x=230, y=420)
        title = Label(self.root,text='customer responses',width=19, bg='#D4D6C8',fg='black',font=('Verdana Pro Black',13)).place(x=440, y=420)
        title = Label(self.root,text='gallery',width=19, bg='#D4D6C8',fg='black',font=('Verdana Pro Black',13)).place(x=640, y=420)
        title = Label(self.root,text='jops',width=19, bg='#D4D6C8',fg='black',font=('Verdana Pro Black',13)).place(x=840, y=420)
        title = Label(self.root,text='',width=20, bg='#D4D6C8',fg='black',font=('Verdana Pro Black',13)).place(x=10, y=480)
        title = Label(self.root,text='our services',width=15, bg='#D4D6C8',fg='black',font=('Verdana Pro Black',13)).place(x=230, y=420)
        #Label.pack(self.root,padx=10,ipadx=50,ipady=70)
root = Tk()  