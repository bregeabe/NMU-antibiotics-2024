import sqlite3

users_data = [
    {"nmuIN": 12345678901234, "firstName": "John", "lastName": "Doe"},
    {"nmuIN": 23456789012345, "firstName": "Jane", "lastName": "Smith"},
    {"nmuIN": 34567890123456, "firstName": "Alice", "lastName": "Johnson"}
]

connection = sqlite3.connect('antibiotics.db')
db = connection.cursor()

for user in users_data:
    db.execute('''
        INSERT INTO Users (nmuIN, firstName, lastName)
        VALUES (?, ?, ?)
    ''', (user["nmuIN"], user["firstName"], user["lastName"]))

db.execute('''
   INSERT INTO UserPatients (userId, patientId) Values (12345678901234, 1);
''')
db.execute('''
    INSERT INTO UserPatients (userId, patientId) Values (23456789012345, 2);
''')

connection.commit()
connection.close()

print("Users seeded successfully.")
