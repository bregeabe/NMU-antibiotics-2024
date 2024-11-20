import customtkinter
import sqlite3
import dbCalls

class PatientLookUpFrame:
    def __init__(self, main_screen):
        self.main_screen = main_screen
        self.right_dashboard = self.main_screen.right_dashboard
        self.current_user = main_screen.current_user_id


        self.patientFont = customtkinter.CTkFont(size=16)

    def build_search_frame(self):
        self.main_screen.search_frame = customtkinter.CTkFrame(self.main_screen.patient_frame, corner_radius=0, height=50, fg_color="#232323")
        self.main_screen.result_label = customtkinter.CTkLabel(self.main_screen.search_frame, text="Search Results", font=customtkinter.CTkFont(size=22, weight="bold"))
        self.main_screen.search_button = customtkinter.CTkButton(self.main_screen.search_frame, text="Search", width=200)
        self.main_screen.search_bar = customtkinter.CTkEntry(self.main_screen.search_frame, placeholder_text="Search...", width=200)

    def build_labels_frame(self):
        aFont = customtkinter.CTkFont(size=18)
        self.main_screen.labels_frame = customtkinter.CTkFrame(self.main_screen.patient_frame, height=50, corner_radius=0, fg_color="#333333")
        self.main_screen.name_label = customtkinter.CTkLabel(self.main_screen.labels_frame, text="Name", font=aFont, width=200)
        self.main_screen.dob_label = customtkinter.CTkLabel(self.main_screen.labels_frame, text="DOB", font=aFont, width=150)
        self.main_screen.sex_label = customtkinter.CTkLabel(self.main_screen.labels_frame, text="Sex", font=aFont, width=150)
        self.main_screen.mrn_label = customtkinter.CTkLabel(self.main_screen.labels_frame, text="MRN", font=aFont, width=150)
        self.main_screen.spec_req_label = customtkinter.CTkLabel(self.main_screen.labels_frame, text="Specimen Req", font=aFont, width=150)
        self.main_screen.work_card_label = customtkinter.CTkLabel(self.main_screen.labels_frame, text="Work Card", font=aFont, width=150)

    def place_search_frame(self):
        self.main_screen.search_frame.grid(column=0, row=0, sticky="ew")
        self.main_screen.result_label.pack(pady=10, padx=15, side='left')
        self.main_screen.search_button.pack(pady=10, padx=15, side='right')
        self.main_screen.search_bar.pack(pady=10, padx=15, side='right')

    def place_labels_frame(self):
        self.main_screen.labels_frame.grid(row=1, column=0, sticky="ew")
        self.main_screen.name_label.grid(row=0,column=0)
        self.main_screen.dob_label.grid(row=0,column=1)
        self.main_screen.sex_label.grid(row=0,column=2)
        self.main_screen.mrn_label.grid(row=0,column=3)
        self.main_screen.spec_req_label.grid(row=0,column=4)
        self.main_screen.work_card_label.grid(row=0,column=5)

        self.main_screen.labels_frame.grid_columnconfigure((0,1,2,3,4,5), weight=1)
        self.main_screen.labels_frame.grid_rowconfigure((0), weight=1)

    def on_create_specimen_req(self, patient_id):
        patient_data = dbCalls.get_patient_data(patient_id)  # Fetch patient data
        if patient_data:
            self.main_screen.open_specimen_req(patient_data, patient_id)  # Open Specimen Requisition frame
        else:
            print(f"No patient data found for patient_id: {patient_id}")

    def build_frames(self):
        self.main_screen.lookup_label = customtkinter.CTkLabel(self.main_screen.right_dashboard, text="Patients", font=customtkinter.CTkFont(size=30, weight="bold"))

        self.main_screen.patient_frame = customtkinter.CTkScrollableFrame(self.main_screen.right_dashboard, corner_radius=10, fg_color="#333333")

        self.build_search_frame()

        self.build_labels_frame()

    def place_frames(self):
        self.main_screen.lookup_label.pack(pady=30)
        self.main_screen.patient_frame.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.8)

        self.place_search_frame()

        self.place_labels_frame()

    def get_work_card(self, patient_id):
        patient_data = dbCalls.get_patient_data(patient_id)
        if patient_data:
            self.main_screen.open_work_card(patient_data, patient_id)
        else:
            print(f"No patient data found for patient_id: {patient_id}")


    def build(self):
        self.main_screen.clear_frame()

        self.build_frames()
        self.place_frames()

        connection = sqlite3.connect('antibiotics.db')
        db = connection.cursor()
        # patients = dbCalls.getPatientAndSpecimenDataByUserID(self.current_user)
        db.execute('''
            SELECT Patients.name, Patients.dob, Patients.mrn, Patients.gender,
                Specimens.collectionDate, Specimens.collectionTime, Specimens.diagnosis, Patients.patientId
            FROM PatientSpecimens
            JOIN UserPatients ON PatientSpecimens.userPatientId = UserPatients.userPatientId
            JOIN Patients ON UserPatients.patientId = Patients.patientId
            JOIN Specimens ON PatientSpecimens.specimenId = Specimens.specimenId
            WHERE UserPatients.userId = ?
        ''', (self.current_user,))
        patients = db.fetchall()
        rowcount = 2
        for patient in patients:
            temp_frame = customtkinter.CTkFrame(self.main_screen.patient_frame, fg_color="#333333", height=50, corner_radius=0)
            customtkinter.CTkLabel(temp_frame, text=patient[0], font=self.patientFont, width=200).grid(column=0, row=0)  # Name
            customtkinter.CTkLabel(temp_frame, text=patient[1], font=self.patientFont, width=160).grid(column=1, row=0)  # DOB
            customtkinter.CTkLabel(temp_frame, text=patient[2], font=self.patientFont, width=150).grid(column=2, row=0)  # MRN
            customtkinter.CTkLabel(temp_frame, text=patient[3], font=self.patientFont, width=160).grid(column=3, row=0)  # Gender

            customtkinter.CTkButton(
                temp_frame,
                text="Specimen Req",
                command=lambda p_id=patient[7]: self.on_create_specimen_req(p_id),
                font=self.patientFont,
                width=150
            ).grid(column=4, row=0)

            customtkinter.CTkButton(
                temp_frame,
                text="Work Card",
                command=lambda p_id=patient[7]: self.get_work_card(p_id),  # Pass the patient_id
                font=self.patientFont,
                width=150
            ).grid(column=5, row=0)

            temp_frame.grid(column=0, row=rowcount, sticky="ew", pady=5)
            temp_frame.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
            temp_frame.grid_rowconfigure(0, weight=1)
            rowcount += 1

        connection.close()

        self.main_screen.patient_frame.grid_rowconfigure((0, 1, 2), weight=0, minsize=50)
        self.main_screen.patient_frame.grid_columnconfigure(0, weight=1, uniform="column")