from tkinter import*
root = Tk()
root.geometry('500x500')
root.title("Registration Form")

label_0 = Label(root, text="Registration form", width=20, font=("bold", 20))
label_0.place(x=90, y=53)

label_name = Label(root, text="Name", width=20, font=("bold", 10))
label_name.place(x=80, y=130)

text_name = Entry(root)
text_name.place(x=240, y=130)

label_lastName = Label(root, text="Last Name", width=20, font=("bold", 10))
label_lastName.place(x=80, y=160)

text_lastName = Entry(root)
text_lastName.place(x=240, y=160)

label_email = Label(root, text="Email", width=20, font=("bold", 10))
label_email.place(x=68, y=210)

text_email = Entry(root)
text_email.place(x=240, y=210)

label_3 = Label(root, text="Gender", width=20, font=("bold", 10))
label_3.place(x=70, y=230)
var = IntVar()
Radiobutton(root, text="Male", padx=5, variable=var,
            value=1).place(x=235, y=230)
Radiobutton(root, text="Female", padx=20,
            variable=var, value=2).place(x=290, y=230)

label_4 = Label(root, text="Age:", width=20, font=("bold", 10))
label_4.place(x=70, y=280)


entry_2 = Entry(root)
entry_2.place(x=240, y=280)

Button(root, text='Submit', width=20, bg='brown',
       fg='white').place(x=180, y=380)
# it is use for display the registration form on the window
root.mainloop()
print("registration form  seccussfully created...")
