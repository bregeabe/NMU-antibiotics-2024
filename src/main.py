from tkinter import *
import sqlite3

connection = sqlite3.connect('antibiotics.db')
db = connection.cursor()

db.execute('SELECT * FROM Patients')
rows = db.fetchall()

print(rows)
for row in rows:
    print(row)


root = Tk()
root.title("Antibiotic Report")
root.minsize(900, 750)  # width, height
root.maxsize(1000, 800)
root.geometry("300x300+50+50")  # width x height + x + y
root.mainloop()