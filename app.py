"""
07.01.2022 - GUI - adding patients - logout - table structure defined
09.01.2022 - searching - updating - admit - logout - show all entries - GUI improvement - diagnosis changed to ward
Future thoughts - discharge patient - calculation of fees - no. of available wards
"""


from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import simpledialog
import prettytable as pt
import backend as bk

font = ('Consolas', 11)
def success():
    print('True')


"""Commands"""


# Adding a patient
def add_patient_command():
    try:
        bk.addPatient(name.get(), name2.get(), age.get(), sex.get(), ward.get(), doctor.get(), status.get(),
                      days_to_admit.get())
        # Pretty Table
        table = pt.PrettyTable(['F_Name', 'L_Name', 'Age', 'Sex', 'Ward', 'Doctor', 'Status', 'Days'])
        table.add_row(
            [name.get(), name2.get(), age.get(), sex.get(), ward.get(), doctor.get(), status.get(),
             days_to_admit.get()])
        st1.config(state='normal')
        st1.delete('1.0', 'end')
        st1.insert(1.0, table)
        st1.config(state='disabled')
    except:
        messagebox.showwarning('Data entry error', 'You have not entered all data!')


# Searching a patient
def search_patient_command():
    searched = bk.getInfo(
        name.get(), name2.get(), age.get(), sex.get(), ward.get(), doctor.get(), status.get(), days_to_admit.get())
    table = pt.PrettyTable(['ID', 'F_Name', 'L_Name', 'Age', 'Sex', 'Ward', 'Doctor', 'Status', 'Days'])
    for row in searched:
        table.add_row(row)
    st1.config(state='normal')
    st1.delete('1.0', 'end')
    st1.insert(1.0, table)
    st1.config(state='disabled')


# Update a patient
def update_patient_command():
    global choice
    choice = simpledialog.askinteger('Update', 'Enter ID to update:')
    result = bk.updatePatient_search(choice)
    if result[0]:
        name.set(result[1][0][1])
        name2.set(result[1][0][2])
        age.set(result[1][0][3])
        sex.set(result[1][0][4])
        ward.set(result[1][0][5])
        doctor.set(result[1][0][6])
        status.set(result[1][0][7])
        days_to_admit.set(result[1][0][8])
        messagebox.showinfo('Data entry','Please change the data to be updated and then press the confirm button!')
        b3.config(state='disabled')
        b1.config(state='disabled')
        b2.config(state='disabled')
        b33.config(state='normal')
    else:
        messagebox.showwarning('ID not found','The ID you entered is not in the database!')


# Confirm command
def confirm_command():
    bk.updatePatient(
        choice, name.get(), name2.get(), age.get(), sex.get(), ward.get(), doctor.get(), status.get(),
        days_to_admit.get()
    )
    b33.config(state='disabled')
    b1.config(state='normal')
    b2.config(state='normal')
    b3.config(state='normal')
    name.set('First name')
    name2.set('Last name')
    age.set('')
    sex.set('Male')
    ward.set('Select')
    doctor.set('Select')
    status.set('Admit')
    days_to_admit.set('')
    show_all_command()


# Admit a patient
def admit_command():
    try:
        bk.admit(
            name.get(), name2.get(), age.get(), sex.get(), ward.get(), doctor.get(), days_to_admit.get()
        )
        show_all_command()
    except:
        messagebox.showwarning('Data entry error', 'You have not entered all data!')


# Discharging a patient
def discharge_command():
    return 1.2


# Showing all data
def show_all_command():
    table_info = bk.showAll()
    if len(table_info) != 0:
        table = pt.PrettyTable(['ID', 'F_Name', 'L_Name', 'Age', 'Sex', 'Ward', 'Doctor', 'Status', 'Days'])
        for row in table_info:
            table.add_row(row)
        st1.config(state='normal')
        st1.delete('1.0', 'end')
        st1.insert(1.0, table)
        st1.config(state='disabled')


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
window.geometry('750x725')
window.resizable(False, False)

# Labels
l1 = Label(window, text='Name:', width=10, anchor=E)
l1.grid(row=0, column=0, sticky=E)
l1.configure(font=font)

l2 = Label(window, text='Age:', anchor=E)
l2.grid(row=1, column=0, sticky=E)
l2.configure(font=font)

l3 = Label(window, text='Sex:', anchor=E)
l3.grid(row=2, column=0, sticky=E)
l3.configure(font=font)

l4 = Label(window,
           text='Ward:',
           width=10,
           anchor=E)
l4.grid(row=3, column=0, sticky=E)
l4.configure(font=font)

l5 = Label(window,
           text='Doctor:',
           width=10,
           anchor=E)
l5.grid(row=4, column=0, sticky=E)
l5.configure(font=font)

l6 = Label(window,
           text='Status:',
           anchor=E)
l6.grid(row=5, column=0, sticky=E)
l6.configure(font=font)

l7 = Label(window,
           text='Number of days consulted/admitted:',
           anchor=E)
l7.grid(row=6,
        column=0,
        sticky=E)
l7.configure(font=font)

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
e1.configure(font=font)

name2 = StringVar()
name2.set('Last name')
e2 = Entry(name_frame, textvariable=name2)
e2.grid(row=0,
        column=2,
        columnspan=2,
        sticky=W)
e2.configure(font=font)

age = StringVar()
e3 = Entry(window, textvariable=age, width=5)
e3.grid(row=1, column=1, sticky=W, padx=4)
e3.configure(font=font)

days_to_admit = StringVar()
days_to_admit.set(1)
e4 = Entry(window, textvariable=days_to_admit)
e4.grid(row=6, column=1, sticky=W)
e4.configure(font=font)

# Dropdown lists
options1 = ['Male', 'Female', 'Other']
sex = StringVar()
sex.set('Male')
dd1 = OptionMenu(window, sex, *options1)
dd1.grid(row=2, column=1, sticky=W)
dd1.configure(font=font)

options2 = ['Select', 'OPD', 'General', 'Special', 'COVID-19', 'ICU']
ward = StringVar()
ward.set('Select')
dd2 = OptionMenu(window, ward, *options2)
dd2.grid(row=3, column=1, sticky=W)
dd2.configure(font=font)

options3 = ['Select', 'Rajeev Kumar', 'Suraj Chaudhry', 'Jyothi Anand', 'Amandeep Singh']
doctor = StringVar()
doctor.set('Select')
dd3 = OptionMenu(window, doctor, *options3)
dd3.grid(row=4, column=1, sticky=W)
dd3.configure(font=font)

# Radio button frame
radio_frame = Frame(window)
radio_frame.grid(row=5,
                 column=1,
                 sticky=W)
# Radio buttons
status = StringVar()
r1 = Radiobutton(radio_frame, text='Admit', variable=status, value='Admit')
r1.grid(row=0, column=0, sticky=W)
r1.configure(font=font)
r2 = Radiobutton(radio_frame, text='Checkup', variable=status, value='Checkup')
r2.grid(row=0, column=1, sticky=W)
r2.configure(font=font)

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
            width=12,
            command=search_patient_command)
b2.grid(row=0,
        column=1,
        rowspan=2,
        sticky=N + E + W + S)

b3 = Button(op_frame, text='Update patient', width=15, command=update_patient_command)
b3.grid(row=0, column=2,sticky=W + E)

b4 = Button(op_frame,
            text='Show all',
            width=12,
            command=show_all_command)
b4.grid(row=0,
        column=4,
        rowspan=2,
        sticky=N + E + W + S)

b31 = Button(op_frame, text='Admit patient', width=15, command=admit_command)
b31.grid(row=1, column=2)

b32 = Button(op_frame, text='Discharge patient', width=15)
b32.grid(row=1, column=3)

b33 = Button(op_frame, text='Confirm',width=15)
b33.grid(row=0, column=3)
b33.config(state='disabled', command=confirm_command)

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
