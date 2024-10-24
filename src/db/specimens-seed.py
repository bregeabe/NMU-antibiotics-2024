import sqlite3

connection = sqlite3.connect('antibiotics.db')
db = connection.cursor()

db.execute('''
INSERT INTO Specimens (
    specimenId, medicalRecordNumber, name, collectionDate, collectionTime, diagnosis, provider, receivingTherapy, 
    specimenType, testOrdered, receivedInLab, specimenAcceptable, cultureId, criticalResults, dayOneInfo, dayTwoInfo, 
    dayThreeInfo, dayFinalInfo, dayOneDate, dayTwoDate, dayThreeDate, dayFinalDate, dayOneTime, dayTwoTime, dayThreeTime, 
    dayFinalTime, colonyDescription, biochemicalReactions, simulatedBiochemId
)
VALUES (
    1, 708635, 'Louis Pasteur', '2024-06-11', '13:05', 'Sore in mouth', 'Dr. Renaldi', 0, 
    'Oral abscess swab', 'Routine aerobic', '13:30', 1, 11, 'Yes', 'Culture in progress', 
    '4+ Staphylococcus Aureus (sensitivity)', '4+ Staphylococcus Aureus', 
    '4+ Staphylococcus (sensitivity complete)', '2024-06-12', '2024-06-13', '2024-06-14', '2024-06-14', 
    '08:00', '08:10', '08:25', '08:25', 'Medium white, beta', 'Gram-positive cocci clusters, catalase pos, coagulase pos, Staph latex pos', 1
);
''')

db.execute('''                
INSERT INTO SimulatedBiochemInfo (
    simulatedBiochemId, test, inoculation, temperature, duration, atmosphericConditions
) VALUES (
    1, 'MSA', '4 quadrant streak for isolation', 37, '10-24hrs', 'Ambient'
);
''')

db.execute('''         
INSERT INTO PatientSpecimens (userPatientId, specimenId) VALUES (1, 1)
''')

connection.commit()
connection.close()

print("Specimens seeded successfully.")
