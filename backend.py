import mysql.connector as sql

# def username_connect():
#     c = sql.connect(host='localhost', user='root', password='password')
#     cursor = c.cursor()

"""
Login backend (login_screen.py)
1. Connect the MySQL database and retrieve data from usernames table for comparison
2. Returns True if perfect match found, False otherwise
"""


def login(username, password):
    db = sql.connect(host='?', user='?', password='?')
    cursor = db.cursor()
    cursor.execute('USE alpha_healthcare')
    cursor.execute(f"SELECT * FROM usernames WHERE username='{username}' AND psswd='{password}';")
    if len(cursor.fetchall()) == 1:
        return True
    else:
        return False


"""
Data entry backend (app.py)
"""


# Adding a patient
def addPatient(name, name2, age, sex, diagnosis, doctor, status, days=1):
    db = sql.connect(host='?', user='?', password='?')
    cursor = db.cursor()
    cursor.execute('USE alpha_healthcare')
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS patient_info('
        'id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,'
        'f_name VARCHAR(10),'
        'l_name VARCHAR(10), '
        'age INTEGER, '
        'sex VARCHAR(6), '
        'diagnosis VARCHAR(10), '
        'doctor VARCHAR(15), '
        'status VARCHAR(7), '
        'days INTEGER)',
    )
    cursor.execute(
        f"INSERT INTO patient_info(f_name,l_name, age, sex, diagnosis, doctor, status, days) "
        f"VALUES ('{name}','{name2}',{age},'{sex}','{diagnosis}','{doctor}','{status}',{days})")
    db.commit()
    db.close()


# Searching a patient
def getInfo(name="", name2="", age="", sex="", diagnosis="", doctor="", status="", days=""):
    db = sql.connect(host='?', user='?', password='?')
    cursor = db.cursor()
    cursor.execute('USE alpha_healthcare')
    cursor.execute(
        f"SELECT * FROM patient_info WHERE f_name='{name}'"
        f"OR l_name = '{name2}' "
        f"OR age='{age}'"
        f"OR sex='{sex}'"
        f"OR diagnosis='{diagnosis}'"
        f"OR doctor='{doctor}'"
        f"OR status='{status}'"
        f"OR days='{days}'"
    )
    row = cursor.fetchall()
    db.commit()
    db.close()
    return row


# Searching for update
def updatePatient_search(id):
    try:
        db = sql.connect(host='?', user='?', password='?')
        cursor = db.cursor()
        cursor.execute('USE alpha_healthcare')
        cursor.execute(
            f"SELECT * FROM patient_info WHERE id={id}"
        )
        row = cursor.fetchall()
        db.commit()
        db.close()
        if len(row) == 1:
            return True, row
        else:
            return False, False
    except sql.errors.ProgrammingError:
        return False, False


# Update patient
def updatePatient(id, name, name2, age, sex, diagnosis, doctor, status, days):
    db = sql.connect(host='?', user='?', password='?')
    cursor = db.cursor()
    cursor.execute('USE alpha_healthcare')
    cursor.execute(
        f"UPDATE patient_info SET f_name='{name}',"
        f"l_name = '{name2}',"
        f"age = {age},"
        f"sex = '{sex}',"
        f"diagnosis = '{diagnosis}',"
        f"doctor = '{doctor}',"
        f"status = '{status}',"
        f"days={days} WHERE id={id}"
    )
    db.commit()
    db.close()


# Admit patient
def admit(name, name2, age, sex, diagnosis, doctor, days):
    addPatient(name, name2, age, sex, diagnosis, doctor, status='Admit', days=days)


# Showing all entries
def showAll():
    db = sql.connect(host='?', user='?', password='?')
    cursor = db.cursor()
    cursor.execute('USE alpha_healthcare')
    cursor.execute('SELECT * FROM patient_info')
    rows = cursor.fetchall()
    main = []
    for row in rows:
        main.append(list(row))
    return main
