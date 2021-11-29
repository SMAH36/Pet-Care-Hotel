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

label_id = Label(root, text="Id", width=20, font=("bold", 10))
label_id.place(x=68, y=190)

text_id = Entry(root)
text_id.place(x=240, y=190)

label_email = Label(root, text="Email", width=20, font=("bold", 10))
label_email.place(x=68, y=210)

text_email = Entry(root)
text_email.place(x=240, y=210)

label_password = Label(root, text="Password", width=20, font=("bold", 10))
label_password.place(x=68, y=230)

text_password = Entry(root)
text_password.place(x=240, y=230)

label_gender = Label(root, text="Gender", width=20, font=("bold", 10))
label_gender.place(x=70, y=250)
var = IntVar()
Radiobutton(root, text="Male", padx=5, variable=var,
            value=1).place(x=235, y=250)
Radiobutton(root, text="Female", padx=20,
            variable=var, value=2).place(x=290, y=250)

label_age = Label(root, text="Age:", width=20, font=("bold", 10))
label_age.place(x=70, y=300)


entry_age = Entry(root)
entry_age.place(x=240, y=300)

Button(root, text='Submit', width=20, bg='brown',
       fg='white').place(x=180, y=380)
# it is use for display the registration form on the window
root.mainloop()
print("registration form  seccussfully created...")


def idVaildetor(id):
    b = id
    id = str(id)
    if(len(id) != 9 and b.isnumeric()):
        return False
    sum, x, counter = 0, 0, 0
    for i in id:
        x = int(i) * ((counter % 2)+1)
        counter += 1
        if x > 9:
            sum += x-9
        else:
            sum += x
    return sum % 10 == 0
