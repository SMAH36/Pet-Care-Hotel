from tkinter import *
from functools import partial
from database import database_connection
from database.database_connection import *
import tkinter as tk
from functions import *
from datetime import date
from tkinter import ttk


def CompleteTask(USER):  # >>>>>>>>>>>>>>>>>>>>>Task 5
    newWindow = Toplevel(root)
    newWindow.attributes('-fullscreen', True)
    newWindow.configure(background='#E9E9E5')
    topLabel = Label(newWindow, text='', width=90, bg='#D4D6C8',
                     fg='black', font=('Verdana Pro Black', 30))
    topLabel.pack(side=TOP)
    Label(newWindow, text="Complete Task", width=30, bg='#E9E9E5',
          fg='black', font=("Elephant", 20)).pack(side=TOP, pady=20)
    table_frame = Frame(newWindow, bg='#5C715E', pady=20, padx=20)
    table_frame.pack(side=TOP, pady=40)
    bottomLabel = Label(newWindow, text='', width=90, bg='#D4D6C8',
                        fg='black', font=('Verdana Pro Black', 30))
    bottomLabel.pack(side=BOTTOM)
    today = date.today()
    todayDate = f'{today.month}/{today.day}/{today.year}'
    rooms = list(map(lambda x: x[0], list(
        getUncompletedTasks(todayDate, USER.userID))))
    print('rooms', rooms)
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
    label_rooms = Label(newWindow, text="Choose rooms:", width=20,
                        bg='#E9E9E5', fg='black', font=("Elephant", 18))
    label_rooms.pack(side=TOP, pady=20)
    text_rooms = Entry(newWindow, justify='center', font=('', 18))
    text_rooms.pack(side=TOP, pady=20)

    def buttonHandler():

        Choosedrooms = list(text_rooms.get().split(','))
        if (completeTask(todayDate, list(filter(lambda x: x in rooms, Choosedrooms)), USER.userID)):
            popupmsg("Your request has been succsefully sent")
            newWindow.destroy()
        else:
            popupmsg("Falied to send your request")

    Button(newWindow, command=buttonHandler, text='Submit',
           width=20, bg='#5C715E', fg='white', font=('', 18)).pack(side=TOP, pady=100)
    Button(newWindow,  command=newWindow.destroy, text="<-Back", width=10,
           bg='#5C715E', fg='white', font=("bold", 12)).place(x=1, y=1)


def ShowMeMyRooms(USER):  # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Task 4
    today = date.today()
    todayDate = f'{today.month}/{today.day}/{today.year}'
    rooms = list(map(lambda x: x[0], list(
        getWorkerRoomsByDate(todayDate, USER.userID))))
    text = 'Your rooms for today : '
    for r in rooms:
        text += r+','
    popupmsg(text)


def ShowMePetByRoom(USER):  # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> task 3
    # (ddd,Dog,ba8beb62-5eb4-4f93-a2a0-657ba7d2a419,1,male,123)
    PetByRoom = Toplevel(root)
    PetByRoom.title("Pet By Room")
    PetByRoom.attributes('-fullscreen', True)
    PetByRoom.configure(background='#E9E9E5')
    topLabel = Label(PetByRoom, text='', width=90, bg='#D4D6C8',
                     fg='black', font=('Verdana Pro Black', 30))
    topLabel.pack(side=TOP)
    Label(PetByRoom, text="Pet's details by room number", width=30,
          bg='#E9E9E5', fg='black', font=("Elephant", 20)).pack(side=TOP, pady=20)
    bottomLabel = Label(PetByRoom, text='', width=90, bg='#D4D6C8',
                        fg='black', font=('Verdana Pro Black', 30))
    bottomLabel.pack(side=BOTTOM)
    today = date.today()
    todayDate = f'{today.month}/{today.day}/{today.year}'
    label_room = Label(PetByRoom, text="Enter room number Please:",
                       width=23, bg='#E9E9E5', fg='black', font=("bold", 18))
    label_room.pack(side=TOP, pady=20)
    text_room = Entry(PetByRoom, width=20, font=("", 18), justify='center')
    text_room.pack(side=TOP, pady=20)

    def PetsDetailsPopUp():
        res = getPetInfoByRoomNumber(todayDate, text_room.get())
        if res != False:
            Pet = list((res).replace('(', '').replace(')', '').split(','))
            print('Pet', Pet)
            text = 'Pet details: \n'
            text += 'Name: '+Pet[0]+'\n'
            text += 'Type: '+Pet[1]+'\n'
            text += 'Age: '+Pet[3]+'\n'
            text += 'Gender: '+Pet[4]+'\n'
            text += 'ID: '+Pet[5]+'\n'
            popupmsg(text)
        else:
            popupmsg('No pet in this room')
    Button(PetByRoom, command=PetsDetailsPopUp, text='Submit',
           width=20, bg='#5C715E', fg='white', font=('', 18)).pack(side=TOP, pady=20)
    Button(PetByRoom, command=PetByRoom.destroy, text="<-Back", width=10,
           bg='#5C715E', fg='white', font=("bold", 12)).place(x=1, y=1)


def homepageWORKER(USER):  # task 6************************************************
    workerHomePage = Toplevel(root)
    workerHomePage.title("Home Page")
    workerHomePage.state("zoomed")
    workerHomePage.configure(background='#E9E9E5')
    topLabel = Label(workerHomePage, text='', width=90,
                     bg='#D4D6C8', fg='black', font=('Verdana Pro Black', 30))
    topLabel.pack(side=TOP)
    bottomLabel = Label(workerHomePage, text='', width=90,
                        bg='#D4D6C8', fg='black', font=('Verdana Pro Black', 30))
    bottomLabel.pack(side=BOTTOM)
    Label(workerHomePage, text="worker Homepage:", width=30, bg='#E9E9E5',
          fg='black', font=("Elephant", 20)).place(x=30, y=120)
    Button(workerHomePage, text="Complete task", width=30, bg='#D4D6C8', fg='black', font=(
        'Elephant', 13), command=lambda: CompleteTask(USER)).place(x=450, y=240)
    Button(workerHomePage, text="Quit", width=30, bg='#D4D6C8', fg='black',
           font=('Elephant', 13), command=root.destroy).place(x=450, y=420)
    Button(workerHomePage, text="My rooms", width=30, bg='#D4D6C8', fg='black', font=(
        'Elephant', 13), command=lambda: ShowMeMyRooms(USER)).place(x=450, y=360)
    Button(workerHomePage, text="Pet's details by room number", width=30, bg='#D4D6C8', fg='black',
           font=('Elephant', 13), command=lambda: ShowMePetByRoom(USER)).place(x=450, y=300)
    Button(workerHomePage, text="Sign out", command=workerHomePage.destroy).grid(
        column=1, row=0)  # >>>>>>>>>>>>>>>>>>>>>>> task 2
    signOut(workerHomePage)  # >>>>>>>>>>3
