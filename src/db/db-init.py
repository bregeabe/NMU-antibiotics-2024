import sqlite3

connection = sqlite3.connect('antibiotics.db')
db = connection.cursor()

db.execute('DROP TABLE IF EXISTS SimulatedBiochemInfo')
db.execute('DROP TABLE IF EXISTS Specimens')
db.execute('DROP TABLE IF EXISTS Patients')
db.execute('DROP TABLE IF EXISTS Users')
db.execute('DROP TABLE IF EXISTS UserPatients')
db.execute('DROP TABLE IF EXISTS PatientSpecimens')


db.execute('''
CREATE TABLE IF NOT EXISTS Patients (
    patientId INT PRIMARY KEY,
    mrn INT,
    name TEXT NOT NULL,
    dob DATE,
    gender TEXT NOT NULL
);
''')

db.execute('''
CREATE TABLE IF NOT EXISTS Specimens (
    specimenId INT PRIMARY KEY,
    medicalRecordNumber INT,
    name TEXT NOT NULL,
    collectionDate DATE,
    collectionTime TIME,
    diagnosis TEXT,
    provider TEXT,
    receivingTherapy bool,
    specimenType TEXT,
    testOrdered TEXT,
    receivedInLab TIME,
    specimenAcceptable bool,
    
    cultureId INT,
    criticalResults TEXT,
    dayOneInfo TEXT,
    dayTwoInfo TEXT,
    dayThreeInfo TEXT,
    dayFourInfo TEXT,
    dayFiveInfo TEXT,
    dayFinalInfo TEXT,
    dayOneDate DATE,
    dayTwoDate DATE,
    dayThreeDate DATE,
    dayFourDate DATE,
    dayFiveDate DATE,
    dayFinalDate DATE,
    dayOneTime TIME,
    dayTwoTime TIME,
    dayThreeTime TIME,
    dayFourTime TIME,
    dayFiveTime TIME,
    dayFinalTime TIME,
           
    simulatedCultureId INT,
    colonyDescription TEXT,
    biochemicalReactions TEXT,
    
    simulatedBiochemId INT
);
''')

db.execute('''
CREATE TABLE IF NOT EXISTS SimulatedBiochemInfo (
    biochemInfoId INT PRIMARY KEY,
    simulatedBiochemId INT,
    test TEXT,
    inoculation TEXT,
    temperature INT,
    duration TEXT,
    atmosphericConditions TEXT,
    FOREIGN KEY (simulatedBiochemId) REFERENCES Specimens(simulatedBiochemId)
);
''')

db.execute('''
CREATE TABLE IF NOT EXISTS Users (
    userId INT PRIMARY KEY,
    nmuIN INT,
    firstName TEXT NOT NULL,
    lastName TEXT NOT NULL
);  
''')

db.execute('''
CREATE TABLE IF NOT EXISTS UserPatients (
    userPatientId INT PRIMARY KEY,
    userId INT,
    patientId INT,
    FOREIGN KEY (userId) REFERENCES Users(userId),
    FOREIGN KEY (patientId) REFERENCES Patients(patientId)
);
''')

db.execute('''
CREATE TABLE IF NOT EXISTS PatientSpecimens (
    patientSpecimenId INT PRIMARY KEY,
    userPatientId INT,
    specimenId INT,
    FOREIGN KEY (userPatientId) REFERENCES UserPatient(userPatientId),
    FOREIGN KEY (specimenId) REFERENCES Specimens(specimenId)
);
''')



connection.commit()
connection.close()


