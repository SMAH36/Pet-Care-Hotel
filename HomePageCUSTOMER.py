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
# def deletePet():
###


def ReservationHistory(USER):
    #{'room_number': '2', 'start_date': '2021-10-10', 'end_date': '2021-10-12'}
    Reserevations = getCustomerHistory(USER.userID)

    newWindow = Toplevel(root)
    newWindow.attributes('-fullscreen', True)
    newWindow.configure(background='#E9E9E5')
    topLabel = Label(newWindow, text='', width=90, bg='#D4D6C8',
                     fg='black', font=('Verdana Pro Black', 30))
    topLabel.pack(side=TOP)
    table_frame = Frame(newWindow, bg='#5C715E', pady=20, padx=20)
    table_frame.pack(side=TOP, pady=40)
    bottomLabel = Label(newWindow, text='', width=90, bg='#D4D6C8',
                        fg='black', font=('Verdana Pro Black', 30))
    bottomLabel.pack(side=BOTTOM)

    Pets_scroll = Scrollbar(table_frame, orient='vertical')
    Pets_scroll.pack(side=RIGHT, fill=Y)

    Pets_scroll = Scrollbar(table_frame, orient='horizontal')
    Pets_scroll.pack(side=BOTTOM, fill=X)

    my_game = ttk.Treeview(
        table_frame, yscrollcommand=Pets_scroll.set, xscrollcommand=Pets_scroll.set)
    my_game.pack()

    Pets_scroll.config(command=my_game.yview)
    Pets_scroll.config(command=my_game.xview)

    # define our column

    my_game['columns'] = ('Room number', 'Checkin date',
                          'Checkout date', 'Total amount')

    # format our column
    wid = 180
    my_game.column("#0", width=0,  stretch=NO)
    my_game.column("Room number", anchor=CENTER, width=wid)
    my_game.column("Checkin date", anchor=CENTER, width=wid)
    my_game.column("Checkout date", anchor=CENTER, width=wid)
    my_game.column("Total amount", anchor=CENTER, width=wid)

    # Create Headings
    my_game.heading("#0", text="", anchor=CENTER)
    my_game.heading("Room number", text="Room number", anchor=CENTER)
    my_game.heading("Checkin date", text="Checkin date", anchor=CENTER)
    my_game.heading("Checkout date", text="Checkout date", anchor=CENTER)
    my_game.heading("Total amount", text="Total amount", anchor=CENTER)

    iidd = 0
    Button(newWindow, command=newWindow.destroy, text='<-Back',
           width=10, bg='#5C715E', fg='white', font=("bold", 12)).place(x=1, y=1)

    def addData(RoomNumber, Firstdate, Lastdate, TotalAmount):
        nonlocal iidd
        my_game.insert(parent='', index='end', iid=iidd, text='',
                       values=(RoomNumber, Firstdate, Lastdate, TotalAmount))
        iidd += 1

    for i in Reserevations:
        D1 = tuple(map(lambda x: int(x), list(i['start_date'].split('-'))))
        D2 = tuple(map(lambda x: int(x), list(i['end_date'].split('-'))))
        d1 = datetime.datetime(D1[0], D1[1], D1[2])
        d2 = datetime.datetime(D2[0], D2[1], D2[2])
        price = ((d2-d1).days+1)*77
        addData(i['room_number'], i['start_date'], i['end_date'], price)
    my_game.pack()

# def ReservationHistory(USER):
#        Reserevations=getRoomHistory(USER.userID)
#        print(Reserevations)

#        newWindow = Toplevel(root)
#        newWindow.state('zoomed')

#        Pets_scroll= Scrollbar(newWindow)
#        Pets_scroll.pack(side=RIGHT, fill=Y)

#        Pets_scroll = Scrollbar(newWindow,orient='horizontal')
#        Pets_scroll.pack(side= BOTTOM,fill=X)

#        my_game = ttk.Treeview(newWindow,yscrollcommand=Pets_scroll.set, xscrollcommand =Pets_scroll.set)
#        my_game.pack()

#        Pets_scroll.config(command=my_game.yview)
#        Pets_scroll.config(command=my_game.xview)

#        #define our column

#        my_game['columns'] = ('Room number', 'Checkin date', 'Checkout date','Total amount')

#        # format our column
#        my_game.column("#0", width=0,  stretch=NO)
#        my_game.column("Room number",anchor=CENTER, width=80)
#        my_game.column("Checkin date",anchor=CENTER,width=80)
#        my_game.column("Checkout date",anchor=CENTER,width=80)
#        my_game.column("Total amount",anchor=CENTER, width=80)


#        #Create Headings
#        my_game.heading("#0",text="",anchor=CENTER)
#        my_game.heading("Room number",text="Room number",anchor=CENTER)
#        my_game.heading("Checkin date",text="Checkin date",anchor=CENTER)
#        my_game.heading("Checkout date",text="Checkout date",anchor=CENTER)
#        my_game.heading("Total amount",text="Total amount",anchor=CENTER)


#        iidd=0
#        Button(newWindow, command=newWindow.destroy, text='Quit page', width=20, bg='brown',fg='white').place(x=100, y=200)
#        def addData(RoomNumber,Firstdate,Lastdate,TotalAmount):
#               nonlocal iidd
#               my_game.insert(parent='',index='end',iid=iidd,text='',values=(RoomNumber,Firstdate,Lastdate,TotalAmount))
#               iidd+=1


#        for i in Reserevations:
#               D1=list(Reserevations['start_date'].split('-'))
#               D2=list(Reserevations['end_date'].split('-'))
#               d1=datetime.datetime(D1[2],D1[0],D1[1])
#               d2=datetime.datetime(D2[2],D2[0],D2[1])
#               price=((d2-d1).days+1)*77
#               print(i)
#               addData(i['room_number'],i['start_date'],i['end_date'],str(price))

def ShowmeMyPets(USER):
    Pets = getPetsByUSERid(USER.userID)
    PetsList = []
    if(len(Pets) == 0):
        popupmsg('You have no pets ,please add one')
    else:
        tktk = Toplevel(root)
        tktk.title("Add Pet Page")
        tktk.attributes('-fullscreen', True)
        tktk.configure(background='#E9E9E5')
        topLabel = Label(tktk, text='', width=90, bg='#D4D6C8',
                         fg='black', font=('Verdana Pro Black', 30))
        topLabel.pack(side=TOP)
        Label(tktk, text="My Pets", width=20, bg='#E9E9E5', fg='black',
              font=("Elephant", 20)).pack(side=TOP, pady=20)
        table_frame = Frame(tktk, bg='#5C715E', pady=20, padx=20)
        table_frame.pack(side=TOP, padx=20)
        bottomLabel = Label(tktk, text='', width=90, bg='#D4D6C8',
                            fg='black', font=('Verdana Pro Black', 30))
        bottomLabel.pack(side=BOTTOM)

        # scrollbar
        Pets_scroll = Scrollbar(table_frame)
        Pets_scroll.pack(side=RIGHT, fill=Y)

        Pets_scroll = Scrollbar(table_frame, orient='horizontal')
        Pets_scroll.pack(side=BOTTOM, fill=X)

        my_game = ttk.Treeview(
            table_frame, yscrollcommand=Pets_scroll.set, xscrollcommand=Pets_scroll.set)

        my_game.pack()

        Pets_scroll.config(command=my_game.yview)
        Pets_scroll.config(command=my_game.xview)

        # define our column

        my_game['columns'] = ('ID', 'Pet name', 'Type', 'Gender', 'Age')

        # format our column
        wid = 150
        my_game.column("#0", width=0,  stretch=NO)
        my_game.column("ID", anchor=CENTER, width=wid)
        my_game.column("Pet name", anchor=CENTER, width=wid)
        my_game.column("Type", anchor=CENTER, width=wid)
        my_game.column("Gender", anchor=CENTER, width=wid)
        my_game.column("Age", anchor=CENTER, width=wid)

        # Create Headings
        my_game.heading("#0", text="", anchor=CENTER)
        my_game.heading("ID", text="ID", anchor=CENTER)
        my_game.heading("Pet name", text="Pets' name", anchor=CENTER)
        my_game.heading("Type", text="Type", anchor=CENTER)
        my_game.heading("Gender", text="Gender", anchor=CENTER)
        my_game.heading("Age", text="Age", anchor=CENTER)
        iidd = 0

        def addData(ID, PetName, Type, Gender, Age):
            nonlocal iidd
            my_game.insert(parent='', index='end', iid=iidd,
                           text='', values=(ID, PetName, Type, Gender, Age))
            iidd += 1

        for p in Pets:
            PetsList.append(p[0].replace('(', '').replace(')', '').split(','))

        for i in PetsList:
            addData(i[5], i[0], i[1], i[4], i[3])
        Button(tktk, text="<-Back", command=tktk.destroy, width=13,
               bg='#5C715E', fg='white', font=("bold", 12)).place(x=1, y=1)
        tktk.mainloop()


def popupPricemsg(f, date1, date2, tkvar, USER):
    if tkvar == 'None':
        popupmsg('Please choose pet before proceed to the next step')
    else:
        D1 = tuple(map(lambda x: int(x), (date1.split('/'))))
        D2 = tuple(map(lambda x: int(x), (date2.split('/'))))
        d1 = datetime.datetime(D1[2], D1[0], D1[1])
        d2 = datetime.datetime(D2[2], D2[0], D2[1])
        if(d2 < d1):
            popup = tk.Toplevel()
            popup.title("!")
            # Can add a font arg here
            label = tk.Label(
                popup, text='Your check-out date must be after your check-in date!')
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
            label = tk.Label(
                popup, text=f"I'm {USER.name} {USER.lastName} with ID number {USER.personalId}\nI agree to pay {price} nis at the reception before {date1}")
            label.pack(side="top", fill="x", pady=10)
            B1 = tk.Button(popup, text="I Agree", command=Helpfun)
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
    tktk.attributes('-fullscreen', True)
    tktk.configure(background='#E9E9E5')
    topLabel = Label(tktk, text='', width=90, bg='#D4D6C8',
                     fg='black', font=('Verdana Pro Black', 30))
    topLabel.pack(side=TOP)
    Label(tktk, text="My Reservation", width=20, bg='#E9E9E5',
          fg='black', font=("Elephant", 20)).pack(side=TOP, pady=20)
    bottomLabel = Label(tktk, text='', width=90, bg='#D4D6C8',
                        fg='black', font=('Verdana Pro Black', 30))
    bottomLabel.pack(side=BOTTOM)
    Button(tktk, command=lambda: popupPricemsg(ReservePage, cal1.get_date(), cal2.get_date(
    ), tkvar.get(), USER), text='Submit', width=20, bg='#5C715E', fg='white', font=("bold", 18)).pack(side=BOTTOM, pady=20)

    Pets = database_connection.getPetsByUSERid(USER.userID)
    PetsList = []
    if(len(Pets) == 0):
        popupmsg('You have no pets, please add one')
        tktk.destroy()
    for p in Pets:
        PetsList.append(p[0].replace('(', '').replace(')', '').split(','))
    dec = {}
    for p in PetsList:
        dec[p[0]+'('+p[1]+')'] = p[2]
    Pets = {}
    Pets = dec.keys()
    # on change dropdown value
    tkvar = StringVar(root)
    tkvar.set('Choose Pet')

    def change_dropdown(*args):
        tkvar.get()
    tkvar.trace('w', change_dropdown)

    text_Type = OptionMenu(tktk, tkvar, *Pets)
    text_Type.pack(pady=20)
    text_Type.config(width=20, font=("", 18))
    text_Type.pack(side=BOTTOM, pady=100)

    menu = root.nametowidget(text_Type.menuname)
    menu.config(font=20)

    date_object = datetime.date.today()
    cal1 = Calendar(tktk, selectmode='day', year=date_object.year,
                    month=date_object.month, day=date_object.day)
    cal1.pack(pady=20)
    cal2 = Calendar(tktk, selectmode='day', year=date_object.year,
                    month=date_object.month, day=date_object.day)
    cal2.pack(pady=20)

    date = Label(tktk, text="")
    date.pack(pady=20)

    def ReservePage():
        ReservedRooms = tuple(map(lambda x: int(
            x[0]), database_connection.reservedRoomsByDate(cal1.get_date(), cal2.get_date())))
        flag = True
        for i in range(1, 78):
            flag = False
            if i not in ReservedRooms:
                if(reserveRoom(i, dec[tkvar.get()], USER.userID, cal1.get_date(), cal2.get_date())):
                    tktk.destroy()
                    popupmsg("Your reservation has been successfully submitted")
                    flag = True
                    break

        if flag == False:
            popupmsg("Your reservation has been failed please select another date")

    Button(tktk, command=tktk.destroy, text="<-Back", width=10,
           bg='#5C715E', fg='white', font=("bold", 12)).place(x=1, y=1)


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
        tkvar.get()

    # link function to change dropdown
    tkvar.trace('w', change_dropdown)
    tktk = Toplevel(root)
    tktk.title("AddPetPage")
    tktk.attributes('-fullscreen', True)
    tktk.configure(background='#E9E9E5')
    Label(tktk, text="Add Pet", width=20, bg='#E9E9E5',
          fg='black', font=("Elephant", 17)).place(x=450, y=90)
    topLabel = Label(tktk, text='', width=90, bg='#D4D6C8',
                     fg='black', font=('Verdana Pro Black', 30))
    topLabel.pack(side=TOP)
    bottomLabel = Label(tktk, text='', width=90, bg='#D4D6C8',
                        fg='black', font=('Verdana Pro Black', 30))
    bottomLabel.pack(side=BOTTOM)

    label_name = Label(tktk, text="Name", width=20,
                       bg='#E9E9E5', fg='black', font=("bold", 15))
    label_name.place(x=473, y=180)

    text_name = Entry(tktk)
    text_name.place(x=650, y=180)

    label_Type = Label(tktk, text="Type", width=20,
                       bg='#E9E9E5', fg='black', font=("bold", 15))
    label_Type.place(x=471, y=220)

    text_Type = OptionMenu(tktk, tkvar, *PetsTypes)
    text_Type.place(x=650, y=220)

    label_id = Label(tktk, text="Id", width=20, bg='#E9E9E5',
                     fg='black', font=("bold", 15))
    label_id.place(x=457, y=260)

    text_id = Entry(tktk, width=20)
    text_id.place(x=650, y=260)

    label_gender = Label(tktk, text="Gender", width=20,
                         bg='#E9E9E5', fg='black', font=("bold", 15))
    label_gender.place(x=480, y=300)
    var = IntVar()
    Radiobutton(tktk, text="Male", padx=5, variable=var, bg='#E9E9E5', fg='black',
                value=1).place(x=650, y=300)
    Radiobutton(tktk, text="Female", padx=20, bg='#E9E9E5', fg='black',
                variable=var, value=2).place(x=730, y=300)

    label_age = Label(tktk, text="Age", width=20,
                      bg='#E9E9E5', fg='black', font=("bold", 15))
    label_age.place(x=473, y=340)

    entry_age = Entry(tktk)
    entry_age.place(x=650, y=340)

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

    Button(tktk, command=buttonClick, text='Submit', width=15,
           bg='#5C715E', fg='white', font=("", 12)).place(x=570, y=500)
    Button(tktk, command=tktk.destroy, text="<-Back", width=10,
           bg='#5C715E', fg='white', font=("bold", 12)).place(x=1, y=1)
 # it is use for display the registration form on the window
    tktk.mainloop()


def homepageCUSTOMER(USER):
    CustomerHomePage = Toplevel(root)
    CustomerHomePage.title("Home Page")
    CustomerHomePage.attributes('-fullscreen', True)
    CustomerHomePage.configure(background='#E9E9E5')
    Label(CustomerHomePage, text="Customer Homepage:", width=20,
          bg='#E9E9E5', fg='black', font=("Elephant", 20)).place(x=50, y=120)
    topLabel = Label(CustomerHomePage, text='', width=90,
                     bg='#D4D6C8', fg='black', font=('Verdana Pro Black', 30))
    topLabel.pack(side=TOP)
    bottomLabel = Label(CustomerHomePage, text='', width=90,
                        bg='#D4D6C8', fg='black', font=('Verdana Pro Black', 30))
    bottomLabel.pack(side=BOTTOM)
    Button(CustomerHomePage, text="My pets", width=20, bg='#D4D6C8', fg='black', font=('Elephant', 15),
           command=lambda: ShowmeMyPets(USER)).place(x=250, y=200)
    Button(CustomerHomePage, text="Reservation", width=20, bg='#D4D6C8', fg='black', font=('Elephant', 15),
           command=lambda: Reservation(USER)).place(x=250, y=270)
    Button(CustomerHomePage, text="AddPet", width=20, bg='#D4D6C8', fg='black', font=('Elephant', 15),
           command=lambda: AddPetPage(USER)).place(x=550, y=200)
    Button(CustomerHomePage, text="Quit", width=20, bg='#D4D6C8', fg='black', font=('Elephant', 15),
           command=root.destroy).place(x=450, y=400)
    Button(CustomerHomePage, text="Reservation history", width=20, bg='#D4D6C8', fg='black', font=('Elephant', 15),
           command=lambda: ReservationHistory(USER)).place(x=550, y=270)
    signOut(CustomerHomePage)
