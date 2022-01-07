from tkinter import *
from functools import partial
from database import database_connection
from database.database_connection import *
import tkinter as tk
from functions import *
from tkinter import ttk
from datetime import date
import datetime


def showAllroomHistory(USER):
    newWindow = Toplevel(root)
    newWindow.attributes('-fullscreen', True)
    newWindow.configure(background='#E9E9E5')
    topLabel = Label(newWindow, text='', width=90, bg='#D4D6C8',
                     fg='black', font=('Verdana Pro Black', 30))
    topLabel.pack(side=TOP)
    Label(newWindow, text="Room history", width=35, bg='#E9E9E5',
          fg='black', font=("Elephant", 15)).pack(side=TOP, pady=20)
    table_frame = Frame(newWindow, bg='#5C715E', pady=20, padx=20)
    table_frame.pack(side=TOP, pady=40)
    bottomLabel = Label(newWindow, text='', width=90, bg='#D4D6C8',
                        fg='black', font=('Verdana Pro Black', 30))
    bottomLabel.pack(side=BOTTOM)

    today = date.today()
    todayDate = f'{today.month}/{today.day}/{today.year}'
    label_room = Label(newWindow, text="Enter room number:",
                       width=20, bg='#E9E9E5', fg='black', font=("bold", 18))
    label_room.pack(side=TOP, pady=20)

    text_room = Entry(newWindow, justify='center', font=('', 18))
    text_room.pack(side=TOP, pady=20)

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

    my_game['columns'] = ('Room number', 'Checkin date', 'Checkout date',
                          'Customer name', 'Customer lastname', 'Customer ID')

    # format our column
    wid = 200
    my_game.column("#0", width=0,  stretch=NO)
    my_game.column("Room number", anchor=CENTER, width=wid)
    my_game.column("Checkin date", anchor=CENTER, width=wid)
    my_game.column("Checkout date", anchor=CENTER, width=wid)
    my_game.column("Customer name", anchor=CENTER, width=wid)
    my_game.column("Customer lastname", anchor=CENTER, width=wid)
    my_game.column("Customer ID", anchor=CENTER, width=wid)

    # Create Headings
    my_game.heading("#0", text="", anchor=CENTER)
    my_game.heading("Room number", text="Room number", anchor=CENTER)
    my_game.heading("Checkin date", text="First date", anchor=CENTER)
    my_game.heading("Checkout date", text="Last date", anchor=CENTER)
    my_game.heading("Customer name", text="Room number", anchor=CENTER)
    my_game.heading("Customer lastname", text="First date", anchor=CENTER)
    my_game.heading("Customer ID", text="Last date", anchor=CENTER)

    iidd = 0

    def addData(RoomNumber, Firstdate, Lastdate, Customername, Customerlastname, CustomerID):
        nonlocal iidd
        my_game.insert(parent='', index='end', iid=iidd, text='', values=(
            RoomNumber, Firstdate, Lastdate, Customername, Customerlastname, CustomerID))
        iidd += 1

    def ReservationsDetails():
        Reserevations = getRoomHistory(text_room.get())
        for i in Reserevations:
            addData(i['room_number'], i['start_date'], i['end_date'],
                    i['user'][0], i['user'][1], i['user'][2])

    Button(newWindow, command=ReservationsDetails, text='Submit', width=20,
           bg='#5C715E', fg='white', font=("bold", 12)).pack(side=TOP, pady=50)
    Button(newWindow, command=newWindow.destroy, text="<-Back", width=10,
           bg='#5C715E', fg='white', font=("bold", 12)).place(x=1, y=1)


def showAllTodayReservation():
    # [('(1,2022-01-04,2022-01-05)',), ('(3,2022-01-04,2022-01-05)',),
    # ('(2,2022-01-05,2022-01-05)',), ('(4,2022-01-05,2022-01-06)',), ('(5,2022-01-03,2022-01-21)',)]
    newWindow = Toplevel(root)
    newWindow.attributes('-fullscreen', True)
    newWindow.configure(background='#E9E9E5')
    topLabel = Label(newWindow, text='', width=90, bg='#D4D6C8',
                     fg='black', font=('Verdana Pro Black', 30))
    topLabel.pack(side=TOP)
    Label(newWindow, text="List of booked rooms", width=35, bg='#E9E9E5',
          fg='black', font=("Elephant", 18)).pack(anchor=N, pady=50)
    table_frame = Frame(newWindow, bg='#5C715E', pady=20, padx=20)
    table_frame.pack(side=TOP, pady=0)
    bottomLabel = Label(newWindow, text='', width=90, bg='#D4D6C8',
                        fg='black', font=('Verdana Pro Black', 30))
    bottomLabel.pack(side=BOTTOM)
    today = date.today()
    todayDate = f'{today.month}/{today.day}/{today.year}'
    rooms = list(map(lambda x: list(x.replace('(', '').replace(')', '').split(
        ',')), (map(lambda x: x[0], getAllReservations(todayDate)))))
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

    my_game['columns'] = ('Room number', 'First data', 'Last date')

    # format our column
    wid = 150
    my_game.column("#0", width=0,  stretch=NO)
    my_game.column("Room number", anchor=CENTER, width=wid)
    my_game.column("First data", anchor=CENTER, width=wid)
    my_game.column("Last date", anchor=CENTER, width=wid)

    # Create Headings
    my_game.heading("#0", text="", anchor=CENTER)
    my_game.heading("Room number", text="Room number", anchor=CENTER)
    my_game.heading("First data", text="First date", anchor=CENTER)
    my_game.heading("Last date", text="Last date", anchor=CENTER)

    iidd = 0

    def addData(RoomNumber, Firstdate, Lastdate):
        nonlocal iidd
        my_game.insert(parent='', index='end', iid=iidd, text='',
                       values=(RoomNumber, Firstdate, Lastdate))
        iidd += 1
    for i in rooms:
        addData(i[0], i[1], i[2])
    Button(newWindow, command=newWindow.destroy, text="<-Back", width=10,
           bg='#5C715E', fg='white', font=("bold", 15)).place(x=1, y=1)


def showReservationDetailsByRoomNum():
    newWindow = Toplevel(root)
    newWindow.attributes('-fullscreen', True)
    newWindow.configure(background='#E9E9E5')
    topLabel = Label(newWindow, text='', width=90, bg='#D4D6C8',
                     fg='black', font=('Verdana Pro Black', 30))
    topLabel.pack(side=TOP)
    Label(newWindow, text="Details by Room Number", width=35,
          bg='#E9E9E5', fg='black', font=("Elephant", 20)).pack(anchor=N, pady=100)
    bottomLabel = Label(newWindow, text='', width=90, bg='#D4D6C8',
                        fg='black', font=('Verdana Pro Black', 30))
    bottomLabel.pack(side=BOTTOM)
    today = date.today()
    todayDate = f'{today.month}/{today.day}/{today.year}'
    Label(newWindow, text="Enter room number:", width=20,
          font=("bold", 18)).pack(anchor=N, pady=80)
    text_room = Entry(newWindow, justify='center', font=('', 20))
    text_room.pack(anchor=N, pady=0)

    def ReservationDetails():
        # ('(fff,Fish,33911706-c7b9-4451-9201-a1b8a1f5dac0,2,female,1231)',
        # (2, 'e8c6d15d-b029-4ff2-90cb-b0de8a2ec38c', 'malak', 'bta', '18', 'Male', '3151112128', 'customer'),
        #  , '2022-01-04', '2022-01-05')
        listall = getReservationInfoByRoomNumber(todayDate, text_room.get())
        if(listall):
            pet = list(listall[0].replace('(', '').replace(')', '').split(','))
            customer = listall[1]
            firstDate = listall[2]
            lastDate = listall[3]
            D1 = tuple(map(lambda x: int(x), list(firstDate.split('-'))))
            D2 = tuple(map(lambda x: int(x), list(lastDate.split('-'))))
            d1 = datetime.datetime(D1[0], D1[1], D1[2])
            d2 = datetime.datetime(D2[0], D2[1], D2[2])
            price = ((d2-d1).days+1)*77
            text = "{0} reservation details: ".format(text_room.get())
            text += ' Customer full name: ' + \
                str(customer[2]) + ' ' + str(customer[3]) + \
                ' | ID: '+str(customer[6]) + '\n'
            text += 'Start -- End date  : '+firstDate + ' -- '+lastDate + '\n'
            text += 'Pet name: '+pet[0] + \
                ' | Pet type: '+pet[1]+' | Pet ID: '+pet[5]
            text += '\nTotal paid : ' + str(price)
            popupmsg(text)
            newWindow.destroy()
        else:
            popupmsg('Currently there are no reservations for this room')

    Button(newWindow, command=ReservationDetails, text='Submit', width=20,
           bg='#5C715E', fg='white', font=("bold", 12)).pack(anchor=N, pady=50)
    Button(newWindow, command=newWindow.destroy, text="<-Back", width=10,
           bg='#5C715E', fg='white', font=("bold", 12)).place(x=1, y=1)


def showWorkers():
    newWindow = Toplevel(root)
    newWindow.attributes('-fullscreen', True)
    topLabel = Label(newWindow, text='', width=90, bg='#D4D6C8',
                     fg='black', font=('Verdana Pro Black', 30))
    topLabel.pack(side=TOP)
    Label(newWindow, text="List of wokers", width=35, bg='#E9E9E5',
          fg='black', font=("Elephant", 18)).pack(side=TOP, pady=20)
    table_frame = Frame(newWindow, bg='#5C715E', pady=20, padx=20)
    table_frame.pack(side=TOP, pady=20)
    newWindow.configure(background='#E9E9E5')
    bottomLabel = Label(newWindow, text='', width=90, bg='#D4D6C8',
                        fg='black', font=('Verdana Pro Black', 30))
    bottomLabel.pack(side=BOTTOM)
    customerList = []
    for c in database_connection.getAllWorkers1():
        firstName = c[0].replace('(', '').replace(')', '').split(',')[0]
        lastName = c[0].replace('(', '').replace(')', '').split(',')[1]
        age = c[0].replace('(', '').replace(')', '').split(',')[2]
        gender = c[0].replace('(', '').replace(')', '').split(',')[3]
        id = c[0].replace('(', '').replace(')', '').split(',')[4]
        customerList.append((firstName, lastName, age, gender, id))

    # scrollbar
    game_scroll = Scrollbar(table_frame)
    game_scroll.pack(side=RIGHT, fill=Y)

    game_scroll = Scrollbar(table_frame, orient='horizontal')
    game_scroll.pack(side=BOTTOM, fill=X)

    my_game = ttk.Treeview(
        table_frame, yscrollcommand=game_scroll.set, xscrollcommand=game_scroll.set)

    my_game.pack()

    game_scroll.config(command=my_game.yview)
    game_scroll.config(command=my_game.xview)

    # define our column

    my_game['columns'] = ('firstName', 'lastName',
                          'age', 'gender', 'personalId')

    # format our column
    my_game.column("#0", width=0,  stretch=NO)
    my_game.column("firstName", anchor=CENTER, width=120)
    my_game.column("lastName", anchor=CENTER, width=120)
    my_game.column("age", anchor=CENTER, width=120)
    my_game.column("gender", anchor=CENTER, width=120)
    my_game.column("personalId", anchor=CENTER, width=120)

    # Create Headings
    my_game.heading("#0", text="", anchor=CENTER)
    my_game.heading("firstName", text="First Name", anchor=CENTER)
    my_game.heading("lastName", text="Last Name", anchor=CENTER)
    my_game.heading("age", text="Age", anchor=CENTER)
    my_game.heading("gender", text="Gender", anchor=CENTER)
    my_game.heading("personalId", text="Personal Id", anchor=CENTER)

    # add data
    counter = 0
    for customer in customerList:
        my_game.insert(parent='', index='end', iid=counter, text='',
                       values=(customer))
        counter = counter + 1
    my_game.pack()
    Button(newWindow, command=newWindow.destroy, text="<-Back", width=10,
           bg='#5C715E', fg='white', font=("bold", 12)).place(x=1, y=1)


def ApproveTask(USER):
    newWindow = Toplevel(root)
    newWindow.attributes('-fullscreen', True)
    newWindow.configure(background='#E9E9E5')
    # Label(newWindow, text="List of wokers details",width=35,bg='#E9E9E5',fg='black', font=("Elephant", 15)).place(x=-20, y=60)
    topLabel = Label(newWindow, text='', width=90, bg='#D4D6C8',
                     fg='black', font=('Verdana Pro Black', 30))
    topLabel.pack(side=TOP)
    table_frame = Frame(newWindow, bg='#5C715E', pady=20, padx=20)
    table_frame.pack(side=TOP, pady=20)
    bottomLabel = Label(newWindow, text='', width=90, bg='#D4D6C8',
                        fg='black', font=('Verdana Pro Black', 30))
    bottomLabel.pack(side=BOTTOM)
    today = date.today()
    todayDate = f'{today.month}/{today.day}/{today.year}'
    rooms = list(map(lambda x: x[0], list(
        getUnapprovedCompletedTasks(todayDate))))
    # scrollbar
    game_scroll = Scrollbar(table_frame)
    game_scroll.pack(side=RIGHT, fill=Y)

    game_scroll = Scrollbar(table_frame, orient='horizontal')
    game_scroll.pack(side=BOTTOM, fill=X)

    my_game = ttk.Treeview(
        table_frame, yscrollcommand=game_scroll.set, xscrollcommand=game_scroll.set)

    my_game.pack()

    game_scroll.config(command=my_game.yview)
    game_scroll.config(command=my_game.xview)

    # define our column

    my_game['columns'] = ('room_number')

    # format our column
    my_game.column("#0", width=0,  stretch=NO)
    my_game.column("room_number", anchor=CENTER, width=450)

    # Create Headings
    my_game.heading("#0", text="", anchor=CENTER)
    my_game.heading("room_number", text="Room Number", anchor=CENTER)

    # add data
    counter = 0
    for room in rooms:
        my_game.insert(parent='', index='end',
                       iid=counter, text='', values=(room))
        counter = counter + 1
    label_rooms = Label(newWindow, text="Choose rooms:",
                        width=20, font=("bold", 18))
    label_rooms.pack(side=TOP, pady=80)
    text_rooms = Entry(newWindow, justify='center', font=('', 18))
    text_rooms.pack(side=TOP, pady=5)

    def buttonHandler():
        if (approveTask(todayDate, text_rooms.get(), USER.userID)):
            popupmsg("Your request has been succsefully sent")
            newWindow.destroy()
        else:
            popupmsg("Falied to send your request")

    Button(newWindow, command=buttonHandler, text='Submit', width=20,
           bg='#5C715E', fg='white', font=("", 18)).pack(side=BOTTOM, pady=100)
    Button(newWindow, text="<-Back", command=newWindow.destroy, width=10,
           bg='#5C715E', fg='white', font=("", 12)).place(x=1, y=1)


def AddWorkerPage():
    AddWorker = Toplevel(root)
    AddWorker.title("Add Worker")
    AddWorker.attributes('-fullscreen', True)
    AddWorker.configure(background='#E9E9E5')
    Label(AddWorker, text="To add the worker...\n Please enter his Email or phone number",
          width=35, bg='#E9E9E5', fg='black', font=("Elephant", 15)).place(x=60, y=120)
    topLabel = Label(AddWorker, text='', width=90, bg='#D4D6C8',
                     fg='black', font=('Verdana Pro Black', 30))
    topLabel.pack(side=TOP)
    topLabel = Label(AddWorker, text='', width=90, bg='#D4D6C8',
                     fg='black', font=('Verdana Pro Black', 30))
    topLabel.pack(side=TOP)
    bottomLabel = Label(AddWorker, text='', width=90, bg='#D4D6C8',
                        fg='black', font=('Verdana Pro Black', 30))
    bottomLabel.pack(side=BOTTOM)
    Button(AddWorker, text="<-Back", width=10, bg='#5C715E', fg='white',
           font=("bold", 12), command=AddWorker.destroy).place(x=0, y=0)

    label_email = Label(AddWorker, text="Email or Phone", bg='#E9E9E5', fg='black',
                        width=16, font=("bold", 16))
    label_email.place(x=430, y=300)
    text_email = Entry(AddWorker, width=20, font=("", 16))
    text_email.place(x=630, y=300)

    def buttonClick():
        flag = True
        if (flag == True and database_connection.checkIfUserExist(text_email.get()) == 0):
            flag = False
            popupmsg('Email Address not Exist!')
        if (flag == True and database_connection.checkIfUserExist(text_email.get()) == 0):
            flag = False
            popupmsg('Phone Number not Exist!')
        elif(flag == True):
            database_connection.userPromotion(text_email.get())
            popupmsg('You have added ' + text_email.get() +
                     'successfuly to workers')

    Button(AddWorker, command=buttonClick, text='Add Worker', width=18,
           bg='#5C715E', fg='white', font=("", 11)).place(x=660, y=370)


def DeleteWorkerPage():
    DeleteWorker = Toplevel(root)
    DeleteWorker.title("Delete Worker")
    DeleteWorker.attributes('-fullscreen', True)
    DeleteWorker.configure(background='#E9E9E5')
    Label(DeleteWorker, text="To delete the worker...\n Please enter his Email or phone number",
          width=35, bg='#E9E9E5', fg='black', font=("Elephant", 15)).place(x=60, y=120)
    topLabel = Label(DeleteWorker, text='', width=90, bg='#D4D6C8',
                     fg='black', font=('Verdana Pro Black', 30))
    topLabel.pack(side=TOP)
    bottomLabel = Label(DeleteWorker, text='', width=90,
                        bg='#D4D6C8', fg='black', font=('Verdana Pro Black', 30))
    bottomLabel.pack(side=BOTTOM)
    Button(DeleteWorker, text="<-Back", width=10, bg='#5C715E', fg='white', font=("bold", 12),
           command=DeleteWorker.destroy).place(x=0, y=0)
    label_email = Label(DeleteWorker, text="Email or Phone", bg='#E9E9E5', fg='black',
                        width=16, font=("bold", 16))
    label_email.place(x=430, y=300)
    text_email = Entry(DeleteWorker, width=20, font=("", 16))
    text_email.place(x=630, y=300)

    def buttonClick():
        flag = True
        if (flag == True and database_connection.checkIfUserExist(text_email.get()) == 0):
            flag = False
            popupmsg('Email Address not Exist!')
        if (flag == True and database_connection.checkIfUserExist(text_email.get()) == 0):
            flag = False
            popupmsg('Phone Number not Exist!')
        elif(flag == True):
            database_connection.removeUser(text_email.get())
            popupmsg('You have removed ' + text_email.get() +
                     'successfuly from workers')

    Button(DeleteWorker, command=buttonClick, text='Delete worker',
           width=18, bg='#5C715E', fg='white', font=("", 11)).place(x=660, y=370)


def chooseWorkerRoom():
    newWindow = Toplevel(root)
    newWindow.attributes('-fullscreen', True)
    newWindow.configure(background='#E9E9E5')
    table_frame = Frame(newWindow, bg='#5C715E', pady=20, padx=20)
    table_frame.pack(side=LEFT, padx=100)
    Label(newWindow, text="List of Rooms (Not Assigned Yet)", width=25,
          bg='#E9E9E5', fg='black', font=("", 19)).place(x=100, y=250)
    topLabel = Label(newWindow, text='', width=90, bg='#D4D6C8',
                     fg='black', font=('Verdana Pro Black', 30))
    topLabel.pack(side=TOP)
    bottomLabel = Label(newWindow, text='', width=90, bg='#D4D6C8',
                        fg='black', font=('Verdana Pro Black', 30))
    bottomLabel.pack(side=BOTTOM)
    dec = {}
    for w in database_connection.getAllWorkers():
        name = w[0].replace('(', '').replace(')', '').split(',')[1]
        pId = w[0].replace('(', '').replace(')', '').split(',')[2]
        user_id = w[0].replace('(', '').replace(')', '').split(',')[0]
        dec[f'{name}-{pId}'] = user_id
    listOfWorker = dec.keys()

    today = date.today()
    todayDate = f'{today.month}/{today.day}/{today.year}'
    listOfResRooms = []
    for rooms in tuple(map(lambda x: (x[0]), database_connection.reservedRoomsByDate(todayDate, todayDate))):
        listOfResRooms.append(rooms)

    listOfWorkersRooms = []
    for rooms in tuple(map(lambda x: (x[0]), database_connection.getAllRoomsWorkers(todayDate))):
        listOfWorkersRooms.append(rooms)

    relaventList = list(
        filter(lambda x: x not in listOfWorkersRooms, listOfResRooms))

    tkvar = StringVar(root)
    tkvar.set('Choose Worker')

    def change_dropdown(*args):
        tkvar.get()
    tkvar.trace('w', change_dropdown)

    text_Type = OptionMenu(newWindow, tkvar, *listOfWorker)
    text_Type.config(width=20, font=("", 11))
    text_Type.place(x=570, y=300)

    menu = root.nametowidget(text_Type.menuname)
    menu.config(font=20)

    # scrollbar
    game_scroll = Scrollbar(table_frame)
    game_scroll.pack(side=RIGHT, fill=Y)

    game_scroll = Scrollbar(table_frame, orient='horizontal')
    game_scroll.pack(side=BOTTOM, fill=X)

    my_game = ttk.Treeview(
        table_frame, yscrollcommand=game_scroll.set, xscrollcommand=game_scroll.set)

    my_game.pack()

    game_scroll.config(command=my_game.yview)
    game_scroll.config(command=my_game.xview)

    # define our column

    my_game['columns'] = ('room_number')

    # format our column
    my_game.column("#0", width=0,  stretch=NO)
    my_game.column("room_number", anchor=CENTER, width=400)

    # Create Headings
    my_game.heading("#0", text="", anchor=CENTER)
    my_game.heading("room_number", text="Room Number", anchor=CENTER)

    # add data
    counter = 0
    for room in relaventList:
        my_game.insert(parent='', index='end',
                       iid=counter, text='', values=(room))
        counter = counter + 1
    label_rooms = Label(newWindow, text="Choose rooms:",
                        width=15, bg='#E9E9E5', fg='black', font=("bold", 17))
    label_rooms.place(x=800, y=300)
    text_rooms = Entry(newWindow, width=20, font=("bold", 20))
    text_rooms.place(x=1000, y=300)

    def buttonHandler():
        rooms = list(text_rooms.get().split(','))
        if (setWorkerToRoom(todayDate, list(filter(lambda x: x in relaventList, rooms)), dec[tkvar.get()])):
            popupmsg("Rooms has been succsefully seted")
            newWindow.destroy()
        else:
            popupmsg("Falied to set rooms")

    Button(newWindow, command=buttonHandler, text='Submit', width=17,
           bg='#5C715E', fg='white', font=("", 16)).place(x=850, y=400)
    # Button(newWindow, text="Quit", command=newWindow.destroy).grid(column=0, row=0)
    Button(newWindow, command=newWindow.destroy, text="<-Back", width=10,
           bg='#5C715E', fg='white', font=("bold", 12)).place(x=1, y=1)


def ChangeWorkerRoom():
    newWindow = Toplevel(root)
    newWindow.attributes('-fullscreen', True)
    newWindow.configure(background='#E9E9E5')
    topLabel = Label(newWindow, text='', width=90, bg='#D4D6C8',
                     fg='black', font=('Verdana Pro Black', 30))
    topLabel.pack(side=TOP)
    Label(newWindow, text="List of rooms", width=35, bg='#E9E9E5',
          fg='black', font=("", 15)).pack(side=TOP, pady=20)
    table_frame = Frame(newWindow, bg='#5C715E', pady=20, padx=20)
    table_frame.pack(side=TOP, padx=20)
    bottomLabel = Label(newWindow, text='', width=90, bg='#D4D6C8',
                        fg='black', font=('Verdana Pro Black', 30))
    bottomLabel.pack(side=BOTTOM)
    Label(newWindow, text="To change worker room =>", width=35,
          bg='#E9E9E5', fg='black', font=("", 13)).pack(side=TOP, pady=20)
    dec = {}
    for w in database_connection.getAllWorkers():
        name = w[0].replace('(', '').replace(')', '').split(',')[1]
        pId = w[0].replace('(', '').replace(')', '').split(',')[2]
        user_id = w[0].replace('(', '').replace(')', '').split(',')[0]
        dec[f'{name}-{pId}'] = user_id
    listOfWorker = dec.keys()

    today = date.today()
    todayDate = f'{today.month}/{today.day}/{today.year}'
    listOfWorkersRooms = []
    for rooms in tuple(map(lambda x: (x[0]), database_connection.getAllRoomsWorkers(todayDate))):
        listOfWorkersRooms.append(rooms)

    tkvar = StringVar(root)
    tkvar.set('Choose Worker')

    def change_dropdown(*args):
        tkvar.get()
    tkvar.trace('w', change_dropdown)

    text_Type = OptionMenu(newWindow, tkvar, *listOfWorker)
    text_Type.pack(side=TOP, pady=20)
    text_Type.config(width=20, font=("", 11))

    menu = root.nametowidget(text_Type.menuname)
    menu.config(font=20)

    # scrollbar
    game_scroll = Scrollbar(table_frame)
    game_scroll.pack(side=RIGHT, fill=Y)

    game_scroll = Scrollbar(table_frame, orient='horizontal')
    game_scroll.pack(side=BOTTOM, fill=X)

    my_game = ttk.Treeview(
        table_frame, yscrollcommand=game_scroll.set, xscrollcommand=game_scroll.set)

    my_game.pack()

    game_scroll.config(command=my_game.yview)
    game_scroll.config(command=my_game.xview)

    # define our column

    my_game['columns'] = ('room_number')

    # format our column
    my_game.column("#0", width=10,  stretch=NO)
    my_game.column("room_number", anchor=CENTER, width=450)

    # Create Headings
    my_game.heading("#0", text="", anchor=CENTER)
    my_game.heading("room_number", text="Room Number", anchor=CENTER)

    # add data
    counter = 0
    for room in listOfWorkersRooms:
        my_game.insert(parent='', index='end',
                       iid=counter, text='', values=(room))
        counter = counter + 1
    label_rooms = Label(newWindow, text="Choose rooms:",
                        width=20, bg='#E9E9E5', fg='black', font=("bold", 12))
    label_rooms.pack(side=TOP, pady=20)
    text_rooms = Entry(newWindow, width=20, font=(
        "bold", 18), justify='center')
    text_rooms.pack(side=TOP, pady=20)

    def buttonHandler():
        if (changeWorkerRoom(todayDate, text_rooms.get(), dec[tkvar.get()])):
            popupmsg("Room's worker has been succsefully changed")
            newWindow.destroy()
        else:
            popupmsg("Falied to change worker")

    Button(newWindow, command=buttonHandler, text='Submit',  width=18,
           bg='#5C715E', fg='white', font=("", 11)).pack(side=TOP, pady=20)
    Button(newWindow, command=newWindow.destroy, text="<-Back", width=10,
           bg='#5C715E', fg='white', font=("bold", 12)).place(x=1, y=1)


def showCustomers():
    newWindow = Toplevel(root)
    newWindow.attributes('-fullscreen', True)
    newWindow.configure(background='#E9E9E5')
    topLabel = Label(newWindow, text='', width=90, bg='#D4D6C8',
                     fg='black', font=('Verdana Pro Black', 30))
    topLabel.pack(side=TOP)
    Label(newWindow, text="List of customers", width=35, bg='#E9E9E5',
          fg='black', font=("Elephant", 20)).pack(side=TOP, pady=50)
    table_frame = Frame(newWindow, bg='#5C715E', pady=10, padx=10)
    table_frame.pack(side=TOP, pady=20)

    bottomLabel = Label(newWindow, text='', width=90, bg='#D4D6C8',
                        fg='black', font=('Verdana Pro Black', 30))
    bottomLabel.pack(side=BOTTOM)
    customerList = []
    for c in database_connection.getAllCustomers():
        firstName = c[0].replace('(', '').replace(')', '').split(',')[0]
        lastName = c[0].replace('(', '').replace(')', '').split(',')[1]
        age = c[0].replace('(', '').replace(')', '').split(',')[2]
        gender = c[0].replace('(', '').replace(')', '').split(',')[3]
        id = c[0].replace('(', '').replace(')', '').split(',')[4]
        customerList.append((firstName, lastName, age, gender, id))

    # scrollbar
    game_scroll = Scrollbar(table_frame)
    game_scroll.pack(side=RIGHT, fill=Y)

    game_scroll = Scrollbar(table_frame, orient='horizontal')
    game_scroll.pack(side=BOTTOM, fill=X)

    my_game = ttk.Treeview(
        table_frame, yscrollcommand=game_scroll.set, xscrollcommand=game_scroll.set)

    my_game.pack()

    game_scroll.config(command=my_game.yview)
    game_scroll.config(command=my_game.xview)

    # define our column

    my_game['columns'] = ('firstName', 'lastName',
                          'age', 'gender', 'personalId')

    # format our column
    wid = 210
    my_game.column("#0", width=0,  stretch=NO)
    my_game.column("firstName", anchor=CENTER, width=wid)
    my_game.column("lastName", anchor=CENTER, width=wid)
    my_game.column("age", anchor=CENTER, width=wid)
    my_game.column("gender", anchor=CENTER, width=wid)
    my_game.column("personalId", anchor=CENTER, width=wid)

    # Create Headings
    my_game.heading("#0", text="", anchor=CENTER)
    my_game.heading("firstName", text="First Name", anchor=CENTER)
    my_game.heading("lastName", text="Last Name", anchor=CENTER)
    my_game.heading("age", text="Age", anchor=CENTER)
    my_game.heading("gender", text="Gender", anchor=CENTER)
    my_game.heading("personalId", text="Personal Id", anchor=CENTER)

    # add data
    counter = 0
    for customer in customerList:
        my_game.insert(parent='', index='end', iid=counter, text='',
                       values=(customer))
        counter = counter + 1
    my_game.pack()
    Button(newWindow, command=newWindow.destroy, text="<-Back", width=10,
           bg='#5C715E', fg='white', font=("bold", 12)).place(x=1, y=1)


def homepageADMIN(USER):
    adminHomePage = Toplevel(root)
    adminHomePage.title("Home Page")
    adminHomePage.attributes('-fullscreen', True)
    adminHomePage.configure(background='#E9E9E5')
    Label(adminHomePage, text="Admin Homepage:", width=20, bg='#E9E9E5',
          fg='black', font=("Elephant", 20)).place(x=50, y=120)
    topLabel = Label(adminHomePage, text='', width=90,
                     bg='#D4D6C8', fg='black', font=('Verdana Pro Black', 30))
    topLabel.pack(side=TOP)
    bottomLabel = Label(adminHomePage, text='', width=90,
                        bg='#D4D6C8', fg='black', font=('Verdana Pro Black', 30))
    bottomLabel.pack(side=BOTTOM)
    Button(adminHomePage, text="Quit", width=20, bg='#D4D6C8', fg='black', font=(
        'Verdana Pro Black', 13), command=root.destroy).place(x=650, y=400)
    signOut(adminHomePage)
    Button(adminHomePage, text="Add Worker", width=20, bg='#D4D6C8', fg='black', font=('Verdana Pro Black', 13),
           command=AddWorkerPage).place(x=350, y=200)
    Button(adminHomePage, text="Delete Worker", width=20, bg='#D4D6C8', fg='black', font=('Verdana Pro Black', 13),
           command=DeleteWorkerPage).place(x=350, y=240)
    Button(adminHomePage, text="Choose Worker Room", width=20, bg='#D4D6C8', fg='black', font=('Verdana Pro Black', 13),
           command=chooseWorkerRoom).place(x=350, y=280)
    Button(adminHomePage, text="Change Worker Room", width=20, bg='#D4D6C8', fg='black', font=('Verdana Pro Black', 13),
           command=ChangeWorkerRoom).place(x=650, y=360)
    Button(adminHomePage, text="Show Customers", width=20, bg='#D4D6C8', fg='black', font=(
        'Verdana Pro Black', 13), command=showCustomers).place(x=650, y=200)
    Button(adminHomePage, text="Approve Completed Tasks", width=20, bg='#D4D6C8', fg='black', font=(
        'Verdana Pro Black', 13), command=lambda: ApproveTask(USER)).place(x=650, y=240)
    Button(adminHomePage, text="Show Workers", width=20, bg='#D4D6C8', fg='black', font=(
        'Verdana Pro Black', 13), command=showWorkers).place(x=650, y=280)
    Button(adminHomePage, text="Details by Room Number", width=20, bg='#D4D6C8', fg='black', font=(
        'Verdana Pro Black', 13), command=showReservationDetailsByRoomNum).place(x=350, y=320)
    Button(adminHomePage, text="Show booked rooms", width=20, bg='#D4D6C8', fg='black', font=(
        'Verdana Pro Black', 13), command=showAllTodayReservation).place(x=350, y=360)
    Button(adminHomePage, text="Room history", width=20, bg='#D4D6C8', fg='black', font=(
        'Verdana Pro Black', 13), command=lambda: showAllroomHistory(USER)).place(x=650, y=320)
