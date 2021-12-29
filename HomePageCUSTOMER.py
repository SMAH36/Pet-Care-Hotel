from tkinter import *
from tkinter import ttk
from typing import Mapping
from tkcalendar import *
from functools import partial
from database import database_connection
from database.database_connection import *
import tkinter as tk
from functions import *
from SignIn import *
import datetime


def ShowmeMyPets(USER):
    Pets = getPetsByUSERid(USER.userID)
    PetsList = []
    if(len(Pets) == 0):
        popupmsg('You have no pets ,please add one ')
    else:
        tktk = Toplevel(root)
        tktk.title("AddPetPage")
        tktk.state("zoomed")
        for p in Pets:
            PetsList.append(p[0].replace('(', '').replace(')', '').split(','))
        dec = {}
        # for i in range(len(Pets)):

        # Pets={}
        # Pets=dec.keys()
        # print(Pets)
        # scrollbar

        Pets_scroll = Scrollbar(tktk)
        Pets_scroll.pack(side=RIGHT, fill=Y)

        Pets_scroll = Scrollbar(tktk, orient='horizontal')
        Pets_scroll.pack(side=BOTTOM, fill=X)

        my_game = ttk.Treeview(
            tktk, yscrollcommand=Pets_scroll.set, xscrollcommand=Pets_scroll.set)

        my_game.pack()

        Pets_scroll.config(command=my_game.yview)
        Pets_scroll.config(command=my_game.xview)

        # define our column

        my_game['columns'] = ('ID', 'Pet name', 'Type', 'Gender', 'Age')

        # format our column
        my_game.column("#0", width=0,  stretch=NO)
        my_game.column("ID", anchor=CENTER, width=80)
        my_game.column("Pet name", anchor=CENTER, width=80)
        my_game.column("Type", anchor=CENTER, width=80)
        my_game.column("Gender", anchor=CENTER, width=80)
        my_game.column("Age", anchor=CENTER, width=80)

        # Create Headings
        my_game.heading("#0", text="", anchor=CENTER)
        my_game.heading("ID", text="ID", anchor=CENTER)
        my_game.heading("Pet name", text="Pets' name", anchor=CENTER)
        my_game.heading("Type", text="Type", anchor=CENTER)
        my_game.heading("Gender", text="Gender", anchor=CENTER)
        my_game.heading("Age", text="Age", anchor=CENTER)


def popupPricemsg(f, date1, date2, tkvar):
    if tkvar == 'None':
        popupmsg('You have to choose one of your pets to continue')
    else:
        D1 = tuple(map(lambda x: int(x), (date1.split('/'))))
        D2 = tuple(map(lambda x: int(x), (date2.split('/'))))
        print(D1)
        d1 = datetime.datetime(D1[2], D1[1], D1[0])
        print(d1)
        d2 = datetime.datetime(D2[2], D2[1], D2[0])
        if(d2 < d1):
            popup = tk.Toplevel()
            popup.title("!")
            # Can add a font arg here
            label = tk.Label(
                popup, text='Your check out date must be after your check in date !')
            label.pack(side="top", fill="x", pady=10)
            B2 = tk.Button(popup, text="Okay", command=popup.destroy)
            B2.pack()
        else:
            def Helpfun():
                popup.destroy()
                f()

            price = ((d2-d1).days+1)*77
            popup = tk.Toplevel()
            popup.title("!")
            # Can add a font arg here
            label = tk.Label(popup, text='Total price : {0}'.format(price))
            label.pack(side="top", fill="x", pady=10)
            B1 = tk.Button(popup, text="Okay", command=Helpfun)
            B1.pack()
            B2 = tk.Button(popup, text="Canacel", command=popup.destroy)
            B2.pack()


def PetAgeVaildetor(x):
    count = 0
    for i in range(len(x)):
        if(x[i] > '9' or x[i] < '0'):
            return False
    return True


def Reservation(USER):
    tktk = Toplevel(root)
    tktk.title("Reservation")
    tktk.geometry("1080x1920")
    Pets = database_connection.getPetsByUSERid(USER.userID)
    PetsList = []
    if(len(Pets) == 0):
        popupmsg('You have no pets ,please add one ')
        tktk.destroy()
    for p in Pets:
        PetsList.append(p[0].replace('(', '').replace(')', '').split(','))
    dec = {}
    for p in PetsList:
        dec[p[0]+'('+p[1]+')'] = p[2]
        print(p[0]+'('+p[1]+')')
        print(p[2])
    Pets = {}
    Pets = dec.keys()
    print(Pets)
    tkvar = StringVar(root)
    tkvar.set('None')  # set the default option
    # on change dropdown value

    def change_dropdown(*args):
        print(tkvar.get())
    label_Type = Label(tktk, text="Pet-('Name'('Type'))",
                       width=20, font=("bold", 10))
    # label_Type.place(x=80, y=160)
    label_Type.pack(pady=20)

    text_Type = OptionMenu(tktk, tkvar, *Pets)
    # text_Type.place(x=240, y=160)
    text_Type.pack(pady=20)
    date_object = datetime.date.today()
    print(date_object.day)
    cal1 = Calendar(tktk, selectmode='day', year=date_object.year,
                    month=date_object.month, day=date_object.day)
    cal1.pack(pady=20)
    cal2 = Calendar(tktk, selectmode='day', year=date_object.year,
                    month=date_object.month, day=date_object.day)
    cal2.pack(pady=20)

    def grad_date(x):
        date.config(text="Selected Date is: " + x.get_date())
    # Add Button and Label
    Button(tktk, text="Get ChekIn Date",
           command=lambda: grad_date(cal1)).pack(pady=20)
    Button(tktk, text="Get CheckOut Date",
           command=lambda: grad_date(cal2)).pack(pady=20)

    date = Label(tktk, text="")
    date.pack(pady=20)

    def ReservePage():
        ReservedRooms = tuple(map(lambda x: int(
            x[0]), database_connection.reservedRoomsByDate(cal1.get_date(), cal2.get_date())))
        flag = True
        for i in range(1, 78):
            flag = False
            if i not in ReservedRooms:
                if(reserveRoom(i, dec[tkvar.get()], cal1.get_date(), cal2.get_date())):
                    tktk.destroy()
                    popupmsg("Your reservation has been succseffuly submited ;)")
                    flag = True
                    break

        if flag == False:
            popupmsg("Your reservation has been failed please select another date")

    Button(tktk, command=lambda: popupPricemsg(ReservePage, cal1.get_date(), cal2.get_date(
    ), tkvar.get()), text='Submit', width=20, bg='brown', fg='white').place(x=180, y=380)


def AddPetPage(USER):
    # Dictionary with options
    PetsTypes = {
        'Dog',
        'Cat',
        'Bird',
        'Fish',
        'Snake',
        'Hamester'
    }
    tkvar = StringVar(root)
    tkvar.set('Dog')  # set the default option
    # on change dropdown value

    def change_dropdown(*args):
        print(tkvar.get())

    # link function to change dropdown
    tkvar.trace('w', change_dropdown)
    tktk = Toplevel(root)
    tktk.title("AddPetPage")
    tktk.geometry("500x500")

    label_name = Label(tktk, text="Name", width=20, font=("bold", 10))
    label_name.place(x=80, y=130)

    text_name = Entry(tktk)
    text_name.place(x=240, y=130)

    label_Type = Label(tktk, text="Type", width=20, font=("bold", 10))
    label_Type.place(x=80, y=160)

    text_Type = OptionMenu(tktk, tkvar, *PetsTypes)
    text_Type.place(x=240, y=160)

    label_id = Label(tktk, text="Id", width=20, font=("bold", 10))
    label_id.place(x=68, y=190)

    text_id = Entry(tktk)
    text_id.place(x=240, y=190)

    label_gender = Label(tktk, text="Gender", width=20, font=("bold", 10))
    label_gender.place(x=70, y=250)
    var = IntVar()
    Radiobutton(tktk, text="Male", padx=5, variable=var,
                value=1).place(x=235, y=250)
    Radiobutton(tktk, text="Female", padx=20,
                variable=var, value=2).place(x=290, y=250)

    label_age = Label(tktk, text="Age:", width=20, font=("bold", 10))
    label_age.place(x=70, y=300)

    entry_age = Entry(tktk)
    entry_age.place(x=240, y=300)

    def buttonClick():
        flag = True
        if len(text_name.get()) < 3:
            flag = False
            popupmsg('Name must be at least 3 letters . . . ')
        if(var.get() == 0 and flag == True):
            flag = False
            popupmsg('Must choose gender ! ! !')
        if(PetAgeVaildetor(entry_age.get()) == False and flag == True):
            flag = False
            popupmsg('>> age must contain only numbers <<')
        if (PetAgeVaildetor(text_id.get()) == False):
            flag = False
            popupmsg('>> ID must contain only numbers <<')
        elif(flag == True):
            if var.get() == 1:
                gender = 'male'
            else:
                gender = 'female'
            if(database_connection.addPet(USER.userID, text_name.get(), tkvar.get(), entry_age.get(), gender, text_id.get()) == True):
                popupmsg('Your pet has been successfuly added :)')
                tktk.destroy()
            else:
                popupmsg('Pet"s ID already exist')

    Button(tktk, command=buttonClick, text='Submit', width=20,
           bg='brown', fg='white').place(x=180, y=380)

 # it is use for display the registration form on the window
    tktk.mainloop()
    print("registration form  seccussfully created...")


def homepageCUSTOMER(USER):
    CustomerHomePage = Toplevel(root)
    CustomerHomePage.title("Home Page")
    CustomerHomePage.geometry("200x200")
    Button(CustomerHomePage, text="My pets",
           command=lambda: ShowmeMyPets(USER)).grid(column=0, row=2)
    Button(CustomerHomePage, text="Reservation",
           command=lambda: Reservation(USER)).grid(column=0, row=1)
    Button(CustomerHomePage, text="AddPet",
           command=lambda: AddPetPage(USER)).grid(column=2, row=0)
    Button(CustomerHomePage, text="Quit",
           command=root.destroy).grid(column=0, row=0)
    signOut(CustomerHomePage)
