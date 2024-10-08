import sqlite3

patients_data = [
    {"MRN": 774553, "name": "Lister, Joseph", "DOB": "01/25/97", "Sex": "Male"},
    {"MRN": 823956, "name": "Charpentier, Emmanuelle", "DOB": "11/11/42", "Sex": "Female"},
    {"MRN": 289635, "name": "Loeffler, Friedrich", "DOB": "11/11/97", "Sex": "Male"},
    {"MRN": 998776, "name": "Price, Jessie", "DOB": "11/21/97", "Sex": "Female"},
    {"MRN": 333578, "name": "Collwell, Rita", "DOB": "06/07/38", "Sex": "Female"},
    {"MRN": 586341, "name": "Alexander, Hattie", "DOB": "04/18/02", "Sex": "Female"},
    {"MRN": 724777, "name": "Hesse, Fanny", "DOB": "03/05/55", "Sex": "Female"},
    {"MRN": 708635, "name": "Pastuer, Louis", "DOB": "06/05/78", "Sex": "Male"},
    {"MRN": 555332, "name": "Nicolle, Charles", "DOB": "08/02/22", "Sex": "Male"},
    {"MRN": 228877, "name": "Laveran, Charles", "DOB": "05/04/99", "Sex": "Male"},
    {"MRN": 135697, "name": "Noguchi, Hideyo", "DOB": "08/15/43", "Sex": "Male"},
    {"MRN": 402896, "name": "Gram, Hans Christian", "DOB": "01/31/45", "Sex": "Male"},
    {"MRN": 786534, "name": "Semmelweis, Ignaz", "DOB": "12/25/93", "Sex": "Male"},
    {"MRN": 444556, "name": "Shatz, Alexander", "DOB": "06/27/14", "Sex": "Male"},
    {"MRN": 698453, "name": "Amos, Harold", "DOB": "04/06/82", "Sex": "Male"},
    {"MRN": 914590, "name": "Curie, Marie", "DOB": "02/18/88", "Sex": "Female"},
    {"MRN": 834827, "name": "Waksman, Selman", "DOB": "05/05/91", "Sex": "Male"},
    {"MRN": 623698, "name": "Lederberg, Esther", "DOB": "02/18/90", "Sex": "Female"},
    {"MRN": 888727, "name": "Dubos, Rene", "DOB": "03/25/1963", "Sex": "Male"},
    {"MRN": 563453, "name": "Moore, Ruth Ella", "DOB": "07/18/2003", "Sex": "Female"},
    {"MRN": 303215, "name": "Fleming, Alexander", "DOB": "11/25/1964", "Sex": "Male"},
    {"MRN": 486213, "name": "Winogradsky, Sergei", "DOB": "02/25/1956", "Sex": "Male"},
    {"MRN": 998007, "name": "Roux, Emile", "DOB": "08/14/57", "Sex": "Male"},
    {"MRN": 223777, "name": "Saylers, Abigail", "DOB": "02/22/96", "Sex": "Female"},
    {"MRN": 543728, "name": "Kleineber, Emmy", "DOB": "02/22/71", "Sex": "Female"},
    {"MRN": 346890, "name": "Bugie, Elizabeth", "DOB": "07/11/45", "Sex": "Female"},
    {"MRN": 563279, "name": "Stephenson, Marjorie", "DOB": "02/18/81", "Sex": "Female"},
    {"MRN": 643728, "name": "Lancefield, Rebecca", "DOB": "02/22/75", "Sex": "Female"},
    {"MRN": 783954, "name": "Cohen, Hans", "DOB": "08/31/02", "Sex": "Male"},
]

connection = sqlite3.connect('antibiotics.db')
db = connection.cursor()

for idx, patient in enumerate(patients_data):
    patient_id = idx + 1
    db.execute('''
        INSERT INTO Patients (patientId, mrn, name, dob, gender)
        VALUES (?, ?, ?, ?, ?)
    ''', (patient_id, patient["MRN"], patient["name"], patient["DOB"], patient["Sex"]))

connection.commit()
connection.close()

print("Patients seeded successfully.")
