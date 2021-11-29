from tkinter import *

root = Tk()

class User:
    def __init__(self,personalID,rank,name):
        self.name = name
        self.personalID = personalID
        self.rank = rank

    def checkRank(self):
        return self.rank





def openNewWindow(a):
    print(f"{a}")
    newWindow = Toplevel(root)
    newWindow.title("New Window")
    newWindow.geometry("200x200")
    Label(newWindow,
          text="This is a new window").pack()

# def digitsOnly(input):
      
#     if input.isdigit():
#         print(input)
#         return True
                          
#     elif input is "":
#         print(input)
#         return True
  
#     else:
#         print(input)
#         return False
        