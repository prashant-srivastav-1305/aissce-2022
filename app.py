from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import simpledialog
import prettytable as pt
import backend as bk

# FONT TUPLE : TYPE CONSOLAS ,SIZE 11
font = ('Consolas', 11)
def success():
    print('True')


# ------------------------------------------COMMANDS---------------------------------------------------------------


# ADDING A PATIENT (BUTTON b1 @ LINES 311-318)
# USE FUNCTION bk.addPatient() WITH ALL THE PARAMETERS FROM THE ENTRIES ,RADIOBUTTONS AND DROP-DOWN LISTS
# SHOW THE OUTPUT IN A TABULAR FORM WITH prettytable AND tkinter.scrolledtext
# EXCEPTION HANDLING WHEN ALL THE REQUIRED FIELDS ARE NOT FILLED
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


# SEARCHING A PATIENT (BUTTON b2 @ LINES 321-328)
# USE FUNCTION bk.getInfo() WITH ALL THE PARAMETERS FROM THE ENTRIES, RADIOBUTTONS AND DROP-DOWN LISTS
# SHOW THE SEARCHED INFORMATION IN A TABULAR FORM WITH prettytable AND tkinter.scrolledtext
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


# UPDATING A PATIENT (BUTTON b3 @ LINES 332-336)
# TAKE THE ID TO UPDATE USING tkinter.simpledialog AND STORING THE ID IN choice 
# USE THE FUNCTION bk.updatePatient_search() TO SEARCH FOR THE REQUIRED ID
# IF PATIENT IS FOUND THEN ALL THE INFO IS SET INTO THE ENTRIES, WHICH THE USER CAN MODIFY
# AFTER THE INFO IS SET INTO THE ENTRIES, UPDATE PATIENT BUTTON IS DISABLED AND CONFIRM BUTTON IS ENABLED
# THE USER CAN PRESS THE CONFIRM BUTTON TO MAKE THE CHANGES (BUTTON b33 @ LINES )
# IS THE ID IS NOT FOUND, A WARNING IS SHOWN USING tkinter.messagebox.showwarning()
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


# CONFIRM COMMAND (BUTTON b33 @ LINES 349-351)
# THIS COMMAND IS USED AFTER THE CONFIRM BUTTON IS ENABLED WHEN THE PATIENT RECORD IS FOUND IN THE DATABASE
# AND THE ENTRIES ARE SET WITH THE INFO. THE USER NEEDS TO PRESS THIS BUTTON AFTER HE/SHE HAS MODIFIES THE INFORMATION
# IT USES THE bk.updatePatient() COMMAND WITH ALL THE REQUIRED PARAMETERS TO UPDATE THE PATIENT
# THE ENTRIES ARE SET TO THEIR DEFAULT VALUES AND ALL THE INFO IS SHOWN IN TABULAR FORM WITH THE show_all_command() (@ LINES )
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


# ADMIT A PATIENT (BUTTON b31 @ LINES 339-340)
# USE THE FUNCTION bk.admit() WITH ALL THE REQUIRED PARAMETERS TO ADMIT A PATIENT
# EXCEPTION HANDLING IF ALL THE DATA IS NOT ENTERED 
# APPROPRIATE MESSAGE IS SHOWN USING tkinter.messagebox.showwarning()
def admit_command():
    try:
        bk.admit(
            name.get(), name2.get(), age.get(), sex.get(), ward.get(), doctor.get(), days_to_admit.get()
        )
        show_all_command()
    except:
        messagebox.showwarning('Data entry error', 'You have not entered all data!')


# DISCHARGING A PATIENT (BUTTON b32 @ LINES 344-345)
# WORK REMAINING.....
def discharge_command():
    return 1.2


# SHOWING ALL DATA (BUTTON b4 @ LINES 354-361)
# SHOW ALL DATA IN THE SCROLLEDTEXT WIDGET USING THE bk.showAll() FUNCTION
# THE SCROLLEDTEXT WIDGgithubET'S STATE IS DISABLED ONCE THE INFORMATION IS DISPLAYED 
# SO THAT NO ONE CAN MODIFY IT EXPLICITLY
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


# LOGOUT  (BUTTON b5 @ LINES 364-371)
# THE USER IS PROMPTED FOR A CHOICE USING tkinter.messagebox.askyesno()
# IF THE USER SELECTS YES THE login_screen.py FILE IS RUN AND THE CURRENT WINDOW IS DESTROYED
# ELSE NOTHING IS DONE AND THE USER REMAINS IN THE CURRENT WINDOW
def logout_command():
    choice = messagebox.askyesno('Logout', 'Do you want to logout?')
    if choice:
        window.destroy()
        import login_screen
    elif not choice:
        pass

# -----------------------------------------------MAIN PROGRAM-----------------------------------------------------------

window = Tk()
window.title('Alpha Healthcare Portal')
window.geometry('750x725')
window.resizable(False, False)

#================================[LABELS]=======================================

# NAME
l1 = Label(window, text='Name:', width=10, anchor=E)
l1.grid(row=0, column=0, sticky=E)
l1.configure(font=font)

# AGE
l2 = Label(window, text='Age:', anchor=E)
l2.grid(row=1, column=0, sticky=E)
l2.configure(font=font)

# SEX 
l3 = Label(window, text='Sex:', anchor=E)
l3.grid(row=2, column=0, sticky=E)
l3.configure(font=font)

# WARD 
l4 = Label(window,
           text='Ward:',
           width=10,
           anchor=E)
l4.grid(row=3, column=0, sticky=E)
l4.configure(font=font)

# DOCTOR 
l5 = Label(window,
           text='Doctor:',
           width=10,
           anchor=E)
l5.grid(row=4, column=0, sticky=E)
l5.configure(font=font)

# STATUS
l6 = Label(window,
           text='Status:',
           anchor=E)
l6.grid(row=5, column=0, sticky=E)
l6.configure(font=font)

# NUMBER OF DAYS CONSULTED/ADMITTED
l7 = Label(window,
           text='Number of days consulted/admitted:',
           anchor=E)
l7.grid(row=6,
        column=0,
        sticky=E)
l7.configure(font=font)

#================================[ENTRIES]============================================

# THIS FRAME HOLDS THE FIRST AND THE LAST NAME ENTRIES
name_frame = Frame(window)
name_frame.grid(row=0,
                column=1,
                sticky=W,
                padx=4)

# FIRST NAME
name = StringVar()
name.set('First name')
e1 = Entry(name_frame, textvariable=name)
e1.grid(row=0,
        column=0,
        columnspan=2,
        sticky=W)
e1.configure(font=font)

# LAST NAME
name2 = StringVar()
name2.set('Last name')
e2 = Entry(name_frame, textvariable=name2)
e2.grid(row=0,
        column=2,
        columnspan=2,
        sticky=W)
e2.configure(font=font)

# AGE
# THE AGE IS STORED IN A StringVar() age
age = StringVar()
e3 = Entry(window, textvariable=age, width=5)
e3.grid(row=1, column=1, sticky=W, padx=4)
e3.configure(font=font)

# DAYS ADMITTED/CONSULTED
# THE INFORMATION IS STORED IN A StringVar() days_to_admit
days_to_admit = StringVar()
days_to_admit.set(1)
e4 = Entry(window, textvariable=days_to_admit)
e4.grid(row=6, column=1, sticky=W)
e4.configure(font=font)

#===============================[DROPDOWN LISTS]===================================

# SEX
options1 = ['Male', 'Female', 'Other']
sex = StringVar()
sex.set('Male')
dd1 = OptionMenu(window, sex, *options1)
dd1.grid(row=2, column=1, sticky=W)
dd1.configure(font=font)

# PATIENT WARD
options2 = ['Select', 'OPD', 'General', 'Special', 'COVID-19', 'ICU']
ward = StringVar()
ward.set('Select')
dd2 = OptionMenu(window, ward, *options2)
dd2.grid(row=3, column=1, sticky=W)
dd2.configure(font=font)

# DOCTOR NAMES
options3 = ['Select', 'Rajeev Kumar', 'Suraj Chaudhry', 'Jyothi Anand', 'Amandeep Singh']
doctor = StringVar()
doctor.set('Select')
dd3 = OptionMenu(window, doctor, *options3)
dd3.grid(row=4, column=1, sticky=W)
dd3.configure(font=font)

#===================================[RADIO BUTTONS]=======================================

# THIS FRAME HOLDS ALL THE RADIO BUTTONS USED TO SELECT THE STATUS
radio_frame = Frame(window)
radio_frame.grid(row=5,
                 column=1,
                 sticky=W)

# PATIENT STATUS IS STORES IN A StringVar() status
status = StringVar()
# FIRST RADIOBUTTON; STATUS: 'Admit'
r1 = Radiobutton(radio_frame, text='Admit', variable=status, value='Admit')
r1.grid(row=0, column=0, sticky=W)
r1.configure(font=font)
# SECOND RADIOBUTTON; STATUS: 'Checkup'
r2 = Radiobutton(radio_frame, text='Checkup', variable=status, value='Checkup')
r2.grid(row=0, column=1, sticky=W)
r2.configure(font=font)

#===================================[BUTTONS]===============================================

# THIS FRAME HOLDS ALL THE BUTTONS USED FOR THE DIFFERENT OPERATIONS
op_frame = Frame(window)
op_frame.grid(row=7,
              column=0,
              columnspan=2,
              padx=60,
              pady=10)

# ADD PATIENT 
b1 = Button(op_frame,
            text='Add patient',
            width=12,
            command=add_patient_command)
b1.grid(row=0,
        column=0,
        rowspan=2,
        sticky=N + E + W + S)

# SEARCHING A PATIENT
b2 = Button(op_frame,
            text='Search patient',
            width=12,
            command=search_patient_command)
b2.grid(row=0,
        column=1,
        rowspan=2,
        sticky=N + E + W + S)

# UPDATING A PATIENT
# ADMIT, DISCHARGE AND CONFIRM ARE BASICALLY EXTENSIONS OF THE UPDATE PATIENT BUTTON
b3 = Button(op_frame, 
            text='Update patient', 
            width=15, 
            command=update_patient_command)
b3.grid(row=0, column=2,sticky=W + E)

# ADMITTING A PATIENT
b31 = Button(op_frame, text='Admit patient', width=15, command=admit_command)
b31.grid(row=1, column=2)

# DISCHARGING A PATIENT
# WORK REMANING ON THIS....
b32 = Button(op_frame, text='Discharge patient', width=15)
b32.grid(row=1, column=3)

# CONFIRM BUTTON
# USED TO CONFIRM THAT THE INFORMATION UPDATED SHOULD BE COMMITTED
b33 = Button(op_frame, text='Confirm',width=15)
b33.grid(row=0, column=3)
b33.config(state='disabled', command=confirm_command)

# SHOW ALL ENTRIES
b4 = Button(op_frame,
            text='Show all',
            width=12,
            command=show_all_command)
b4.grid(row=0,
        column=4,
        rowspan=2,
        sticky=N + E + W + S)

# LOGOUT BUTTON
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

#===============================[SCROLLEDTEXT WIDGET]===============================================

# THIS IS USED TO DISPLAY THE TABLES IN THE APPLICATION
st1 = scrolledtext.ScrolledText(window, font=('Consolas', '11'), state='disabled', width=90)
st1.grid(row=8, column=0, columnspan=9)
st1.config(background='#f0f0ed')

window.mainloop()

#----------------------------------------------------------END---------------------------------------------------------------
