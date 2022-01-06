from tkinter import *
from functools import partial
from database import database_connection
from database.database_connection import *
import tkinter as tk
from functions import *
from datetime import date
from tkinter import ttk

def CompleteTask(USER):# >>>>>>>>>>>>>>>>>>>>>Task 5
       newWindow = Toplevel(root)
       newWindow.state('zoomed')
       today = date.today()
       todayDate = f'{today.month}/{today.day}/{today.year}'
       rooms = list(map(lambda x:x[0],list(getUncompletedTasks(todayDate, USER.userID))))
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
       Choosedrooms=list(text_rooms.get().split(',')) 
       def buttonHandler():
              if (completeTask(todayDate,list(filter(lambda x:x in rooms,Choosedrooms)),USER.userID)):      
                     popupmsg("Your request has been succsefully sent")
                     newWindow.destroy()
              else:
                     popupmsg("Falied to send your request ! ! !")  
              

       Button(newWindow, command=buttonHandler, text='Submit', width=20, bg='brown',fg='white').place(x=100, y=200)
       Button(newWindow, text="Quit", command=newWindow.destroy).grid(column=0, row=0)
   
def ShowMeMyRooms(USER):#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> Task 4
       today = date.today()
       todayDate = f'{today.month}/{today.day}/{today.year}'
       rooms = list(map(lambda x:x[0],list(getWorkerRoomsByDate(todayDate, USER.userID))))
       text='Your rooms for today : '
       for r in rooms:
              text+=r+','
       popupmsg(text)
def ShowMePetByRoom(USER):#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> task 3
       #(ddd,Dog,ba8beb62-5eb4-4f93-a2a0-657ba7d2a419,1,male,123)
       PetByRoom = Toplevel(root)
       PetByRoom.title("Pet By Room")
       PetByRoom.geometry("300x300")
       today = date.today()
       todayDate = f'{today.month}/{today.day}/{today.year}'
       label_room = Label(PetByRoom, text="Enter room number Please:",width=20, font=("bold", 10))
       label_room.place(x=0, y=100)
       text_room = Entry(PetByRoom)
       text_room.place(x=200, y=100)
       
       def PetsDetailsPopUp():
              Pet=list(getPetInfoByRoomNumber(todayDate,text_room.get()).replace('(','').replace(')','').split(','))
              print(Pet)
              text='Pet details: \n'
              text+='Name: '+Pet[0]+'\n'
              text+='Type: '+Pet[1]+'\n'
              text+='Age: '+Pet[3]+'\n'
              text+='Gender: '+Pet[4]+'\n'
              text+='ID: '+Pet[5]+'\n'
              popupmsg(text)
       Button(PetByRoom, command=PetsDetailsPopUp, text='Submit', width=20, bg='brown',fg='white').place(x=100, y=200)
       

def homepageWORKER(USER):#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> task 6
       workerHomePage = Toplevel(root)
       workerHomePage.title("Home Page")
       workerHomePage.geometry("200x200")
       Button(workerHomePage, text="Complete task",command=lambda :CompleteTask(USER)).grid(column=0, row=2)
       Button(workerHomePage, text="Quit",command=root.destroy).grid(column=0, row=0)
       Button(workerHomePage, text="Sign out",command=workerHomePage.destroy).grid(column=1, row=0)#>>>>>>>>>>>>>>>>>>>>>>> task 2
       Button(workerHomePage, text="My rooms",command=lambda :ShowMeMyRooms(USER)).grid(column=2, row=0)
       Button(workerHomePage, text="Pet's details by room number",command=lambda :ShowMePetByRoom(USER)).grid(column=0, row=1)
       signOut(workerHomePage)#>>>>>>>>>>3
