import customtkinter
import sqlite3
import dbCalls

class Culture_Notes:
    def __init__(self, main_screen, patientData=None):
        self.main_screen = main_screen
        self.right_dashboard = main_screen.right_dashboard

        self.mainFont = customtkinter.CTkFont(size=16)
        self.headerFont = customtkinter.CTkFont(size=18, weight="bold")
        self.current_user_id = main_screen.current_user_id

        self.current_patient_data = patientData
        print(self.current_patient_data)

    def build(self):
        self.main_screen.clear_frame()

        self.right_dashboard.grid_columnconfigure(0, weight=1)
        self.create_title()

        self.biochem_frame = customtkinter.CTkFrame(self.right_dashboard)
        self.biochem_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        for col in range(3):
            self.biochem_frame.grid_columnconfigure(col, weight=1)

        self.create_notes()
        self.create_buttons()

    def create_title(self):
        aFont = customtkinter.CTkFont(size=30, weight="bold")
        title_label = customtkinter.CTkLabel(self.right_dashboard, text="NMU Lab Microbiology Work Card Notes", font=aFont)
        title_label.grid(row=0, column=0, columnspan=2, pady=(10, 20), sticky="ew")

    def create_isolate_number(self):
        self.culture_frame = customtkinter.CTkFrame(self.biochem_frame)
        self.culture_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        customtkinter.CTkLabel(self.culture_frame, text="Isolate Number", font=self.headerFont).grid(row=0, column=0, sticky="w", padx=10)
        self.culture_entry = customtkinter.CTkTextbox(self.culture_frame, width=375, height=60)
        self.culture_entry.grid(row=1, column=0, padx=10, pady=10)

    def create_colony_desc(self):
        self.colony_frame = customtkinter.CTkFrame(self.biochem_frame)
        self.colony_frame.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        customtkinter.CTkLabel(self.colony_frame, text="Colony Description", font=self.headerFont).grid(row=0, column=0, sticky="w", padx=10)
        self.colony_entry = customtkinter.CTkTextbox(self.colony_frame, width=375, height=60)
        self.colony_entry.grid(row=1, column=0, padx=10, pady=10)

    def create_additional_notes(self):
        self.reactions_frame = customtkinter.CTkFrame(self.biochem_frame)
        self.reactions_frame.grid(row=0, column=2, padx=10, pady=10, sticky="ew")
        customtkinter.CTkLabel(self.reactions_frame, text="Additional Notes", font=self.headerFont).grid(row=0, column=0, sticky="w", padx=10)
        self.reactions_entry = customtkinter.CTkTextbox(self.reactions_frame, width=375, height=60)
        self.reactions_entry.grid(row=1, column=0, padx=10, pady=10)

    def create_notes(self):
        self.create_isolate_number()
        self.create_colony_desc()
        self.create_additional_notes()


        # Add 3 biochem tests
        for i in range(3):
            self.add_biochem_test(i)

        # add 3 simulated biochem tests
        for i in range(3):
            self.add_sim_biochem_test(i+3)
        
        # Configure columns and rows to take up space evenly
        self.biochem_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.biochem_frame.grid_rowconfigure((0, 1), weight=1)


    def add_biochem_test(self, test_number):
        # Calculate row and column based on the test count
        row, col = divmod(test_number, 3)

        # Frame for each biochem test, placed in a specific row and column
        test_frame = customtkinter.CTkFrame(self.biochem_frame)

        # Add input fields for the test within this test_frame
        customtkinter.CTkLabel(test_frame, text=f"Biochem Test {test_number + 1}", font=self.headerFont).grid(padx=5, row=0, column=0, columnspan=2, sticky="w")

        customtkinter.CTkLabel(test_frame, text="Test Name", font=self.mainFont).grid(padx=5, row=1, column=0, sticky="w")
        test_name_entry = customtkinter.CTkEntry(test_frame)
        test_name_entry.grid(row=1, column=1, padx=5, pady=5)

        customtkinter.CTkLabel(test_frame, text="Set Up Date", font=self.mainFont).grid(padx=5, row=2, column=0, sticky="w")
        set_up_date_entry = customtkinter.CTkEntry(test_frame)
        set_up_date_entry.grid(row=2, column=1, padx=5, pady=5)

        customtkinter.CTkLabel(test_frame, text="Set Up Time", font=self.mainFont).grid(padx=5, row=3, column=0, sticky="w")
        set_up_time_entry = customtkinter.CTkEntry(test_frame)
        set_up_time_entry.grid(row=3, column=1, padx=5, pady=5)

        #Tabs and spaces are there to align it correctly.
        customtkinter.CTkLabel(test_frame, text="Result\t\t       ", font=self.mainFont).grid(padx=5, row=4, column=0, sticky="w")
        results_entry = customtkinter.CTkEntry(test_frame)
        results_entry.grid(row=4, column=1, padx=5, pady=5)

        test_frame.grid_columnconfigure((0,1),weight=1)
        test_frame.grid_rowconfigure((0,1,2,3,4,5,6), weight=1)
        test_frame.grid(row=row + 1, column=col, padx=10, pady=5, sticky="nsew")  # Offset row by 1 for correct positioning

    def add_sim_biochem_test(self, test_number):
        # Calculate row and column based on the test count
        row, col = divmod(test_number, 3)

        # Frame for each biochem test, placed in a specific row and column
        test_frame = customtkinter.CTkFrame(self.biochem_frame)
        test_frame.grid(row=row + 1, column=col, padx=10, pady=5, sticky="nsew")  # Offset row by 1 for correct positioning

        # Add input fields for the test within this test_frame
        customtkinter.CTkLabel(test_frame, text=f"Simultated Biochem Test {test_number - 3 + 1}", font=self.headerFont).grid(padx=5, row=0, column=0, columnspan=2, sticky="w")

        customtkinter.CTkLabel(test_frame, text="Test Name", font=self.mainFont).grid(padx=5, row=1, column=0, sticky="w")
        test_name_entry = customtkinter.CTkEntry(test_frame)
        test_name_entry.grid(row=1, column=1, padx=5, pady=5)

        customtkinter.CTkLabel(test_frame, text="Inoculation", font=self.mainFont).grid(padx=5, row=2, column=0, sticky="w")
        inoculation_entry = customtkinter.CTkEntry(test_frame)
        inoculation_entry.grid(row=2, column=1, padx=5, pady=5)

        customtkinter.CTkLabel(test_frame, text="Temperature", font=self.mainFont).grid(padx=5, row=3, column=0, sticky="w")
        temperature_entry = customtkinter.CTkEntry(test_frame)
        temperature_entry.grid(row=3, column=1, padx=5, pady=5)

        customtkinter.CTkLabel(test_frame, text="Duration", font=self.mainFont).grid(padx=5, row=4, column=0, sticky="w")
        duration_entry = customtkinter.CTkEntry(test_frame)
        duration_entry.grid(row=4, column=1, padx=5, pady=5)

        customtkinter.CTkLabel(test_frame, text="Atmospheric Conditions", font=self.mainFont).grid(padx=5, row=5, column=0, sticky="w")
        conditions_entry = customtkinter.CTkEntry(test_frame)
        conditions_entry.grid(row=5, column=1, padx=5, pady=5)

        customtkinter.CTkLabel(test_frame, text="Result", font=self.mainFont).grid(padx=5, row=6, column=0, sticky="w")
        conditions_entry = customtkinter.CTkEntry(test_frame)
        conditions_entry.grid(row=6, column=1, padx=5, pady=5)

        test_frame.grid_columnconfigure((0,1),weight=1)
        test_frame.grid_rowconfigure((0,1,2,3,4,5,6), weight=1)


    def create_buttons(self):
        button_frame = customtkinter.CTkFrame(self.biochem_frame)
        button_frame.grid(row=3, column=0, columnspan=3, padx=10, pady=20, sticky="ew")

        # Configure middle columns to take up the extra space
        for col in range(2, 6):
            button_frame.grid_columnconfigure(col, weight=1)
        
        cancel_button = customtkinter.CTkButton(button_frame, text="Cancel", command=self.cancel)
        cancel_button.grid(row=0, column=6, padx=5, pady=5, sticky="e")

        save_button = customtkinter.CTkButton(button_frame, text="Save", command=self.save)
        save_button.grid(row=0, column=7, padx=10, pady=5, sticky="e")


    def cancel(self):
        self.main_screen.clear_frame()
        self.main_screen.open_work_card(self.current_patient_data)

    def save(self):
        try:
            isolate_number = self.culture_entry.get("1.0", "end").strip()
            colony_desc = self.colony_entry.get("1.0", "end").strip()
            biochem_reactions = self.reactions_entry.get("1.0", "end").strip()

            biochem_tests = []

            for i in range(3):
                test_frame = self.biochem_frame.grid_slaves(row=i // 3 + 1, column=i % 3)[0]
                test_name = test_frame.grid_slaves(row=1, column=1)[0].get().strip()
                set_up_date = test_frame.grid_slaves(row=2, column=1)[0].get().strip()
                set_up_time = test_frame.grid_slaves(row=3, column=1)[0].get().strip()
                results = test_frame.grid_slaves(row=4, column=1)[0].get().strip()
                biochem_tests.append((test_name, set_up_date, set_up_time, results))

            for i in range(6,3):
                test_frame = self.biochem_frame.grid_slaves(row=i // 3 + 1, column=i % 3)[0]
                test_name = test_frame.grid_slaves(row=1, column=1)[0].get().strip()
                inoculation = test_frame.grid_slaves(row=2, column=1)[0].get().strip()
                temperature = test_frame.grid_slaves(row=3, column=1)[0].get().strip()
                duration = test_frame.grid_slaves(row=4, column=1)[0].get().strip()
                atmospheric_conditions = test_frame.grid_slaves(row=5, column=1)[0].get().strip()
                biochem_tests.append((test_name, inoculation, temperature, duration, atmospheric_conditions))

            connection = sqlite3.connect("antibiotics.db")
            cursor = connection.cursor()
            patientId = dbCalls.get_patient_id_by_mrn(self.current_patient_data[2])
            userPatientId = dbCalls.get_user_patient_id(self, patientId)

            query = '''
                INSERT INTO CultureNotes (
                    userPatientId, isolateNumber, colonyDescription, additionalNotes,
                    test1Name, test1SetUpDate, test1SetUpTime, test1Results,                  
                    test2Name, test2SetUpDate, test2SetUpTime, test2Results,
                    test3Name, test3SetUpDate, test3SetUpTime, test3Results,
                    test4Name, test4Inoculation, test4Temperature, test4Duration, test4AtmosphericConditions,
                    test5Name, test5Inoculation, test5Temperature, test5Duration, test5AtmosphericConditions,
                    test6Name, test6Inoculation, test6Temperature, test6Duration, test6AtmosphericConditions
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(userPatientId) DO UPDATE SET
                    isolateNumber = excluded.isolateNumber,
                    colonyDescription = excluded.colonyDescription,
                    additionalNotes = excluded.additionalNotes,

                    test1Name = excluded.test1Name, test1SetUpDate = excluded.test1SetUpDate,
                    test1SetUpTime = excluded.test1SetUpTime, test1Results = excluded.test1Results,

                    test2Name = excluded.test2Name, test2SetUpDate = excluded.test2SetUpDate,
                    test2SetUpTime = excluded.test2SetUpTime, test2Results = excluded.test2Results,

                    test3Name = excluded.test3Name, test3SetUpDate = excluded.test3SetUpDate,
                    test3SetUpTime = excluded.test3SetUpTime, test3Results = excluded.test3Results,

                    test4Name = excluded.test4Name, test4Inoculation = excluded.test4Inoculation,
                    test4Temperature = excluded.test4Temperature, test4Duration = excluded.test4Duration,
                    test4AtmosphericConditions = excluded.test4AtmosphericConditions,

                    test5Name = excluded.test5Name, test5Inoculation = excluded.test5Inoculation,
                    test5Temperature = excluded.test5Temperature, test5Duration = excluded.test5Duration,
                    test5AtmosphericConditions = excluded.test5AtmosphericConditions,

                    test6Name = excluded.test6Name, test6Inoculation = excluded.test6Inoculation,
                    test6Temperature = excluded.test6Temperature, test6Duration = excluded.test6Duration,
                    test6AtmosphericConditions = excluded.test6AtmosphericConditions
            '''

            # Flatten biochem_tests data and insert into database
            cursor.execute(query, (userPatientId, isolate_number, colony_desc, biochem_reactions, *[item for test in biochem_tests for item in test]))

            # Commit and close
            connection.commit()
            print("Culture Notes data upserted successfully.")
            self.main_screen.clear_frame()
            self.main_screen.open_work_card(self.current_patient_data)

        except Exception as e:
            print(f"Error in save: {e}")
        finally:
            if connection:
                connection.close()


    def populate_form(self, userPatientID):
        try:
            connection = sqlite3.connect("antibiotics.db")
            cursor = connection.cursor()

            # Query data for the current user
            query = '''
                SELECT *
                FROM CultureNotes
                WHERE userPatientId = ?
            '''
            cursor.execute(query, (userPatientID,))
            record = cursor.fetchone()

            if not record:
                print("No data found for the current user.")
                return

            # Map database columns to record values
            column_names = [
                "noteId", "userPatientId", "isolateNumber", "colonyDescription", "additionalNotes",
                "test1Name", "test1SetUpDate", "test1SetUpTime", "test1Results",
                "test2Name", "test2SetUpDate", "test2SetUpTime", "test2Results",
                "test3Name", "test3SetUpDate", "test3SetUpTime", "test3Results",
                "test4Name", "test4Inoculation", "test4Temperature", "test4Duration", "test4AtmosphericConditions",
                "test5Name", "test5Inoculation", "test5Temperature", "test5Duration", "test5AtmosphericConditions",
                "test6Name", "test6Inoculation", "test6Temperature", "test6Duration", "test6AtmosphericConditions"
            ]
            culture_notes_data = dict(zip(column_names, record))

            # Populate Isolate Number, Colony Description, and Additional Notes
            self.culture_entry.delete("1.0", "end")
            self.culture_entry.insert("1.0", culture_notes_data.get("isolateNumber", ""))

            self.colony_entry.delete("1.0", "end")
            self.colony_entry.insert("1.0", culture_notes_data.get("colonyDescription", ""))

            self.reactions_entry.delete("1.0", "end")
            self.reactions_entry.insert("1.0", culture_notes_data.get("additionalNotes", ""))

            # Populate Biochemical Test fields
            for i in range(6):
                # Calculate the row and column for the test frame
                row, col = divmod(i, 3)
                test_frame = self.biochem_frame.grid_slaves(row=row + 1, column=col)[0]

                # Get corresponding field names from the database
                test_fields = {
                    1: f"test{i+1}Name",
                    2: f"test{i+1}Inoculation",
                    3: f"test{i+1}Temperature",
                    4: f"test{i+1}Duration",
                    5: f"test{i+1}AtmosphericConditions",
                }

                # Populate each field in the test frame
                for j, db_column in test_fields.items():
                    widget = test_frame.grid_slaves(row=j, column=1)[0]  # Accessing the second column in the frame
                    if widget and isinstance(widget, customtkinter.CTkEntry):
                        widget.delete(0, "end")
                        widget.insert(0, culture_notes_data.get(db_column, ""))

            print("Form populated successfully with Culture Notes data.")

        except Exception as e:
            print(f"Error in populate_form for Culture Notes: {e}")

        finally:
            if connection:
                connection.close()
