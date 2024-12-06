import sqlite3

connection = sqlite3.connect('antibiotics.db')
db = connection.cursor()

# Drop old tables (if needed)
db.execute('DROP TABLE IF EXISTS SimulatedBiochemInfo')
db.execute('DROP TABLE IF EXISTS Specimens')
db.execute('DROP TABLE IF EXISTS Patients')
db.execute('DROP TABLE IF EXISTS Users')
db.execute('DROP TABLE IF EXISTS UserPatients')
db.execute('DROP TABLE IF EXISTS PatientSpecimens')
db.execute('DROP TABLE IF EXISTS SpecimenRequisition')
db.execute('DROP TABLE IF EXISTS WorkCard')
db.execute('DROP TABLE IF EXISTS CultureNotes')

# Recreate tables
db.execute('''
CREATE TABLE IF NOT EXISTS Patients (
    patientId INTEGER PRIMARY KEY AUTOINCREMENT,
    mrn INT,
    name TEXT NOT NULL,
    dob DATE,
    gender TEXT NOT NULL
);
''')

db.execute('''
CREATE TABLE IF NOT EXISTS Users (
    userId INTEGER PRIMARY KEY AUTOINCREMENT,
    nmuIN INTEGER UNIQUE NOT NULL,
    firstName TEXT NOT NULL,
    lastName TEXT NOT NULL,
    isAdmin INTEGER DEFAULT 0,
    hasBeenViewed INTEGER DEFAULT 0
);
''')

db.execute('''
CREATE TABLE IF NOT EXISTS UserPatients (
    userPatientId INTEGER PRIMARY KEY AUTOINCREMENT,
    userId INT,
    patientId INT,
    grade TEXT,
    feedback TEXT, 
    FOREIGN KEY (userId) REFERENCES Users(userId),
    FOREIGN KEY (patientId) REFERENCES Patients(patientId)
);
''')

db.execute('''
CREATE TABLE IF NOT EXISTS SpecimenRequisition (
    requisitionId INTEGER PRIMARY KEY AUTOINCREMENT,
    userPatientId INTEGER NOT NULL UNIQUE,
    provider TEXT,
    diagnosis TEXT,
    collectionDate DATE,
    collectionTime TIME,
    specimenType TEXT,
    testOrdered TEXT,
    receivingTherapy BOOL,
    receivedInLab TIME,
    specimenAcceptable BOOL,
    FOREIGN KEY (userPatientId) REFERENCES UserPatients(userPatientId)
);
''')

db.execute('''
CREATE TABLE IF NOT EXISTS WorkCard (
    workCardId INTEGER PRIMARY KEY AUTOINCREMENT,
    userPatientId INTEGER NOT NULL UNIQUE,
    cultureId INT,
    priority TEXT,
    wbcQty TEXT,
    epiQty TEXT,
    gpcQty TEXT,
    gpbQty TEXT,
    gncQty TEXT,
    gnbQty TEXT,
    otherQty TEXT,
    day1Observation TEXT,
    day1Date TEXT,
    day1Time TEXT,
    day2Observation TEXT,
    day2Date TEXT,
    day2Time TEXT,
    day3Observation TEXT,
    day3Date TEXT,
    day3Time TEXT,
    day4Observation TEXT,
    day4Date TEXT,
    day4Time TEXT,
    day5Observation TEXT,
    day5Date TEXT,
    day5Time TEXT,
    day6Observation TEXT,
    day6Date TEXT,
    day6Time TEXT,
    criticalResults TEXT,
    FOREIGN KEY (userPatientId) REFERENCES UserPatients(userPatientId)
);
''')

db.execute('''
CREATE TABLE IF NOT EXISTS CultureNotes (
    noteId INTEGER PRIMARY KEY AUTOINCREMENT,
    userPatientId INTEGER NOT NULL UNIQUE,
    isolateNumber TEXT,
    colonyDescription TEXT,
    additionalNotes TEXT,
           
    test1Name TEXT,
    test1SetUpDate TEXT,
    test1SetUpTime INT,
    test1Results TEXT,
           
    test2Name TEXT,
    test2SetUpDate TEXT,
    test2SetUpTime TEXT,
    test2Results TEXT,
           
    test3Name TEXT,
    test3SetUpDate TEXT,
    test3SetUpTime TEXT,
    test3Results TEXT,
           
    test4Name TEXT,
    test4Inoculation TEXT,
    test4Temperature INT,
    test4Duration TEXT,
    test4AtmosphericConditions TEXT,
    test4Results TEXT,
           
    test5Name TEXT,
    test5Inoculation TEXT,
    test5Temperature INT,
    test5Duration TEXT,
    test5AtmosphericConditions TEXT,
    test5Results TEXT,
           
    test6Name TEXT,
    test6Inoculation TEXT,
    test6Temperature INT,
    test6Duration TEXT,
    test6AtmosphericConditions TEXT,
    test6Results TEXT,
           
    FOREIGN KEY (userPatientId) REFERENCES UserPatients(userPatientId)
);
''')

connection.commit()
connection.close()
