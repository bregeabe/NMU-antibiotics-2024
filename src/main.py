import sqlite3
from tkinter import *
from tkinter import messagebox

connection = sqlite3.connect('antibiotics.db')
db = connection.cursor()

db.execute('SELECT * FROM Patients')
rows = db.fetchall()
print(rows)
for row in rows:
    print(row)

def show_page(frame):
    frame.tkraise()

def login():
    username = username_entry.get()
    if username == "00":
        show_page(menu_page)
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password")

def open_create_page():
    show_page(create_page)

def open_lookup_page():
    show_page(lookup_page)

root = Tk()
root.title("Antibiotic Report")
root.geometry("1200x700")
root.grid_rowconfigure(0, weight=1) 
root.grid_columnconfigure(0, weight=1)

login_page = Frame(root)
menu_page = Frame(root)
create_page = Frame(root)
lookup_page = Frame(root)

for frame in (login_page, menu_page, create_page, lookup_page):
    frame.grid(row=0, column=0, sticky='nsew')

def configure_grid_for_centering(frame):
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_rowconfigure(1, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_columnconfigure(1, weight=1)

configure_grid_for_centering(login_page)

login_frame = Frame(login_page)
login_frame.grid(row=0, column=0, sticky='nsew') 

# Label(login_frame, text="Login", font=("Arial", 18)).grid(row=1, column=2, columnspan=2, pady=10)
Label(login_frame, text="Enter NMU IN:").grid(row=3, column=0, padx=5, pady=15, sticky='e')
username_entry = Entry(login_frame)
username_entry.grid(row=3, column=1, pady=15)
Button(login_frame, text="Login", command=login).grid(row=3, column=2, columnspan=2, pady=20)
login_frame.grid_columnconfigure(0, weight=10)
login_frame.grid_columnconfigure(2, weight=1)

configure_grid_for_centering(menu_page)

menu_frame = Frame(menu_page)
menu_frame.grid(row=0, column=0, sticky='nsew')

Label(menu_frame, text="Menu", font=("Arial", 18)).grid(row=0, column=0, columnspan=2, pady=10)
Button(menu_frame, text="Create", width=20, command=open_create_page).grid(row=1, column=0, columnspan=2, pady=10)
Button(menu_frame, text="Lookup", width=20, command=open_lookup_page).grid(row=2, column=0, columnspan=2, pady=10)
menu_frame.grid_columnconfigure(0, weight=1)
menu_frame.grid_columnconfigure(1, weight=1)


configure_grid_for_centering(create_page)

create_frame = Frame(create_page)
create_frame.grid(row=0, column=0, sticky='nsew')

Label(create_frame, text="Create Page", font=("Arial", 18)).grid(row=0, column=0, columnspan=2, pady=10)
Button(create_frame, text="Back to Menu", command=lambda: show_page(menu_page)).grid(row=1, column=0, columnspan=2, pady=10)
create_frame.grid_columnconfigure(0, weight=1)
create_frame.grid_columnconfigure(1, weight=1)

configure_grid_for_centering(lookup_page)

lookup_frame = Frame(lookup_page)
lookup_frame.grid(row=0, column=0, sticky='nsew')

Label(lookup_frame, text="Lookup Page", font=("Arial", 18)).grid(row=0, column=0, columnspan=2, pady=10)
Button(lookup_frame, text="Back to Menu", command=lambda: show_page(menu_page)).grid(row=1, column=0, columnspan=2, pady=10)
lookup_frame.grid_columnconfigure(0, weight=1)
lookup_frame.grid_columnconfigure(1, weight=1)
show_page(login_page)

root.mainloop()
