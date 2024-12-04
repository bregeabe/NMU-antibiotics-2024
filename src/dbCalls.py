import sqlite3

connection = sqlite3.connect('antibiotics.db')
db = connection.cursor()

def getAllPatients(db):
    db.execute('SELECT * FROM Patients')
    patients = db.fetchall()
    connection.close()
    return patients

def get_patient_id_by_mrn(mrn):
    connection = None
    try:
        connection = sqlite3.connect('antibiotics.db')
        db = connection.cursor()

        db.execute('''
            SELECT patientId
            FROM Patients
            WHERE mrn = ?
        ''', (mrn,))
        result = db.fetchone()

        return result[0] if result else None

    except Exception as e:
        print(f"Error in get_patient_id_by_mrn: {e}")
        return None

    finally:
        if connection:
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

def get_patient_data(patient_id):
    connection = sqlite3.connect('antibiotics.db')
    cursor = connection.cursor()

    try:
        cursor.execute('''
            SELECT name, dob, mrn, gender
            FROM Patients
            WHERE patientId = ?
        ''', (patient_id,))
        patient_data = cursor.fetchone()

        if patient_data:
            return list(patient_data)
        else:
            print(f"No patient data found for patient_id: {patient_id}")
            return None
    except Exception as e:
        print(f"Error fetching patient data: {e}")
        return None
    finally:
        connection.close()

def get_specimen_data(patient_id):
    connection = sqlite3.connect('antibiotics.db')
    cursor = connection.cursor()

    cursor.execute('''
        SELECT Specimens.*
        FROM PatientSpecimens
        JOIN UserPatients ON PatientSpecimens.userPatientId = UserPatients.userPatientId
        JOIN Specimens ON PatientSpecimens.specimenId = Specimens.specimenId
        WHERE UserPatients.patientId = ?
    ''', (patient_id,))
    specimen_data = cursor.fetchone()

    connection.close()
    return specimen_data

def get_user_patient_id(self, patientId=None):
    connection = sqlite3.connect('antibiotics.db')
    cursor = connection.cursor()
    if not patientId:
        patientId = self.patient_id

    cursor.execute('''
        SELECT userPatientId FROM UserPatients
        WHERE userId = ? AND patientId = ?
    ''', (self.current_user_id, patientId))

    result = cursor.fetchone()

    if result:
        user_patient_id = result[0]
    else:
        cursor.execute('''
            INSERT INTO UserPatients (userId, patientId) VALUES (?, ?)
        ''', (self.current_user_id, patientId))
        connection.commit()
        user_patient_id = cursor.lastrowid

    if user_patient_id is None:
        cursor.execute('''
            SELECT userPatientId FROM UserPatients
            WHERE userId = ? AND patientId = ?
        ''', (self.current_user_id, patientId))
        user_patient_id = cursor.fetchone()[0]

    connection.close()
    return user_patient_id

def getAllUsers(db):
    db.execute('SELECT * FROM Users')
    users = db.fetchall()
    connection.close()
    return users