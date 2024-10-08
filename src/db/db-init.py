import sqlite3

connection = sqlite3.connect('antibiotics.db')
db = connection.cursor()

db.execute('DROP TABLE IF EXISTS SimulatedBiochemInfo')
db.execute('DROP TABLE IF EXISTS SimulatedBiochems')
db.execute('DROP TABLE IF EXISTS SimulatedCultures')
db.execute('DROP TABLE IF EXISTS CultureReadout')
db.execute('DROP TABLE IF EXISTS Specimens')
db.execute('DROP TABLE IF EXISTS Patients')

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
    patientId INT,
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
    FOREIGN KEY (patientId) REFERENCES Patients(patientId)
);
''')

db.execute('''
CREATE TABLE IF NOT EXISTS CultureReadout (
    cultureId INT PRIMARY KEY,
    specimenId INT,
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
    FOREIGN KEY (specimenId) REFERENCES Specimens(specimenId)
);        
''')

db.execute('''
CREATE TABLE IF NOT EXISTS SimulatedCultures (
    simulatedCultureId INT PRIMARY KEY,
    specimenId INT,
    colonyDescription TEXT,
    biochemicalReactions TEXT,
    FOREIGN KEY (specimenId) REFERENCES Specimens(specimenId)
);        
''')

db.execute('''
    CREATE TABLE IF NOT EXISTS SimulatedBiochems (
    simulatedBiochemId INT PRIMARY KEY,
    simulatedCultureId INT,
    FOREIGN KEY (simulatedCultureId) REFERENCES SimulatedCultures(simulatedCultureId)
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
    FOREIGN KEY (simulatedBiochemId) REFERENCES SimulatedBiochems(simulatedBiochemId)
);
''')


connection.commit()
connection.close()


