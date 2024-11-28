import customtkinter
import sqlite3
import dbCalls

class PatientCreateFrame:
    def __init__(self, main_screen):
        self.main_screen = main_screen
        self.right_dashboard = self.main_screen.right_dashboard
        self.patientFont = customtkinter.CTkFont(size=15)

    def build_search_frame(self):
        self.search_frame = customtkinter.CTkFrame(self.create_patient_frame, corner_radius=0, height=50, fg_color="#232323")
        self.result_label = customtkinter.CTkLabel(self.search_frame, text="Search Results", font=customtkinter.CTkFont(size=22, weight="bold"))
        self.search_button = customtkinter.CTkButton(self.search_frame, text="Search", width=200, command=self.search)
        self.search_bar = customtkinter.CTkEntry(self.search_frame, placeholder_text="Search...", width=200)
        self.search_bar.bind("<Return>", self.search)

    def build_labels_frame(self):
        aFont = customtkinter.CTkFont(size=18)
        self.labels_frame = customtkinter.CTkFrame(self.patient_frame, height=50, corner_radius=0, fg_color="#333333")
        self.name_label = customtkinter.CTkLabel(self.labels_frame, text="Name", font=aFont, width=200)
        self.dob_label = customtkinter.CTkLabel(self.labels_frame, text="DOB", font=aFont, width=160)
        self.sex_label = customtkinter.CTkLabel(self.labels_frame, text="Sex", font=aFont, width=150)
        self.mrn_label = customtkinter.CTkLabel(self.labels_frame, text="MRN", font=aFont, width=160)
        self.create_label = customtkinter.CTkLabel(self.labels_frame, text="Create Patient", font=aFont, width=150)

    def place_search_frame(self):
        self.search_frame.grid(column=0, row=0, sticky="ew", padx=15)
        self.result_label.pack(pady=10, padx=15, side='left')
        self.search_button.pack(pady=10, padx=15, side='right')
        self.search_bar.pack(pady=10, padx=15, side='right')

    def place_labels_frame(self):
        self.labels_frame.grid(row=0, column=0, sticky="ew")
        self.name_label.grid(row=0,column=0)
        self.dob_label.grid(row=0,column=1)
        self.sex_label.grid(row=0,column=2)
        self.mrn_label.grid(row=0,column=3)
        self.create_label.grid(row=0,column=4)

        self.labels_frame.grid_columnconfigure((0,1,2,3,4), weight=1)
        self.labels_frame.grid_rowconfigure((0), weight=1)

    def build_frames(self):
        self.lookup_label = customtkinter.CTkLabel(self.right_dashboard, text="Patients", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.create_patient_frame = customtkinter.CTkFrame(self.right_dashboard, corner_radius=10, fg_color="#232323")
        self.build_search_frame()
        self.patient_frame = customtkinter.CTkScrollableFrame(self.create_patient_frame, corner_radius=10, fg_color="#333333")
        self.build_labels_frame()

    def place_frames(self):
        self.lookup_label.pack(pady=30)
        self.create_patient_frame.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.8)
        self.create_patient_frame.grid_columnconfigure((0), weight=1)
        self.patient_frame.place(relx=0.025, rely=0.075, relwidth=0.95, relheight=0.9)
        self.place_search_frame()
        self.place_labels_frame()

    def on_create_specimen_req(self, patient_id):
        patient_data = dbCalls.get_patient_data(patient_id)
        if patient_data:
            self.main_screen.open_specimen_req(patient_data, patient_id)
        else:
            print(f"Error: No data found for patient_id: {patient_id}")

    # Creates the new patient row, put in a method for reusing in search
    def add_patient_row(self, patient, rowcount):
        temp_frame = customtkinter.CTkFrame(self.patient_frame, height=50, corner_radius=0, fg_color="#333333")
        customtkinter.CTkLabel(temp_frame, text=patient[2], font=self.patientFont, width=200).grid(column=0, row=0)
        customtkinter.CTkLabel(temp_frame, text=patient[3], font=self.patientFont, width=150).grid(column=1, row=0)
        customtkinter.CTkLabel(temp_frame, text=patient[4], font=self.patientFont, width=150).grid(column=2, row=0)
        customtkinter.CTkLabel(temp_frame, text=patient[1], font=self.patientFont, width=150).grid(column=3, row=0)
        customtkinter.CTkButton(temp_frame, text="Create", command=lambda p_id=patient[0]: self.on_create_specimen_req(p_id), font=self.patientFont, width=150).grid(column=4, row=0)
        temp_frame.grid(column=0,row=rowcount,sticky="ew", pady=5)
        temp_frame.grid_columnconfigure((0,1,2,3,4), weight=1)

    def build(self):
        self.main_screen.clear_frame()
        self.build_frames()
        self.place_frames()
        
        connection = sqlite3.connect('antibiotics.db')
        db = connection.cursor()

        patients = dbCalls.getAllPatients(db)

        for rowcount, patient in enumerate(patients, 1):
            self.add_patient_row(patient, rowcount)
        connection.close()
        self.patient_frame.grid_rowconfigure((0,1,2), weight=0, minsize=50 )
        self.patient_frame.grid_columnconfigure((0), weight=1, uniform="column")

# event=none because we dont need the event of pressing enter, just call this function
    def search(self, event=None):
        #Get the users input and remove all white space
        entry = self.search_bar.get().strip()
        #Clear the patient frame for new entries
        for widget in self.patient_frame.winfo_children():
            widget.destroy()

        #Place back the labels at the top of the frame
        self.build_labels_frame()
        self.place_labels_frame()

        #Search for their entry in the db
        connection = sqlite3.connect('antibiotics.db')
        db = connection.cursor()
        query = "SELECT * FROM patients WHERE name LIKE ? OR mrn LIKE ? OR dob LIKE ?"
        patients = db.execute(query, (f"%{entry}%", f"%{entry}%", f"%{entry}%")).fetchall()
        connection.close()

        #if anything was found, show that information. Otherwise, say nothing was found
        if patients:
            for rowcount, patient in enumerate(patients, 1):
                self.add_patient_row(patient, rowcount)
        else:
            customtkinter.CTkLabel(self.patient_frame, text="No results found", font=self.patientFont).grid(column=0, row=2, pady=10)

        #make sure the frame looks correct and you cannot scroll pass where patients are.
        self.patient_frame.grid_rowconfigure((0, 1, 2), weight=0, minsize=50)
        self.patient_frame.grid_columnconfigure((0), weight=1, uniform="column")