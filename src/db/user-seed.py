import sqlite3

users_data = [
    {"nmuIN": 12345678901234, "firstName": "John", "lastName": "Doe", "isAdmin": "0"},
    {"nmuIN": 23456789012345, "firstName": "Jane", "lastName": "Smith", "isAdmin": "0"},
    {"nmuIN": 34567890123456, "firstName": "Alice", "lastName": "Johnson", "isAdmin": "0"},
    {"nmuIN": 2, "firstName": "Admin", "lastName": "Admin", "isAdmin": "1"}
]

connection = sqlite3.connect('antibiotics.db')
db = connection.cursor()

for user in users_data:
    db.execute('''
        INSERT INTO Users (nmuIN, firstName, lastName, isAdmin)
        VALUES (?, ?, ?, ?)
    ''', (user["nmuIN"], user["firstName"], user["lastName"], user["isAdmin"]))

db.execute('''
   INSERT INTO UserPatients (userId, patientId) Values (1, 1);
''')
db.execute('''
    INSERT INTO UserPatients (userId, patientId) Values (2, 2);
''')

connection.commit()
connection.close()

print("Users seeded successfully.")
