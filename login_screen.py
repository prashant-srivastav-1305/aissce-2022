"""
This is the login screen of the main program
Username:
Password:
Login button and close button
"""

from tkinter import *
from tkinter import messagebox
import backend as bk

font = ('Courier New', 12, 'bold')
font2 = ('Consolas', 16, 'bold','underline')


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
icon = PhotoImage(file='alpha.png')
window.iconphoto(False, icon)


# Image
img = PhotoImage(file='main_logo.png')
img_button = Button(window, image=img)
img_button.grid(row=0,
                column=0,
                pady=5)

# Frame to display everything
mainFrame = Frame(window, bg='teal')
mainFrame.grid(row=1, column=0)

# Display
title2 = Label(mainFrame, text='Alpha healthcare\u2122 PORTAL', fg='yellow', bg='teal')
title2.grid(row=0, column=0, columnspan=2)
title2.configure(font=font2)

# Entry labels and fields
l1 = Label(mainFrame, text='Username:', fg='white', bg='teal')
l1.grid(row=1, column=0)
l1.configure(font= font)

l2 = Label(mainFrame, text='Password:', fg='white', bg='teal')
l2.grid(row=2, column=0)
l2.configure(font=font)

username = StringVar()
e1 = Entry(mainFrame, textvariable=username)
e1.grid(row=1, column=1)
e1.configure(font=font)

password = StringVar()
e2 = Entry(mainFrame, textvariable=password, show='●')
e2.grid(row=2,
        column=1)
e2.bind('<Return>', login_command)
e2.configure(font=font)

# Login button with lime background and spanning width of 2 columns
b1 = Button(mainFrame,
            text='Login',
            bg='lime',
            command=login_command,
            activebackground='green',
            activeforeground='white')
b1.grid(row=3,
        column=0,
        columnspan=2,
        sticky=W + E,
        pady=5)
b1.configure(font=font)

# Close button to destroy the window
b2 = Button(mainFrame,
            text='Close',
            bg='red',
            command=window.destroy)
b2.grid(row=4,
        column=0,
        columnspan=2,
        sticky=W + E,
        pady=10)
b2.configure(font=font)

window.mainloop()
