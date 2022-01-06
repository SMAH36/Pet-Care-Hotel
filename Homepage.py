
# from tkinter import *
# from tkinter import messagebox
# from tkinter import ttk
# class pets:
#     def __init__(self,root):
#         self.root = root
#         self.root.state('zoomed')
#         self.root.title('pets hotel')
#         self.root.configure(background='#E9E9E5')
#         #self.root.resizable(False,True)
#         title = Label(self.root,text='...Welcome to our PETS CARE&LOVE animals hotel...',width=50, bg='#E8EAE6',fg='black',font=('Verdana Pro Black',20)).place(x=0, y=180)
#         title = Label(self.root,text='',width=90, bg='#D4D6C8',fg='black',font=('Verdana Pro Black',20)).place(x=0, y=120)
#         title = Label(self.root,text='',width=90, bg='#D4D6C8',fg='black',font=('Verdana Pro Black',20)).place(x=0, y=420)
#         title = Label(self.root,text='PETS CARE&LOVE',width=20, bg='#CFDAC8',fg='black',font=('Verdana Pro Black',20)).place(x=930, y=120)
#         title = Label(self.root,text='your pet deserves the best care\neven when you are not around.\nWill that be possible?...',width=30, bg='#CFDAC8',fg='black',font=('Verdana Pro Black',13)).place(x=960, y=160)
#         title = Label(self.root,text='booking for a hotel',width=20, bg='#D4D6C8',fg='black',font=('Verdana Pro Black',13)).place(x=10, y=420)
#         title = Label(self.root,text='our services',width=15, bg='#D4D6C8',fg='black',font=('Verdana Pro Black',13)).place(x=230, y=420)
#         title = Label(self.root,text='customer responses',width=19, bg='#D4D6C8',fg='black',font=('Verdana Pro Black',13)).place(x=440, y=420)
#         title = Label(self.root,text='gallery',width=19, bg='#D4D6C8',fg='black',font=('Verdana Pro Black',13)).place(x=640, y=420)
#         title = Label(self.root,text='jops',width=19, bg='#D4D6C8',fg='black',font=('Verdana Pro Black',13)).place(x=840, y=420)
#         title = Label(self.root,text='',width=20, bg='#D4D6C8',fg='black',font=('Verdana Pro Black',13)).place(x=10, y=480)
#         title = Label(self.root,text='our services',width=15, bg='#D4D6C8',fg='black',font=('Verdana Pro Black',13)).place(x=230, y=420)
#         #Label.pack(self.root,padx=10,ipadx=50,ipady=70)

# root = Tk()
# Button(root, text='LOGIN', width=7, bg='#9A9B94',fg='black',font=('',13)).place(x=110, y=30)
# Button(root, text='SIGNUP', width=8, bg='#9A9B94',fg='black',font=('',13)).place(x=190, y=30)
# Button(root, text= 'ADD MY PET', width=11, bg='#9A9B94',fg='black',font=('',13)).place(x=280, y=30)
# Button(root, text='BOOK APPOINTMENT', width=18, bg='#9A9B94',fg='black',font=('',13)).place(x=400, y=30)
# Button(root, text='ABOUT US', width=9, bg='#9A9B94',fg='black',font=('',13)).place(x=580, y=30)
# Button(root, text='TESTIMONIALS', width=13, bg='#9A9B94',fg='black',font=('',13)).place(x=680, y=30)
# Button(root, text='CONTACT US', width=11, bg='#9A9B94',fg='black',font=('',13)).place(x=820, y=30)
# Button(root, text='EXIT', width=15, bg='#5C715E',fg='black',font=('',13)).place(x=1100, y=610)
# Button(root, text='FIND US', width=8, bg='#9A9B94',fg='black',font=('',13)).place(x=940, y=30)
# #Button(root, text='LOGOUT', width=8, bg='#9A9B94',fg='black',font=('',13)).place(x=1040, y=30)
# Button(root, text='Read more...', width=11, bg='#CFDAC8',fg='black',font=('',13)).place(x=1125, y=225)
# Button(root, text='', width=2, bg='#DDBEBE',fg='black',font=('',13)).place(x=1160, y=30)

# op = pets(root)
# photo=PhotoImage(file="")
# root.mainloop()

from tkinter import *
from tkinter import ttk


ws = Tk()
ws.title('PythonGuides')
ws.geometry('300x200')
ws['bg'] = 'black'

game_frame = Frame(ws)
game_frame.pack()

# scrollbar
# scrollbar
game_scroll = Scrollbar(game_frame)
game_scroll.pack(side=RIGHT, fill=Y)

game_scroll = Scrollbar(game_frame, orient='horizontal')
game_scroll.pack(side=BOTTOM, fill=X)

my_game = ttk.Treeview(
    game_frame, yscrollcommand=game_scroll.set, xscrollcommand=game_scroll.set)


my_game.pack()

game_scroll.config(command=my_game.yview)
game_scroll.config(command=my_game.xview)

my_game = ttk.Treeview(
    game_frame, yscrollcommand=game_scroll.set)


my_game.pack()

game_scroll.config(command=my_game.yview)
game_scroll.config(command=my_game.xview)

# define our column

my_game['columns'] = ('player_id', 'player_name',
                      'player_Rank', 'player_states', 'player_city')

# format our column
my_game.column("#0", width=0,  stretch=NO)
my_game.column("player_id", anchor=CENTER, width=80)
my_game.column("player_name", anchor=CENTER, width=80)
my_game.column("player_Rank", anchor=CENTER, width=80)
my_game.column("player_states", anchor=CENTER, width=80)
my_game.column("player_city", anchor=CENTER, width=80)

# Create Headings
my_game.heading("#0", text="", anchor=CENTER)
my_game.heading("player_id", text="Id", anchor=CENTER)
my_game.heading("player_name", text="Name", anchor=CENTER)
my_game.heading("player_Rank", text="Rank", anchor=CENTER)
my_game.heading("player_states", text="States", anchor=CENTER)
my_game.heading("player_city", text="States", anchor=CENTER)

# add data
my_game.insert(parent='', index='end', iid=0, text='',
               values=('1', 'Ninja', '101', 'Oklahoma', 'Moore'))
my_game.insert(parent='', index='end', iid=1, text='',
               values=('2', 'Ranger', '102', 'Wisconsin', 'Green Bay'))
my_game.insert(parent='', index='end', iid=2, text='',
               values=('3', 'Deamon', '103', 'California', 'Placentia'))
my_game.insert(parent='', index='end', iid=3, text='',
               values=('4', 'Dragon', '104', 'New York', 'White Plains'))
my_game.insert(parent='', index='end', iid=4, text='',
               values=('5', 'CrissCross', '105', 'California', 'San Diego'))
my_game.insert(parent='', index='end', iid=5, text='',
               values=('6', 'ZaqueriBlack', '106', 'Wisconsin', 'TONY'))
my_game.insert(parent='', index='end', iid=6, text='',
               values=('7', 'RayRizzo', '107', 'Colorado', 'Denver'))
my_game.insert(parent='', index='end', iid=7, text='',
               values=('8', 'Byun', '108', 'Pennsylvania', 'ORVISTON'))
my_game.insert(parent='', index='end', iid=8, text='',
               values=('9', 'Trink', '109', 'Ohio', 'Cleveland'))
my_game.insert(parent='', index='end', iid=9, text='',
               values=('10', 'Twitch', '110', 'Georgia', 'Duluth'))
my_game.insert(parent='', index='end', iid=10, text='',
               values=('11', 'Animus', '111', 'Connecticut', 'Hartford'))
my_game.pack()


ws.mainloop()
