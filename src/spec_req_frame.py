import customtkinter
import sqlite3
import dbCalls

class Specimen_Requisition:
    def __init__(self, main_screen, patient_id=None):
        self.patient_id = patient_id
        self.main_screen = main_screen
        self.right_dashboard = main_screen.right_dashboard
        self.current_user_id = main_screen.current_user_id
        self.mainFont = customtkinter.CTkFont(size=16)
        self.headerFont = customtkinter.CTkFont(size=18, weight="bold")

    def build_left_labels(self):
        self.patient_info_label = customtkinter.CTkLabel(self.left_spec_frame, text="Patient Information", font=self.headerFont, text_color="#FFFFFF")
        self.patient_info_label.grid(column=0, row=0, padx=10, pady=(10, 20), columnspan=2, sticky="w")

        labels = ["Name:", "Date of Birth:", "Medical Record Number:", "Sex:", "Ordering Provider:", "Diagnosis:", "Collection Date:", "Collection Time:", "Specimen Source/Type:", "Tests Ordered:", "Is Patient Receiving Therapy?"]
        for i, label_text in enumerate(labels):
            label = customtkinter.CTkLabel(self.left_spec_frame, text=label_text, font=self.mainFont, text_color="#FFFFFF")
            label.grid(column=0, row=i+1, sticky="w", padx=10, pady=5)

    def build_left_entries(self):
        non_editable_labels = [
            {"label": "First Last", "row": 1},
            {"label": "MM/DD/YYYY", "row": 2},
            {"label": "******", "row": 3},
            {"label": "Male / Female", "row": 4}
        ]

        for item in non_editable_labels:
            value_label = customtkinter.CTkLabel(self.left_spec_frame, text=item["label"], font=self.mainFont, text_color="#FFFFFF", anchor="w")
            value_label.grid(column=1, row=item["row"], padx=10, pady=5, sticky="w")

        placeholders = [
            "Dr. ...", "Check up, ...", "MM/DD/YYYY", "Military time",
            "Urine, sputum, ...", "Urine culture, ...", "Yes / No"
        ]

        for i, placeholder in enumerate(placeholders, start=5):
            entry = customtkinter.CTkEntry(self.left_spec_frame, placeholder_text=placeholder, font=self.mainFont, width=250)
            entry.grid(column=1, row=i, padx=10, pady=5)


    def build_right_labels(self):
        self.lab_only_label = customtkinter.CTkLabel(self.right_spec_frame, text="Laboratory Staff Only", font=self.headerFont, text_color="#FFFFFF")
        self.lab_only_label.grid(column=0, row=0, padx=10, pady=(10, 20), columnspan=2, sticky="w")

        labels = ["Time Received in Lab:", "Is the Specimen Acceptable?"]
        for i, label_text in enumerate(labels):
            label = customtkinter.CTkLabel(self.right_spec_frame, text=label_text, font=self.mainFont, text_color="#FFFFFF")
            label.grid(column=0, row=i+1, sticky="w", padx=10, pady=5)

    def build_right_entries(self):
        placeholders = ["Military time", "Yes / No"]
        for i, placeholder in enumerate(placeholders):
            entry = customtkinter.CTkEntry(self.right_spec_frame, placeholder_text=placeholder, font=self.mainFont, width=250)
            entry.grid(column=1, row=i+1, padx=10, pady=5)

        self.right_spec_frame.grid_rowconfigure(len(placeholders)+3, weight=1)

        self.cancel_button = customtkinter.CTkButton(self.right_spec_frame, text="Cancel", font=self.mainFont, command=self.cancel_action)
        self.cancel_button.grid(column=0, row=len(placeholders)+20, padx=10, pady=20)

        self.submit_button = customtkinter.CTkButton(self.right_spec_frame, text="Submit", font=self.mainFont, command=self.submit_action)
        self.submit_button.grid(column=1, row=len(placeholders)+20, padx=10, pady=20)

    def build_frames(self):
        self.left_spec_frame = customtkinter.CTkFrame(self.right_dashboard, fg_color="#2b2b2b")
        self.left_spec_frame.place(relx=0.05, rely=0.1, relwidth=0.43, relheight=0.8)

        self.right_spec_frame = customtkinter.CTkFrame(self.right_dashboard, fg_color="#2b2b2b")
        self.right_spec_frame.place(relx=0.52, rely=0.1, relwidth=0.43, relheight=0.8)

        self.build_left_labels()
        self.build_left_entries()
        self.build_right_labels()
        self.build_right_entries()

        for i in range(20):
            self.left_spec_frame.grid_rowconfigure(i, weight=1)
            self.right_spec_frame.grid_rowconfigure(i, weight=1)
        self.left_spec_frame.grid_columnconfigure((0, 1), weight=1)
        self.right_spec_frame.grid_columnconfigure((0, 1), weight=1)

    def build(self):
        self.main_screen.clear_frame()

        self.spec_req_label = customtkinter.CTkLabel(self.right_dashboard, text="Specimen Requisition", font=customtkinter.CTkFont(size=30, weight="bold"), text_color="#FFFFFF")
        self.spec_req_label.pack(pady=30)

        self.build_frames()

    def cancel_action(self):
        self.main_screen.clear_frame()
        self.main_screen.lookup()
        print("Cancelled. Returning to previous screen.")

    def submit_action(self):
        connection = None
        try:
            # Gather data
            provider = self.left_spec_frame.grid_slaves(row=5, column=1)[0].get()
            diagnosis = self.left_spec_frame.grid_slaves(row=6, column=1)[0].get()
            collection_date = self.left_spec_frame.grid_slaves(row=7, column=1)[0].get()
            collection_time = self.left_spec_frame.grid_slaves(row=8, column=1)[0].get()
            specimen_type = self.left_spec_frame.grid_slaves(row=9, column=1)[0].get()
            test_ordered = self.left_spec_frame.grid_slaves(row=10, column=1)[0].get()
            receiving_therapy = self.left_spec_frame.grid_slaves(row=11, column=1)[0].get().lower() == "yes"
            received_in_lab = self.right_spec_frame.grid_slaves(row=1, column=1)[0].get()
            specimen_acceptable = self.right_spec_frame.grid_slaves(row=2, column=1)[0].get().lower() == "yes"

            # Database connection
            connection = sqlite3.connect('antibiotics.db')
            cursor = connection.cursor()

            # Get userPatientId
            user_patient_id = dbCalls.get_user_patient_id(self)

            # Upsert logic for SpecimenRequisition
            cursor.execute('''
                INSERT INTO SpecimenRequisition (
                    userPatientId, provider, diagnosis, collectionDate, collectionTime,
                    specimenType, testOrdered, receivingTherapy, receivedInLab, specimenAcceptable
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(userPatientId) DO UPDATE SET
                    provider = excluded.provider,
                    diagnosis = excluded.diagnosis,
                    collectionDate = excluded.collectionDate,
                    collectionTime = excluded.collectionTime,
                    specimenType = excluded.specimenType,
                    testOrdered = excluded.testOrdered,
                    receivingTherapy = excluded.receivingTherapy,
                    receivedInLab = excluded.receivedInLab,
                    specimenAcceptable = excluded.specimenAcceptable
            ''', (
                user_patient_id, provider, diagnosis, collection_date, collection_time, 
                specimen_type, test_ordered, receiving_therapy, received_in_lab, specimen_acceptable
            ))

            # Commit and close
            connection.commit()
            print("Specimen requisition data upserted successfully.")
            self.main_screen.clear_frame()
            self.main_screen.lookup()

        except Exception as e:
            print(f"Error in submit_action: {e}")
        finally:
            if connection:
                connection.close()



    def populate_form(self, patient_data):
        if patient_data:
            non_editable_fields = [1, 2, 3, 4]
            for i, value in enumerate(patient_data[:4]):
                label_widget = self.left_spec_frame.grid_slaves(row=non_editable_fields[i], column=1)
                if label_widget:
                    label_widget[0].configure(text=str(value) if value else "")

            connection = sqlite3.connect('antibiotics.db')
            cursor = connection.cursor()

            # Fetch data from SpecimenRequisition
            cursor.execute('''
                SELECT provider, diagnosis, collectionDate, collectionTime, specimenType, testOrdered,
                    receivingTherapy, receivedInLab, specimenAcceptable
                FROM SpecimenRequisition
                JOIN UserPatients ON SpecimenRequisition.userPatientId = UserPatients.userPatientId
                WHERE UserPatients.patientId = ? AND UserPatients.userId = ?
            ''', (self.patient_id, self.current_user_id))

            specimen_data = cursor.fetchone()
            connection.close()

            if specimen_data:
                print("Specimen requisition data fetched:", specimen_data)
                for i, value in enumerate(specimen_data, start=5):
                    if value == 0:
                        value = "No"
                    if value == 1:
                        value = "Yes"
                    entry_widget = self.left_spec_frame.grid_slaves(row=i, column=1)
                    if entry_widget:
                        entry_widget[0].delete(0, 'end')
                        entry_widget[0].insert(0, str(value) if value else "")
            else:
                print("No specimen requisition data found for this patient.")






