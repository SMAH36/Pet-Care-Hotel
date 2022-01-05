from tkinter import *
from functools import partial
from database import database_connection
from database.database_connection import *
import tkinter as tk
from functions import *
from tkinter import ttk
from datetime import date
# ADD WORKER <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
def showReservationDetailsByRoomNum():
    newWindow = Toplevel(root)
    newWindow.state('zoomed')
    today = date.today()
    todayDate = f'{today.month}/{today.day}/{today.year}'
    label_room = Label(newWindow, text="Enter room number:",width=20, font=("bold", 10))
    label_room.place(x=0, y=100)
    text_room = Entry(newWindow)
    text_room.place(x=200, y=100)
    def ReservationDetails():
        

    Button(newWindow, command=ReservationDetails, text='Submit', width=20, bg='brown',fg='white').place(x=100, y=200)
    


def showWorkers():
    newWindow = Toplevel(root)
    newWindow.state('zoomed')
    customerList = []
    for c in database_connection.getAllWorkers1():
        firstName = c[0].replace('(', '').replace(')', '').split(',')[0]
        lastName = c[0].replace('(', '').replace(')', '').split(',')[1]
        age = c[0].replace('(', '').replace(')', '').split(',')[2]
        gender = c[0].replace('(', '').replace(')', '').split(',')[3]
        id = c[0].replace('(', '').replace(')', '').split(',')[4]
        customerList.append((firstName, lastName, age, gender, id))

    # scrollbar
    game_scroll = Scrollbar(newWindow)
    game_scroll.pack(side=RIGHT, fill=Y)

    game_scroll = Scrollbar(newWindow, orient='horizontal')
    game_scroll.pack(side=BOTTOM, fill=X)

    my_game = ttk.Treeview(
        newWindow, yscrollcommand=game_scroll.set, xscrollcommand=game_scroll.set)

    my_game.pack()

    game_scroll.config(command=my_game.yview)
    game_scroll.config(command=my_game.xview)

    # define our column

    my_game['columns'] = ('firstName', 'lastName',
                          'age', 'gender', 'personalId')

    # format our column
    my_game.column("#0", width=0,  stretch=NO)
    my_game.column("firstName", anchor=CENTER, width=80)
    my_game.column("lastName", anchor=CENTER, width=80)
    my_game.column("age", anchor=CENTER, width=80)
    my_game.column("gender", anchor=CENTER, width=80)
    my_game.column("personalId", anchor=CENTER, width=80)

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

def ApproveTask(USER):
       newWindow = Toplevel(root)
       newWindow.state('zoomed')
       today = date.today()
       todayDate = f'{today.month}/{today.day}/{today.year}'
       rooms = list(map(lambda x:x[0],list(getUnapprovedCompletedTasks(todayDate))))
       print(rooms)
       # scrollbar
       game_scroll = Scrollbar(newWindow)
       game_scroll.pack(side=RIGHT, fill=Y)

       game_scroll = Scrollbar(newWindow, orient='horizontal')
       game_scroll.pack(side=BOTTOM, fill=X)

       my_game = ttk.Treeview(newWindow, yscrollcommand=game_scroll.set, xscrollcommand=game_scroll.set)

       my_game.pack()

       game_scroll.config(command=my_game.yview)
       game_scroll.config(command=my_game.xview)

       # define our column

       my_game['columns'] = ('room_number')

       # format our column
       my_game.column("#0", width=0,  stretch=NO)
       my_game.column("room_number", anchor=CENTER, width=80)

       # Create Headings
       my_game.heading("#0", text="", anchor=CENTER)
       my_game.heading("room_number", text="Room Number", anchor=CENTER)

       # add data
       counter = 0
       for room in rooms:
              my_game.insert(parent='', index='end', iid=counter, text='',values=(room))
              counter = counter + 1
       label_rooms = Label(newWindow, text="Choose rooms:",width=20, font=("bold", 10))
       label_rooms.place(x=0, y=100)
       text_rooms = Entry(newWindow)
       text_rooms.place(x=200, y=100)
       def buttonHandler():
              if (approveTask(todayDate,text_rooms.get(),USER.userID)):      
                     popupmsg("Your request has been succsefully sent")
                     newWindow.destroy()
              else:
                     popupmsg("Falied to send your request ! ! !")  
              

       Button(newWindow, command=buttonHandler, text='Submit', width=20, bg='brown',fg='white').place(x=100, y=200)
       Button(newWindow, text="Quit", command=newWindow.destroy).grid(column=0, row=0)
   
def AddWorkerPage():
    AddWorker = Toplevel(root)
    AddWorker.title("Add Worker")
    AddWorker.geometry("500x500")
    Button(AddWorker, text="Back", command=AddWorker.destroy).grid(
        column=0, row=0)
    label_email = Label(AddWorker, text="Email or Phone",
                        width=20, font=("bold", 10))
    label_email.place(x=0, y=100)
    text_email = Entry(AddWorker)
    text_email.place(x=200, y=100)

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

    Button(AddWorker, command=buttonClick, text='Submit', width=20, bg='brown',fg='white').place(x=90, y=120)


def DeleteWorkerPage():
    DeleteWorker = Toplevel(root)
    DeleteWorker.title("Delete Worker")
    DeleteWorker.geometry("500x500")
    Button(DeleteWorker, text="Quit",
           command=DeleteWorker.destroy).grid(column=0, row=0)
    label_email = Label(DeleteWorker, text="Email or Phone",
                        width=20, font=("bold", 10))
    label_email.place(x=0, y=100)
    text_email = Entry(DeleteWorker)
    text_email.place(x=200, y=100)

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

    Button(DeleteWorker, command=buttonClick, text='Submit', width=20, bg='brown',
           fg='white').place(x=90, y=120)


def chooseWorkerRoom():
    newWindow = Toplevel(root)
    newWindow.state('zoomed')
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

    relaventList = list(filter(lambda x: x not in listOfWorkersRooms, listOfResRooms))

    tkvar = StringVar(root)
    tkvar.set('Choose Worker')

    def change_dropdown(*args):
        print(tkvar.get())
    tkvar.trace('w', change_dropdown)

    text_Type = OptionMenu(newWindow, tkvar, *listOfWorker)
    text_Type.place(x=240, y=160)

    # scrollbar
    game_scroll = Scrollbar(newWindow)
    game_scroll.pack(side=RIGHT, fill=Y)

    game_scroll = Scrollbar(newWindow, orient='horizontal')
    game_scroll.pack(side=BOTTOM, fill=X)

    my_game = ttk.Treeview(
        newWindow, yscrollcommand=game_scroll.set, xscrollcommand=game_scroll.set)

    my_game.pack()

    game_scroll.config(command=my_game.yview)
    game_scroll.config(command=my_game.xview)

    # define our column

    my_game['columns'] = ('room_number')

    # format our column
    my_game.column("#0", width=0,  stretch=NO)
    my_game.column("room_number", anchor=CENTER, width=80)

    # Create Headings
    my_game.heading("#0", text="", anchor=CENTER)
    my_game.heading("room_number", text="Room Number", anchor=CENTER)

    # add data
    counter = 0
    for room in relaventList:
        my_game.insert(parent='', index='end', iid=counter, text='',values=(room))
        counter = counter + 1
    label_rooms = Label(newWindow, text="Choose rooms:",width=20, font=("bold", 10))
    label_rooms.place(x=0, y=100)
    text_rooms = Entry(newWindow)
    text_rooms.place(x=200, y=100)
    def buttonHandler():
        rooms=list(text_rooms.get().split(',')) 
        # print(relaventList,rooms)
        # print(list(filter(lambda x:x in relaventList,rooms)))
        if (setWorkerToRoom(todayDate, list(filter(lambda x:x in relaventList,rooms)), dec[tkvar.get()])):
            popupmsg("Rooms has been succsefully seted")
            newWindow.destroy()
        else:
            popupmsg("Falied to set rooms ! ! !")
    

    Button(newWindow, command=buttonHandler, text='Submit', width=20, bg='brown',fg='white').place(x=100, y=200)
    Button(newWindow, text="Quit", command=newWindow.destroy).grid(column=0, row=0)
   
def ChangeWorkerRoom():
    newWindow = Toplevel(root)
    newWindow.state('zoomed')
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
        print(tkvar.get())
    tkvar.trace('w', change_dropdown)

    text_Type = OptionMenu(newWindow, tkvar, *listOfWorker)
    text_Type.place(x=240, y=160)

    # scrollbar
    game_scroll = Scrollbar(newWindow)
    game_scroll.pack(side=RIGHT, fill=Y)

    game_scroll = Scrollbar(newWindow, orient='horizontal')
    game_scroll.pack(side=BOTTOM, fill=X)

    my_game = ttk.Treeview(newWindow, yscrollcommand=game_scroll.set, xscrollcommand=game_scroll.set)

    my_game.pack()

    game_scroll.config(command=my_game.yview)
    game_scroll.config(command=my_game.xview)

    # define our column

    my_game['columns'] = ('room_number')

    # format our column
    my_game.column("#0", width=0,  stretch=NO)
    my_game.column("room_number", anchor=CENTER, width=80)

    # Create Headings
    my_game.heading("#0", text="", anchor=CENTER)
    my_game.heading("room_number", text="Room Number", anchor=CENTER)

    # add data
    counter = 0
    print(listOfWorkersRooms)
    for room in listOfWorkersRooms:
        my_game.insert(parent='', index='end', iid=counter, text='',values=(room))
        counter = counter + 1
    label_rooms = Label(newWindow, text="Choose rooms:",width=20, font=("bold", 10))
    label_rooms.place(x=0, y=100)
    text_rooms = Entry(newWindow)
    text_rooms.place(x=200, y=100)
    def buttonHandler():
        if (changeWorkerRoom(todayDate,text_rooms.get(), dec[tkvar.get()])):      
            popupmsg("Room's worker has been succsefully changed")
            newWindow.destroy()
        else:
            popupmsg("Falied to change worker ! ! !")  
    

    Button(newWindow, command=buttonHandler, text='Submit', width=20, bg='brown',fg='white').place(x=100, y=200)
    Button(newWindow, text="Quit", command=newWindow.destroy).grid(column=0, row=0)
   

def showCustomers():
    newWindow = Toplevel(root)
    newWindow.state('zoomed')
    customerList = []
    for c in database_connection.getAllCustomers():
        firstName = c[0].replace('(', '').replace(')', '').split(',')[0]
        lastName = c[0].replace('(', '').replace(')', '').split(',')[1]
        age = c[0].replace('(', '').replace(')', '').split(',')[2]
        gender = c[0].replace('(', '').replace(')', '').split(',')[3]
        id = c[0].replace('(', '').replace(')', '').split(',')[4]
        customerList.append((firstName, lastName, age, gender, id))

    # scrollbar
    game_scroll = Scrollbar(newWindow)
    game_scroll.pack(side=RIGHT, fill=Y)

    game_scroll = Scrollbar(newWindow, orient='horizontal')
    game_scroll.pack(side=BOTTOM, fill=X)

    my_game = ttk.Treeview(
        newWindow, yscrollcommand=game_scroll.set, xscrollcommand=game_scroll.set)

    my_game.pack()

    game_scroll.config(command=my_game.yview)
    game_scroll.config(command=my_game.xview)

    # define our column

    my_game['columns'] = ('firstName', 'lastName',
                          'age', 'gender', 'personalId')

    # format our column
    my_game.column("#0", width=0,  stretch=NO)
    my_game.column("firstName", anchor=CENTER, width=80)
    my_game.column("lastName", anchor=CENTER, width=80)
    my_game.column("age", anchor=CENTER, width=80)
    my_game.column("gender", anchor=CENTER, width=80)
    my_game.column("personalId", anchor=CENTER, width=80)

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


def homepageADMIN(USER):
    adminHomePage = Toplevel(root)
    adminHomePage.title("Home Page")
    adminHomePage.state('zoomed')
    
    Button(adminHomePage, text="Quit",command=root.destroy).grid(column=0, row=0)
    signOut(adminHomePage)
    Button(adminHomePage, text="Add Worker",
           command=AddWorkerPage).grid(column=0, row=1)
    Button(adminHomePage, text="Delete Worker",
           command=DeleteWorkerPage).grid(column=1, row=1)
    Button(adminHomePage, text="choose worker room",
           command=chooseWorkerRoom).grid(column=2, row=1)
    Button(adminHomePage, text="Show customers",command=showCustomers).grid(column=1, row=2)
    Button(adminHomePage, text="Approve completed tasks",command=lambda :ApproveTask(USER)).grid(column=0, row=2)
    Button(adminHomePage, text="Show Workers",command=showWorkers).grid(column=0, row=3)

