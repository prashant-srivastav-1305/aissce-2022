"""
Remaining tasks:
1. Searching patient
2. Update patient
2.1 / 2.2 : Admit/Discharge
3. Show all
"""


from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import backend as bk
import prettytable as pt


def success():
    print('True')


"""Commands"""


# Adding a patient
def add_patient_command():
    try:
        bk.addPatient(name.get(), name2.get(), age.get(), sex.get(), diagnosis.get(), doctor.get(), status.get(),
                      days_to_admit.get())
        # Pretty Table
        table = pt.PrettyTable(['F_Name', 'L_Name', 'Age', 'Sex', 'Diagnosis', 'Doctor', 'Status', 'Days'])
        table.add_row(
            [name.get(), name2.get(), age.get(), sex.get(), diagnosis.get(), doctor.get(), status.get(),
             days_to_admit.get()])
        st1.config(state='normal')
        st1.delete('1.0', 'end')
        st1.insert(1.0, table)
        st1.config(state='disabled')
    except:
        messagebox.showwarning('Data entry error', 'You have not entered all data!')


# Searching a patient
def search_patient_command():
    return 0


# Update a patient
def update_patient_command():
    return 1


# Admit a patient
def admit_command():
    return 1.1


# Discharging a patient
def discharge_command():
    return 1.2


# Showing all data
def show_all_command():
    return 2


# Logout
def logout_command():
    choice = messagebox.askyesno('Logout', 'Do you want to logout?')
    if choice:
        window.destroy()
        import login_screen
    elif not choice:
        pass


window = Tk()
window.title('Alpha Healthcare Portal')
window.geometry('750x500')
window.resizable(False, False)

# Labels
l1 = Label(window, text='Name:', width=10, anchor=E)
l1.grid(row=0, column=0, sticky=E)

l2 = Label(window, text='Age:', anchor=E)
l2.grid(row=1, column=0, sticky=E)

l3 = Label(window, text='Sex:', anchor=E)
l3.grid(row=2, column=0, sticky=E)

l4 = Label(window,
           text='Diagnosis:',
           width=10,
           anchor=E)
l4.grid(row=3, column=0, sticky=E)

l5 = Label(window,
           text='Doctor:',
           width=10,
           anchor=E)
l5.grid(row=4, column=0, sticky=E)

l6 = Label(window,
           text='Status:',
           anchor=E)
l6.grid(row=5, column=0, sticky=E)

l7 = Label(window,
           text='Number of days to admit (if any):',
           anchor=E)
l7.grid(row=6,
        column=0,
        sticky=E)

# Entry frame
name_frame = Frame(window)
name_frame.grid(row=0,
                column=1,
                sticky=W,
                padx=4)
# Entries
name = StringVar()
name.set('First name')
e1 = Entry(name_frame, textvariable=name)
e1.grid(row=0,
        column=0,
        columnspan=2,
        sticky=W)

name2 = StringVar()
name2.set('Last name')
e2 = Entry(name_frame, textvariable=name2)
e2.grid(row=0,
        column=2,
        columnspan=2,
        sticky=W)

age = StringVar()
e3 = Entry(window, textvariable=age, width=5)
e3.grid(row=1, column=1, sticky=W, padx=4)

days_to_admit = StringVar()
days_to_admit.set(0)
e4 = Entry(window, textvariable=days_to_admit)
e4.grid(row=6, column=1, sticky=W)

# Dropdown lists
options1 = ['Male', 'Female', 'Other']
sex = StringVar()
sex.set('Male')
dd1 = OptionMenu(window, sex, *options1)
dd1.grid(row=2, column=1, sticky=W)

options2 = ['Select', 'Illness1', 'Illness2', 'Illness3', 'Illness4', 'Illness5']
diagnosis = StringVar()
diagnosis.set('Select')
dd2 = OptionMenu(window, diagnosis, *options2)
dd2.grid(row=3, column=1, sticky=W)

options3 = ['Select', 'Rajeev Kumar', 'Suraj Chaudhry', 'Jyothi Anand', 'Amandeep Singh']
doctor = StringVar()
doctor.set('Select')
dd3 = OptionMenu(window, doctor, *options3)
dd3.grid(row=4, column=1, sticky=W)

# Radio button frame
radio_frame = Frame(window)
radio_frame.grid(row=5,
                 column=1,
                 sticky=W)
# Radio buttons
status = StringVar()
r1 = Radiobutton(radio_frame, text='Admit', variable=status, value='Admit')
r1.grid(row=0, column=0, sticky=W)
r2 = Radiobutton(radio_frame, text='Checkup', variable=status, value='Checkup')
r2.grid(row=0, column=1, sticky=W)

# Operation button frame
op_frame = Frame(window)
op_frame.grid(row=7,
              column=0,
              columnspan=2,
              padx=60,
              pady=10)

# Operation buttons
b1 = Button(op_frame,
            text='Add patient',
            width=12,
            command=add_patient_command)
b1.grid(row=0,
        column=0,
        rowspan=2,
        sticky=N + E + W + S)

b2 = Button(op_frame,
            text='Search patient',
            width=12)
b2.grid(row=0,
        column=1,
        rowspan=2,
        sticky=N + E + W + S)

b3 = Button(op_frame, text='Update patient', width=30)
b3.grid(row=0, column=2, columnspan=2, sticky=W + E)

b4 = Button(op_frame,
            text='Show all',
            width=12)
b4.grid(row=0,
        column=4,
        rowspan=2,
        sticky=N + E + W + S)

b31 = Button(op_frame, text='Admit patient', width=15)
b31.grid(row=1, column=2)

b32 = Button(op_frame, text='Discharge patient', width=15)
b32.grid(row=1, column=3)

b5 = Button(op_frame,
            text='Logout',
            width=12,
            command=logout_command)
b5.grid(row=0,
        column=5,
        rowspan=2,
        sticky=N + E + W + S)

# Frame
# f1 = Frame(window, bg='teal')
# f1.grid(row=8, column=0)

# ScrollText
st1 = scrolledtext.ScrolledText(window, font=('Consolas', '11'), state='disabled', width=90)
st1.grid(row=8, column=0, columnspan=9)
st1.config(background='#f0f0ed')

window.mainloop()
