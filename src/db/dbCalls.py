import sqlite3

connection = sqlite3.connect('antibiotics.db')
db = connection.cursor()

def getAllPatients(db):
    db.execute('SELECT * FROM Patients')
    
    patients = db.fetchall()
    for patient in patients:
        print(f"Patient ID: {patient[0]}")
        print(f"MRN: {patient[1]}")
        print(f"Name: {patient[2]}")
        print(f"Date of Birth: {patient[3]}")
        print(f"Gender: {patient[4]}\n")
    
    connection.close()

def getCultureReadoutForPatientSpecimen(db, patientSpecimenId):
    db.execute('''
        SELECT Specimens.cultureId, Specimens.criticalResults, Specimens.dayOneInfo, Specimens.dayTwoInfo, Specimens.dayThreeInfo, Specimens.dayFourInfo, Specimens.dayFiveInfo, Specimens.dayFinalInfo, Specimens.dayOneDate, Specimens.dayTwoDate, Specimens.dayThreeDate, Specimens.dayFourDate, Specimens.dayFiveDate, Specimens.dayFinalDate, Specimens.dayOneTime, Specimens.dayTwoTime, Specimens.dayThreeTime, Specimens.dayFourTime, Specimens.dayFiveTime, Specimens.dayFinalTime 
        FROM PatientSpecimens
        JOIN Specimens ON PatientSpecimens.specimenId = Specimens.specimenId
        Where PatientSpecimens.patientSpecimenId = ?
    ''', (patientSpecimenId))
    return db.fetchone()

def getUserPatients (db, userPatientId):
    db.execute('''
        SELECT * From UserPatients;
    ''')
    return db.fetchone()

print(getUserPatients(db, 1))