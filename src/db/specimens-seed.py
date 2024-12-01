import sqlite3

connection = sqlite3.connect('antibiotics.db')
db = connection.cursor()

# Insert Specimen Requisition Data
db.execute('''
INSERT INTO SpecimenRequisition (
    userPatientId, provider, diagnosis, collectionDate, collectionTime, specimenType, testOrdered,
    receivingTherapy, receivedInLab, specimenAcceptable
)
VALUES (
    1, 'Dr. Renaldi', 'Sore in mouth', '2024-06-11', '13:05', 'Oral abscess swab', 'Routine aerobic',
    0, '13:30', 1
);
''')

# Insert Work Card Data
db.execute('''
INSERT INTO WorkCard (
    userPatientId, cultureId, priority,
    wbcQty, epiQty, gpcQty, gpbQty, gncQty, gnbQty, otherQty,
    day1Observation, day1Date, day1Time,
    day2Observation, day2Date, day2Time,
    day3Observation, day3Date, day3Time,
    day4Observation, day4Date, day4Time,
    day5Observation, day5Date, day5Time,
    finalObservation, finalDate, finalTime,
    criticalResults
) VALUES (
    1, 1001, 'Routine Aerobic',
    NULL, NULL, '4+', NULL, NULL, NULL, NULL,
    'Culture in progress', '6/12/24', '8:00',
    '4+ Staphylococcus Aureus - sensitivity in progress', '6/13/24', '8:10',
    '4+ Staphylococcus Aureus - sensitivity reported', '6/14/24', '8:25',
    NULL, NULL, NULL,
    NULL, NULL, NULL,
    '4+ Staphylococcus - sensitivity complete', '6/14/24', NULL,
    NULL
);
''')

db.execute('''
INSERT INTO CultureNotes (
    userPatientId,
    colonyDescription,
    cultureWorkup,
    biochemicalReactions,
    test1Name, test1Inoculation, test1Temperature, test1Duration, test1AtmosphericConditions,
    test2Name, test2Inoculation, test2Temperature, test2Duration, test2AtmosphericConditions,
    test3Name, test3Inoculation, test3Temperature, test3Duration, test3AtmosphericConditions,
    test4Name, test4Inoculation, test4Temperature, test4Duration, test4AtmosphericConditions,
    test5Name, test5Inoculation, test5Temperature, test5Duration, test5AtmosphericConditions,
    test6Name, test6Inoculation, test6Temperature, test6Duration, test6AtmosphericConditions
)
VALUES (
    1,
    'Medium white, beta',
    '**NOTE DATES OF TESTING**',
    'Gram-positive cocci clusters\nCatalase positive\nCoagulase positive\nStaph latex positive',
    'MSA', '4 quadrant streak for isolation', 35, '18-24 hrs', 'Ambient',
    NULL, NULL, NULL, NULL, NULL,
    NULL, NULL, NULL, NULL, NULL,
    NULL, NULL, NULL, NULL, NULL,
    NULL, NULL, NULL, NULL, NULL,
    NULL, NULL, NULL, NULL, NULL
);

''')

connection.commit()
connection.close()

print("Specimen, Work Card, and Culture Notes seeded successfully.")
