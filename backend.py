import mysql.connector as sql

#
# def username_connect():
#     c = sql.connect(host='localhost', user='root', password='password')
#     cursor = c.cursor()

"""
Login backend (login_screen.py)
1. Connect the MySQL database and retrieve data from usernames table for comparison
2. Returns True if perfect match found, False otherwise
"""


def login(username, password):
    db = sql.connect(host='<enter>', user='<enter>', password='<enter>')
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
def addPatient(name,name2, age, sex, diagnosis, doctor, status, days=0):
    db = sql.connect(host='<enter>', user='<enter>', password='<enter>')
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
def getInfo(name="", age="", sex="", diagnosis="", doctor="", status="", days=""):
    db = sql.connect(host='<enter>', user='<enter>', password='<enter>')
    cursor = db.cursor()
    cursor.execute('USE alpha_healthcare')
    cursor.execute(
        f"SELECT * FROM patient_info WHERE name='{name}' "
        f"OR age={age}"
        f"OR sex='{sex}'"
        f"OR diagnosis='{diagnosis}'"
        f"OR doctor='{doctor}'"
        f"OR status='{status}'"
        f"OR days={days}"
    )
    row = cursor.fetchall()
    db.commit()
    db.close()
    return row
