import sqlite3

connection = sqlite3.connect('antibiotics.db')
db = connection.cursor()

db.execute('''
CREATE TABLE IF NOT EXISTS Patients (
    patientId INT PRIMARY KEY,
    name TEXT NOT NULL,
    age INT NOT NULL,
    dateOfBirth DATE,
    gender TEXT NOT NULL
);
''')

db.execute('''
CREATE TABLE IF NOT EXISTS Specimens (
    specimenId INT PRIMARY KEY,
    name TEXT NOT NULL,
    age INT NOT NULL
);
''')

db.execute('''
CREATE TABLE IF NOT EXISTS PatientSpecimens (
    patientSpecimenId INT PRIMARY KEY,
    patientId INT,
    specimenId INT,
    medicalRecordNumber INT,
    collectionDate DATE,
    collectionTime TIME,
    diagnosis TEXT,
    provider TEXT,
    receivingTherapy bool,
    specimenType TEXT,
    testOrdered TEXT
    receivedInLab TIME,
    specimenAcceptable bool,
    colonyDescription TEXT,
    biochemicalReactionsNoted TEXT,
    
    FOREIGN KEY (patientId) REFERENCES Patients(patientId),
    FOREIGN KEY (specimenId) REFERENCES Specimens(specimenId)
);
''')

db.execute('''
CREATE TABLE IF NOT EXISTS CultureReadout (
    cultureId INT PRIMARY KEY,
    patientSpecimenId INT,
    FOREIGN KEY (patientSpecimenId) REFERENCES PatientSpecimens(patientSpecimenId)
);        
''')

db.execute('''
CREATE TABLE IF NOT EXISTS CultureReadoutInfo (
    cultureInfoId INT PRIMARY KEY,
    cultureId INT,
    day INT NOT NULL,
    info TEXT,
    finalInfo TEXT,
    date DATE,
    time TIME,
    FOREIGN KEY (cultureId) REFERENCES CultureReadout(cultureId)
);        
''')



connection.commit()
connection.close()


