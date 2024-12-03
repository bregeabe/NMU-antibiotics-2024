import tkinter
import customtkinter
import sqlite3
from spec_req_frame import Specimen_Requisition
from patientLookupFrame import PatientLookUpFrame
from patientCreateFrame import PatientCreateFrame
from barcode_frame import BarcodeFrame
from work_card_frame import Work_Card_Frame
from culture_notes import Culture_Notes

DARK_MODE = "dark"
customtkinter.set_appearance_mode(DARK_MODE)
customtkinter.set_default_color_theme("dark-blue")

# You must run db-init and patient-seed before running program to have the program work correctly.
class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.current_user_id = None
        self.current_patient_id = None
        self.title("Change Frames")
        #self.overrideredirect(True)
        self.focus_force()
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))

        self.login_container = customtkinter.CTkFrame(self, corner_radius=10)
        self.main_container = customtkinter.CTkFrame(self, corner_radius=10)
        self.signup_container = customtkinter.CTkFrame(self, corner_radius=10)

        self.create_login_frame()
        self.create_main_frame()
        self.create_signup_frame()
        self.create_specimen_frame = PatientCreateFrame(self)
        self.lookup_frame = PatientLookUpFrame(self)
        self.spec_req_frame = Specimen_Requisition(self)
        self.workcard_frame = Work_Card_Frame(self)
        self.culture_frame = Culture_Notes(self)
        self.show_login_screen()
        self.pending_user_id = None

    def create_signup_frame(self):
        self.signup_label = customtkinter.CTkLabel(self.signup_container, text="Sign Up", font=customtkinter.CTkFont(size=24, weight="bold"))
        self.signup_label.pack(pady=50)

        self.username_entry = customtkinter.CTkEntry(self.signup_container, placeholder_text="First Name")
        self.username_entry.pack(pady=10)

        self.password_entry = customtkinter.CTkEntry(self.signup_container, placeholder_text="Last Name")
        self.password_entry.pack(pady=10)

        self.signup_button = customtkinter.CTkButton(self.signup_container, text="Sign Up", command=self.signup)
        self.signup_button.pack(pady=10)

        self.bt_to_login = customtkinter.CTkButton(self.signup_container, text="Back to Login", command=self.show_login_screen)
        self.bt_to_login.pack(pady=10)

    def create_login_frame(self):
        self.login_container.pack(fill=tkinter.BOTH, expand=True, padx=10, pady=10)

        self.login_label = customtkinter.CTkLabel(self.login_container, text="Scan NMU ID", font=customtkinter.CTkFont(size=32, weight="bold"))
        self.login_label.pack(pady=50)

        self.login_label = customtkinter.CTkLabel(self.login_container, text="or enter the 14 digit code on the back", font=customtkinter.CTkFont(size=12, weight="normal"))
        self.login_label.pack(pady=10)

        self.nmuIN_entry = customtkinter.CTkEntry(self.login_container, placeholder_text="Click", show="*")
        self.nmuIN_entry.pack(pady=10)

        self.nmuIN_entry.bind("<Return>", self.login)

        self.login_button = customtkinter.CTkButton(self.login_container, text="Login", command=self.login)
        self.login_button.pack(pady=10)

        self.bt_Quit = customtkinter.CTkButton(self.login_container, text="Quit", fg_color= '#EA0000', hover_color = '#B20000', command=self.close_window)
        self.bt_Quit.pack(pady=10)

    def create_main_frame(self):
        self.main_container.pack(fill=tkinter.BOTH, expand=True, padx=10, pady=10)

        self.left_side_panel = customtkinter.CTkFrame(self.main_container, width=150, corner_radius=10)
        self.left_side_panel.pack(side=tkinter.LEFT, fill=tkinter.Y, expand=False, padx=5, pady=5)

        self.left_side_panel.grid_columnconfigure(0, weight=1)
        self.left_side_panel.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=0)

        self.logo_label = customtkinter.CTkLabel(self.left_side_panel, text="NMU Antibiotic Report \n", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(40, 10))

        self.bt_statement = customtkinter.CTkButton(self.left_side_panel, text="Create Patient", command=self.create)
        self.bt_statement.grid(row=3, column=0, padx=20, pady=10)

        self.bt_categories = customtkinter.CTkButton(self.left_side_panel, text="Specimen Requisition", command=self.requisition)
        self.bt_categories.grid(row=4, column=0, padx=20, pady=10)

        self.bt_categories = customtkinter.CTkButton(self.left_side_panel, text="Specimen Workcard", command=self.workcard)
        self.bt_categories.grid(row=5, column=0, padx=20, pady=10)

        self.bt_categories = customtkinter.CTkButton(self.left_side_panel, text="Simulated Biochems", command=self.biochems)
        self.bt_categories.grid(row=6, column=0, padx=20, pady=10)

        self.bt_Quit = customtkinter.CTkButton(self.left_side_panel, text="Change User", fg_color= '#EA0000', hover_color = '#B20000', command=self.show_login_screen)
        self.bt_Quit.grid(row=9, column=0, padx=20, pady=10)

        self.bt_Quit = customtkinter.CTkButton(self.left_side_panel, text="Quit", fg_color= '#EA0000', hover_color = '#B20000', command=self.close_window)
        self.bt_Quit.grid(row=10, column=0, padx=20, pady=10)

        self.right_side_panel = customtkinter.CTkFrame(self.main_container, corner_radius=10, fg_color="#000811")
        self.right_side_panel.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=5, pady=5)

        self.right_dashboard = customtkinter.CTkFrame(self.main_container, corner_radius=10, fg_color="#000811")
        self.right_dashboard.pack(in_=self.right_side_panel, side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)

        self.barcode_frame = BarcodeFrame(self)
        self.bt_dashboard = customtkinter.CTkButton(self.left_side_panel, text="Patient Lookup", command=self.lookup)
        self.bt_dashboard.grid(row=2, column=0, padx=20, pady=10)
        self.bt_categories = customtkinter.CTkButton(self.left_side_panel, text="Barcode Scanning", command=self.barcode_frame.barcode)
        self.bt_categories.grid(row=1, column=0, padx=20, pady=10)


    def show_login_screen(self):
        self.main_container.pack_forget()
        self.signup_container.pack_forget()
        self.login_container.pack(fill=tkinter.BOTH, expand=True)

    def show_main_screen(self):
        self.login_container.pack_forget()
        self.main_container.pack(fill=tkinter.BOTH, expand=True)

    def show_signup_screen(self):
        self.login_container.pack_forget()
        self.main_container.pack_forget()
        self.signup_container.pack(fill=tkinter.BOTH, expand=True)
        self.signup_label = customtkinter.CTkLabel(self.signup_container, text="", fg_color="transparent")

    def signup(self):
        firstName = self.username_entry.get()
        lastName = self.password_entry.get()
        userId = self.pending_user_id

        connection = sqlite3.connect('antibiotics.db')
        db = connection.cursor()

        try:
            db.execute('''INSERT INTO Users (nmuIN, firstName, lastName) VALUES (?, ?, ?)''', (userId, firstName, lastName))
            connection.commit()
            db.execute("SELECT userId FROM Users WHERE nmuIN = ?", (userId,))
            new_user = db.fetchone()
            self.current_user_id = new_user[0]
            self.username_entry.delete(0, tkinter.END)
            self.password_entry.delete(0, tkinter.END)

            self.login_label.configure(text="Sign up successful! Please log in.", fg_color="green")
            self.show_login_screen()
        except sqlite3.IntegrityError:
            self.login_label.configure(text="User ID already exists. Try logging in.", fg_color="red")
        finally:
            connection.close()

    def login(self, event=None):
        nmuIN = int(self.nmuIN_entry.get())
        connection = sqlite3.connect('antibiotics.db')
        db = connection.cursor()

        db.execute("SELECT userId FROM Users WHERE nmuIN = ?", (nmuIN,))
        user = db.fetchone()

        if user:
            self.current_user_id = user[0]
            # print("Login Successful. Current User ID:", self.current_user_id)
            self.nmuIN_entry.delete(0, tkinter.END)
            self.show_main_screen()
        else:
            self.pending_user_id = nmuIN
            self.nmuIN_entry.delete(0, tkinter.END)
            self.show_signup_screen()
            self.signup_label.configure(text="User not found. Please sign up.")

    def lookup(self):
        self.clear_frame()
        if hasattr(self, 'lookup_frame') and self.lookup_frame:
            del self.lookup_frame
        self.lookup_frame = PatientLookUpFrame(self)
        self.lookup_frame.build()

    def create(self):
        self.clear_frame()
        if hasattr(self, 'create_specimen_frame') and self.create_specimen_frame:
            del self.create_specimen_frame
        self.create_specimen_frame = PatientCreateFrame(self)
        self.create_specimen_frame.build()

    def scanning(self):
        self.clear_frame()

    def requisition(self):
        self.spec_req_frame.build()

    def workcard(self):
        self.clear_frame()
        if hasattr(self, 'work_card_frame') and self.workcard_frame:
            del self.workcard_frame
        self.workcard_frame = Work_Card_Frame(self)
        self.workcard_frame.build()

    def biochems(self):
        self.culture_frame.build()

    def close_window(self):
        App.destroy(self)

    def clear_frame(self):
        for widget in self.right_dashboard.winfo_children():
            widget.destroy()

    def open_specimen_req(self, patient_data, patient_id):
        try:
            self.clear_frame()
            self.spec_req_frame = Specimen_Requisition(self, patient_id=patient_id)
            self.spec_req_frame.build()

            if callable(getattr(self.spec_req_frame, 'populate_form', None)):
                self.spec_req_frame.populate_form(patient_data)
            else:
                raise AttributeError("populate_form method is not defined or callable in Specimen_Requisition.")
        except Exception as e:
            print(f"Error in open_specimen_req: {e}")

    def open_work_card(self, patient_data=None):
        try:
            self.clear_frame()

            if not patient_data and hasattr(self, 'patient_data'):
                patient_data = self.patient_data

            if patient_data:
                self.workcard_frame = Work_Card_Frame(self)
                self.workcard_frame.build()
                self.workcard_frame.populate_form(patient_data)
            else:
                print("No patient data available to open Work Card.")
        except Exception as e:
            print(f"Error in open_work_card: {e}")


    def open_culture_notes(self):
        try:
            self.clear_frame()
            self.culture_notes_frame = Culture_Notes(self)
            self.culture_notes_frame.build()

            if hasattr(self.culture_notes_frame, 'populate_form') and callable(self.culture_notes_frame.populate_form):
                self.culture_notes_frame.populate_form()
            else:
                print("populate_form method is not defined or callable in Culture_Notes.")
        except Exception as e:
            print(f"Error in open_culture_notes: {e}")



a = App()
a.mainloop()