import sqlite3

def getAllPatients():
    connection = sqlite3.connect('antibiotics.db')
    db = connection.cursor()
    
    db.execute('SELECT * FROM Patients')
    
    patients = db.fetchall()
    for patient in patients:
        print(f"Patient ID: {patient[0]}")
        print(f"MRN: {patient[1]}")
        print(f"Name: {patient[2]}")
        print(f"Date of Birth: {patient[3]}")
        print(f"Gender: {patient[4]}\n")
    
    connection.close()

get_all_patients()
