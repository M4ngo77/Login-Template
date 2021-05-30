#Modules
from tkinter import Button, Frame, Tk, Entry, Label

#Accounts
accounts = [
    ("lololololo@gmail.com", "lolololo"),
    ("bobobobobo@gmail.com", "bobobobo"),
    ("cococococo@gmail.com", "cocococo"),
    ("aoaoaoaoao@gmail.com", "aoaoaoao"),
    ("krkrkrkrkr@gmail.com", "krkrkrkr"),
    ("tetetetete@gmail.com", "tetetete"),
    ("sksksksksk@gmail.com", "sksksksk")
]

#Window
window = Tk()
window.geometry('640x560')
window.title('Login')
window.iconbitmap('icon.ico')
window.configure(bg='purple')
window.resizable(False, False)

#Login Window
login_window = Frame(window, width=300, height=450, bg='white')
login_window.place(x=165, y=45)

#Login Text
login_text = Label(window, text='Login', font=('Montserrat',20,'bold'))
login_text.configure(fg='black', bg='white')
login_text.place(x=270, y=70)

#Email Text
email_text = Label(window, text='Enter Email', font=('Montserrat',15,'bold'))
email_text.configure(fg='black', bg='white')
email_text.place(x=220, y=145)

#Password Text
password_text = Label(window, text='Enter Password', font=('Montserrat',15,'bold'))
password_text.configure(fg='black', bg='white')
password_text.place(x=220, y=275)

#Email Enter
email_enter = Entry(window)
email_enter.configure(bg='white', fg='black', font=('Montserrat',18,'bold'))
email_enter.place(x=220, y=170, height=50, width=200)

#Password Enter
password_enter = Entry(window)
password_enter.configure(bg='white', fg='black', font=('Montserrat',18,'bold'))
password_enter.place(x=220, y=300, height=50, width=200)

#Login Function
def login():
    email = email_enter.get()
    password = password_enter.get()
    if email == accounts[0][0] and password == accounts[0][1] or email == accounts[1][0] and password == accounts[1][1] or email == accounts[2][0] and password == accounts[2][1] or email == accounts[3][0] and password == accounts[3][1] or email == accounts[4][0] and password == accounts[4][1] or email == accounts[5][0] and password == accounts[5][1] or email == accounts[6][0] and password == accounts[6][1]:
        success = Label(text='Success. You Loged in', fg='green', bg='white')
        success.place(x=245, y=355)
    else:
        feiled = Label(text='Incorrect Email Or Password', fg='red', bg='white')
        feiled.place(x=245, y=355)

#Login Button
login_button = Button(window, text='Login', fg='white', bg='red', command=login)
login_button.place(x=220, y=380, height=50, width=200)

window.mainloop()
