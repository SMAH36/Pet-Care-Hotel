from tkinter import *
from functools import partial
from database import database_connection
import tkinter as tk
from functions import *
from SignIn import *
def PetAgeVaildetor(x):
       count=0
       for i in range (len(x)):
              if(x[i]>'9' or x[i]<'0'):
                     return False
       return True
def Reservation(USER):
       Pets=getPetsByUSERid(USER.userID)
       dec=[]
       for p in range(len(Pets)):
              dec[Pets[p][0]+'('+Pets[p][1]+')']=Pets[p][2]
       tkvar = StringVar(root)
       tkvar.set('Dog') # set the default option
       # on change dropdown value
       def change_dropdown(*args):
              print( tkvar.get() )

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
       tkvar.set('Dog') # set the default option
       # on change dropdown value
       def change_dropdown(*args):
              print( tkvar.get() )

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
              if( PetAgeVaildetor(entry_age.get())==False and flag == True):
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
                     if(database_connection.addPet(USER.userID, text_name.get(), tkvar.get(), entry_age.get(), gender,text_id.get())==True):
                            popupmsg('Your pet has been successfuly added :)')
                            tktk.destroy()
                     else:
                            popupmsg('Pet"s ID already exist')


       x = Button(tktk, command=buttonClick, text='Submit', width=20, bg='brown',
               fg='white').place(x=180, y=380)

    # it is use for display the registration form on the window
       tktk.mainloop()
       print("registration form  seccussfully created...")
def homepageCUSTOMER(USER):
    CustomerHomePage = Toplevel(root)
    CustomerHomePage.title("Home Page")
    CustomerHomePage.geometry("200x200")
    Button(CustomerHomePage, text="Reservation",command=lambda : AddPetPage(USER)).grid(column=0, row=1)
    Button(CustomerHomePage, text="AddPet",command=lambda : AddPetPage(USER)).grid(column=2, row=0)
    Button(CustomerHomePage, text="Quit",command=root.destroy).grid(column=0, row=0)
    signOut(CustomerHomePage)