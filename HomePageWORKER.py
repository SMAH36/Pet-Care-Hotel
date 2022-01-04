from tkinter import *
from functools import partial
from database import database_connection
from database.database_connection import *
import tkinter as tk
from functions import *
from datetime import date

def ShowMeMyRooms(USER):
       today = date.today()
       todayDate = f'{today.month}/{today.day}/{today.year}'
       rooms = list(map(lambda x:x[0],list(getWorkerRoomsByDate(todayDate, USER.userID))))
       text='Your rooms for today : '
       for r in rooms:
              text+=r+','
       popupmsg(text)
def ShowMePetByRoom(USER):
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
       

def homepageWORKER(USER):
       workerHomePage = Toplevel(root)
       workerHomePage.title("Home Page")
       workerHomePage.geometry("200x200")
       Button(workerHomePage, text="Quit",command=root.destroy).grid(column=0, row=0)
       Button(workerHomePage, text="My rooms",command=lambda :ShowMeMyRooms(USER)).grid(column=2, row=0)
       Button(workerHomePage, text="Pet's details by room number",command=lambda :ShowMePetByRoom(USER)).grid(column=-0, row=1)
       signOut(workerHomePage)
