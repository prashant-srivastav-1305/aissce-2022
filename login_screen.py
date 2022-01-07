"""
This is the login screen of the main program
Username:
Password:
Login button and close button
"""

from tkinter import *
from tkinter import messagebox
import backend as bk


# Commands
def login_command(event=None):
    if bk.login(username.get(), password.get()):
        window.destroy()
        import app
        app.success()
    else:
        messagebox.showwarning(
            'Login error', 'The username or password is incorrect!'
        )


window = Tk()
window.title('Alpha Healthcare Login')
window.configure(bg='teal')
window.resizable(False, False)
window.config(padx=10)

# Display
title1 = Label(window, text='--------- |\u03B1|\u2122 ---------', fg='yellow', bg='teal')
title1.grid(row=0, column=0, columnspan=2)

title2 = Label(window, text='Alpha healthcare\u2122 PORTAL', fg='yellow', bg='teal')
title2.grid(row=1, column=0, columnspan=2)

# Entry labels and fields
l1 = Label(window, text='Username:', fg='white', bg='teal')
l1.grid(row=2, column=0)

l2 = Label(window, text='Password:', fg='white', bg='teal')
l2.grid(row=3, column=0)

username = StringVar()
e1 = Entry(window, textvariable=username)
e1.grid(row=2, column=1)

password = StringVar()
e2 = Entry(window, textvariable=password, show='●')
e2.grid(row=3, column=1)
e2.bind('<Return>', login_command)

# Login button with lime background and spanning width of 2 columns
b1 = Button(window,
            text='Login',
            bg='lime',
            command=login_command,
            activebackground='green',
            activeforeground='white')
b1.grid(row=4,
        column=0,
        columnspan=2,
        sticky=W + E,
        pady=5)

# Close button to destroy the window
b2 = Button(window,
            text='Close',
            bg='red',
            command=window.destroy)
b2.grid(row=5,
        column=0,
        columnspan=2,
        sticky=W + E,
        pady=5)

window.mainloop()
