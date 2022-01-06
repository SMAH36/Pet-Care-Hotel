from tkinter import *
from tkinter import messagebox
from tkinter import ttk


class pets:
    def __init__(self, root):
        self.root = root
        self.root.state('zoomed')
        self.root.title('pets hotel')
        self.root.configure(background='#E9E9E5')
        # self.root.resizable(False,True)
        title = Label(self.root, text='...Welcome to our PETS CARE&LOVE animals hotel...',
                      width=50, bg='#E8EAE6', fg='black', font=('Verdana Pro Black', 20)).place(x=0, y=180)
        title = Label(self.root, text='', width=90, bg='#D4D6C8', fg='black', font=(
            'Verdana Pro Black', 20)).place(x=0, y=120)
        title = Label(self.root, text='', width=90, bg='#D4D6C8', fg='black', font=(
            'Verdana Pro Black', 20)).place(x=0, y=420)
        title = Label(self.root, text='PETS CARE&LOVE', width=20, bg='#CFDAC8',
                      fg='black', font=('Verdana Pro Black', 20)).place(x=930, y=120)
        title = Label(self.root, text='your pet deserves the best care\neven when you are not around.\nWill that be possible?...',
                      width=30, bg='#CFDAC8', fg='black', font=('Verdana Pro Black', 13)).place(x=960, y=160)
        title = Label(self.root, text='booking for a hotel', width=20, bg='#D4D6C8',
                      fg='black', font=('Verdana Pro Black', 13)).place(x=10, y=420)
        title = Label(self.root, text='our services', width=15, bg='#D4D6C8',
                      fg='black', font=('Verdana Pro Black', 13)).place(x=230, y=420)
        title = Label(self.root, text='customer responses', width=19, bg='#D4D6C8',
                      fg='black', font=('Verdana Pro Black', 13)).place(x=440, y=420)
        title = Label(self.root, text='gallery', width=19, bg='#D4D6C8',
                      fg='black', font=('Verdana Pro Black', 13)).place(x=640, y=420)
        title = Label(self.root, text='jops', width=19, bg='#D4D6C8', fg='black', font=(
            'Verdana Pro Black', 13)).place(x=840, y=420)
        title = Label(self.root, text='', width=20, bg='#D4D6C8', fg='black', font=(
            'Verdana Pro Black', 13)).place(x=10, y=480)
        title = Label(self.root, text='our services', width=15, bg='#D4D6C8',
                      fg='black', font=('Verdana Pro Black', 13)).place(x=230, y=420)
        # Label.pack(self.root,padx=10,ipadx=50,ipady=70)


root = Tk()
Button(root, text='LOGIN', width=7, bg='#9A9B94',
       fg='black', font=('', 13)).place(x=110, y=30)
Button(root, text='SIGNUP', width=8, bg='#9A9B94',
       fg='black', font=('', 13)).place(x=190, y=30)
Button(root, text='ADD MY PET', width=11, bg='#9A9B94',
       fg='black', font=('', 13)).place(x=280, y=30)
Button(root, text='BOOK APPOINTMENT', width=18, bg='#9A9B94',
       fg='black', font=('', 13)).place(x=400, y=30)
Button(root, text='ABOUT US', width=9, bg='#9A9B94',
       fg='black', font=('', 13)).place(x=580, y=30)
Button(root, text='TESTIMONIALS', width=13, bg='#9A9B94',
       fg='black', font=('', 13)).place(x=680, y=30)
Button(root, text='CONTACT US', width=11, bg='#9A9B94',
       fg='black', font=('', 13)).place(x=820, y=30)
Button(root, text='EXIT', width=15, bg='#5C715E',
       fg='black', font=('', 13)).place(x=1100, y=610)
Button(root, text='FIND US', width=8, bg='#9A9B94',
       fg='black', font=('', 13)).place(x=940, y=30)
# Button(root, text='LOGOUT', width=8, bg='#9A9B94',fg='black',font=('',13)).place(x=1040, y=30)
Button(root, text='Read more...', width=11, bg='#CFDAC8',
       fg='black', font=('', 13)).place(x=1125, y=225)
Button(root, text='', width=2, bg='#DDBEBE',
       fg='black', font=('', 13)).place(x=1160, y=30)

op = pets(root)
photo = PhotoImage(file="")
root.mainloop()
