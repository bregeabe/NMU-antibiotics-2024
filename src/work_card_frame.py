import customtkinter
from culture_notes import Culture_Notes
import sqlite3
import dbCalls

class Work_Card_Frame:
    def __init__(self, main_screen):
        self.main_screen = main_screen
        self.right_dashboard = main_screen.right_dashboard

        self.mainFont = customtkinter.CTkFont(size=16)
        self.headerFont = customtkinter.CTkFont(size=18, weight="bold")

        self.notes = Culture_Notes(main_screen)
        self.current_user = main_screen.current_user_id
        self.placeholders = {}


    def build(self):
        self.main_screen.clear_frame()

        self.right_dashboard.grid_columnconfigure(0, weight=1)

        # Build each section of the work card
        self.create_title()
        self.create_prefilled_section()
        self.create_non_prefilled_section()


    def create_title(self):
        aFont = customtkinter.CTkFont(size=30, weight="bold")
        title_label = customtkinter.CTkLabel(self.right_dashboard, text="NMU Lab Microbiology Work Card", font=aFont)
        title_label.grid(row=0, column=0, columnspan=2, pady=(10, 20), sticky="ew")


    def create_prefilled_section(self):
        prefilled_frame = customtkinter.CTkFrame(self.right_dashboard)
        prefilled_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")

        for col in range(4):
            prefilled_frame.grid_columnconfigure(col, weight=1)

        fields = [
            ("Patient Name", ""),
            ("Patient DOB", ""),
            ("MRN", ""),
            ("Sex", ""),
            ("Date Collected", "mm/dd/yy"),
            ("Time Collected", "HH:MM"),
            ("Specimen Diagnosis", ""),
            ("Patient Doctor", ""),
        ]

        prefilled_frame.grid_rowconfigure(0, minsize=10)
        prefilled_frame.grid_rowconfigure(100, minsize=10)

        for i, (label, placeholder) in enumerate(fields):
            row, col = divmod(i, 4)
            field_label = customtkinter.CTkLabel(prefilled_frame, text=label, font=self.mainFont)
            field_label.grid(row=row * 2, column=col, padx=(10, 5), pady=2, sticky="w")

            field_entry = customtkinter.CTkEntry(prefilled_frame, placeholder_text=placeholder)
            field_entry.grid(row=row * 2 + 1, column=col, padx=(5, 10), pady=2, sticky="ew")
            
            # Store the entry in placeholders
            self.placeholders[label] = field_entry


    def create_non_prefilled_section(self):
        non_prefilled_frame = customtkinter.CTkFrame(self.right_dashboard)
        non_prefilled_frame.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")
        non_prefilled_frame.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)

        self.create_culture_id(non_prefilled_frame)
        self.create_priority(non_prefilled_frame)
        self.create_direct_gram_stain(non_prefilled_frame)
        self.create_culture_readout(non_prefilled_frame)

        self.create_button_section(non_prefilled_frame)

    def create_culture_id(self, aFrame):
        culture_id_label = customtkinter.CTkLabel(aFrame, text="Culture ID:", font=self.mainFont)
        culture_id_label.grid(row=0, column=0, padx=(10, 5), pady=5, sticky="w")

        culture_id_entry = customtkinter.CTkEntry(aFrame, placeholder_text="1-20")
        culture_id_entry.grid(row=0, column=1, padx=(5, 10), pady=5, sticky="ew")
        self.placeholders["Culture ID"] = culture_id_entry

    def create_priority(self, aFrame):
        priority_label = customtkinter.CTkLabel(aFrame, text="Priority:", font=self.mainFont)
        priority_label.grid(row=0, column=2, padx=(10, 5), pady=5, sticky="w")

        priority_entry = customtkinter.CTkOptionMenu(aFrame, values=["STAT", "ROUTINE"])
        priority_entry.grid(row=0, column=3, padx=(5, 10), pady=5, sticky="ew")
        self.placeholders["Priority"] = priority_entry

    def create_direct_gram_stain(self, aFrame):
        gram_stain_frame = customtkinter.CTkFrame(aFrame)
        gram_stain_frame.grid(row=1, column=0, columnspan=8, padx=10, pady=10, sticky="ew")

        gram_stain_label = customtkinter.CTkLabel(gram_stain_frame, text="Direct Gram Stain: ", font=self.mainFont)
        gram_stain_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="w")

        gram_stain_options = ["WBC", "EPI", "GPC", "GPB", "GNC", "GNB", "Other"]

        for col in range(len(gram_stain_options) * 2):  # Multiply by 2 for label-entry pairs
            gram_stain_frame.grid_columnconfigure(col, weight=1, uniform="stain")

        for i, option in enumerate(gram_stain_options):
            label = customtkinter.CTkLabel(gram_stain_frame, text=option, font=self.mainFont)
            label.grid(row=0, column=(i * 2)+1, padx=(5, 2), pady=2, sticky="e")

            entry = customtkinter.CTkEntry(gram_stain_frame, width=40, placeholder_text="Qty")
            entry.grid(row=0, column=(i * 2) + 2, padx=(2, 10), pady=2, sticky="w")
            self.placeholders[option] = entry  # Add to placeholders


    def create_date_and_time(self, culture_readout_frame, i):
        date_label = customtkinter.CTkLabel(culture_readout_frame, text="Date:", font=self.mainFont)
        date_label.grid(row=i + 1, columnspan=1, column=4, padx=(5, 10), pady=10, sticky="ew")

        date_entry = customtkinter.CTkEntry(culture_readout_frame)
        date_entry.grid(row=i + 1, columnspan=1, column=5, padx=(10, 5), pady=10, sticky="ew")
        self.placeholders[f"day{i+1}Date"] = date_entry


        time_label = customtkinter.CTkLabel(culture_readout_frame, text="Time:", font=self.mainFont)
        time_label.grid(row=i + 1, columnspan=1, column=6, padx=(5, 10), pady=10, sticky="ew")

        time_entry = customtkinter.CTkEntry(culture_readout_frame)
        time_entry.grid(row=i + 1, columnspan=1, column=7, padx=(10, 5), pady=10, sticky="ew")
        self.placeholders[f"day{i+1}Time"] = time_entry

    def create_culture_readout(self, aFrame):
        culture_readout_frame = customtkinter.CTkFrame(aFrame)
        culture_readout_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        culture_readout_label = customtkinter.CTkLabel(culture_readout_frame, text="Culture Readout", font=self.headerFont)
        culture_readout_label.grid(row=0, column=0, columnspan=2, padx=25, pady=10, sticky="w")

        for col in range(12):
            culture_readout_frame.grid_columnconfigure(col, weight=1)

        for i in range(5):
            day_label = customtkinter.CTkLabel(culture_readout_frame, text=f"Day {i+1}:", font=self.mainFont)
            day_label.grid(row=i + 1, column=0, padx=(10, 5), pady=10, sticky="e")

            day_entry = customtkinter.CTkEntry(culture_readout_frame, placeholder_text=f"Observations for Day {i+1}")
            day_entry.grid(row=i + 1, columnspan=3, column=1, padx=(5, 10), pady=10, sticky="ew")
            self.placeholders[f"day{i+1}Observation"] = day_entry  # Add to placeholders

            self.create_date_and_time(culture_readout_frame, i)

        final_label = customtkinter.CTkLabel(culture_readout_frame, text="Final: ", font=self.mainFont)
        final_label.grid(row=6, column=0, padx=(10, 5), pady=10, sticky="e")

        final_entry = customtkinter.CTkEntry(culture_readout_frame, placeholder_text="Final observations")
        final_entry.grid(row=6, columnspan=3, column=1, padx=(5, 10), pady=10, sticky="ew")
        self.placeholders["finalObservation"] = final_entry


        self.create_date_and_time(culture_readout_frame, 5)

        critical_results_frame = customtkinter.CTkFrame(aFrame)
        critical_results_frame.grid(row=2, column=4, columnspan=4, padx=10, pady=10, sticky="nsew")
        critical_results_frame.grid_columnconfigure(0, weight=1)  # Make sure the column expands
        critical_results_frame.grid_rowconfigure(1, weight=1)  # Ensure row expands vertically

        critical_results_label = customtkinter.CTkLabel(critical_results_frame, text="Critical Results", font=self.headerFont)
        critical_results_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        critical_results_entry = customtkinter.CTkTextbox(critical_results_frame, height=60)
        critical_results_entry.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
        self.placeholders["critical_results"] = critical_results_entry  # Add to placeholders


    def get_gram_stain_value(self, option):
        gram_stain_values = {
            "WBC": self.placeholders.get("WBC"),
            "EPI": self.placeholders.get("EPI"),
            "GPC": self.placeholders.get("GPC"),
            "GPB": self.placeholders.get("GPB"),
            "GNC": self.placeholders.get("GNC"),
            "GNB": self.placeholders.get("GNB"),
            "Other": self.placeholders.get("Other")
        }
        return gram_stain_values.get(option, None).get() if gram_stain_values.get(option) else None

    def get_date_and_time(self, day_number):
        date_key = f"day{day_number}Date"
        time_key = f"day{day_number}Time"

        date_entry = self.placeholders.get(date_key)
        time_entry = self.placeholders.get(time_key)

        date_value = date_entry.get() if date_entry else None
        time_value = time_entry.get() if time_entry else None

        return date_value, time_value
    
    def get_day_observations(self, day_number):
        day_key = f"day{day_number}Observations"
        day_entry = self.placeholders.get(day_key)
        return day_entry.get() if day_entry else None

    def get_final_observations(self):
        final_entry = self.placeholders.get("final_observations")
        return final_entry.get() if final_entry else None

    def get_critical_results(self):
        critical_results_entry = self.placeholders.get("critical_results")
        return critical_results_entry.get() if critical_results_entry else None

    def go_to_culture_notes(self):
        # Fetch full patient data (8 fields) before navigating to Culture Notes
        patient_data = dbCalls.get_patient_data(self.current_user)  # Use current_user ID to fetch
        if patient_data:
            self.main_screen.patient_data = patient_data  # Save patient data globally in main_screen
            self.main_screen.open_culture_notes()
        else:
            print("Unable to fetch patient data for Culture Notes.")


    def create_button_section(self, non_prefilled_frame):

        button_frame = customtkinter.CTkFrame(non_prefilled_frame)
        button_frame.grid(row=4, column=0, columnspan=8, padx=10, pady=10, sticky="ew")

        # Configure middle columns to take up the extra space
        for col in range(2, 6):
            button_frame.grid_columnconfigure(col, weight=1)

        culture_notes_button = customtkinter.CTkButton(
            button_frame,
            text="Culture Notes and Tests",
            command=self.go_to_culture_notes
        )
        culture_notes_button.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        cancel_button = customtkinter.CTkButton(button_frame, text="Cancel", command=self.cancel)
        cancel_button.grid(row=0, column=6, padx=5, pady=5, sticky="e")

        save_button = customtkinter.CTkButton(button_frame, text="Save", command=self.save)
        save_button.grid(row=0, column=7, padx=5, pady=5, sticky="e")

    def cancel(self):
        self.main_screen.clear_frame()
        self.main_screen.lookup()

    def save(self):
        connection = None
        try:
            data = {}
            patientData = {
                "patientName": self.placeholders["Patient Name"].get().strip(),
                "patientDob": self.placeholders["Patient DOB"].get().strip(),
                "mrn": self.placeholders["MRN"].get().strip(),
                "gender": self.placeholders["Sex"].get().strip(),
                "dateCollected": self.placeholders["Date Collected"].get().strip(),
                "timeCollected": self.placeholders["Time Collected"].get().strip(),
                "specimenDiagnosis": self.placeholders["Specimen Diagnosis"].get().strip(),
                "provider": self.placeholders["Patient Doctor"].get().strip()
            }
            data["userPatientId"] = self.current_user
            data["cultureId"] = self.placeholders["Culture ID"].get().strip()
            data["priority"] = self.placeholders["Priority"].get().strip()

            gram_stain_options = ["WBC", "EPI", "GPC", "GPB", "GNC", "GNB", "Other"]
            for option in gram_stain_options:
                entry_widget = self.placeholders.get(option)
                if entry_widget:
                    data[f"{option.lower()}Qty"] = entry_widget.get().strip()
                else:
                    data[f"{option.lower()}Qty"] = ""

            for i in range(1, 6):
                data[f"day{i}Observation"] = self.placeholders[f"day{i}Observation"].get().strip()
                data[f"day{i}Date"] = self.placeholders[f"day{i}Date"].get().strip()
                data[f"day{i}Time"] = self.placeholders[f"day{i}Time"].get().strip()

            data["finalObservation"] = self.placeholders["finalObservation"].get().strip()
            data["finalDate"] = self.placeholders["day6Date"].get().strip()
            data["finalTime"] = self.placeholders["day6Time"].get().strip()

            critical_results_widget = self.placeholders.get("critical_results")
            if critical_results_widget:
                data["criticalResults"] = critical_results_widget.get("1.0", "end").strip()
            else:
                data["criticalResults"] = ""

            connection = sqlite3.connect("antibiotics.db")
            cursor = connection.cursor()

            columns = ", ".join(data.keys())
            placeholders = ", ".join(["?"] * len(data))
            updates = ", ".join([f"{col} = excluded.{col}" for col in data.keys()])

            query = f'''
                INSERT INTO WorkCard ({columns})
                VALUES ({placeholders})
                ON CONFLICT(userPatientId) DO UPDATE SET
                {updates}
            '''
            cursor.execute(query, tuple(data.values()))

            connection.commit()
            print("Work Card data saved successfully.")

            self.main_screen.clear_frame()
            self.main_screen.lookup()

        except Exception as e:
            print(f"Error in save: {e}")
        finally:
            if connection:
                connection.close()

    def populate_form(self, patient_data):
        try:
            (
                name,
                dob,
                mrn,
                gender,
                collection_date,
                collection_time,
                diagnosis,
                provider,
            ) = patient_data

            prefilled_fields = {
                "Patient Name": name,
                "Patient DOB": dob,
                "MRN": mrn,
                "Sex": gender,
                "Date Collected": collection_date,
                "Time Collected": collection_time,
                "Specimen Diagnosis": diagnosis,
                "Patient Doctor": provider,
            }

            for field_label, value in prefilled_fields.items():
                entry_widget = self.placeholders.get(field_label)
                if entry_widget:
                    entry_widget.delete(0, "end")
                    entry_widget.insert(0, value if value else "")
                    entry_widget.configure(state="disabled")
        except Exception as e:
            print(f"Error in prefilled fields: {e}")

        try:
            connection = sqlite3.connect("antibiotics.db")
            cursor = connection.cursor()

            query = '''
                SELECT *
                FROM WorkCard
                WHERE userPatientId = ?
            '''
            cursor.execute(query, (self.current_user,))
            record = cursor.fetchone()

            if not record:
                print("No data found for the current user.")
                return

            column_names = [
                "workCardId", "userPatientId", "cultureId", "priority",
                "wbcQty", "epiQty", "gpcQty", "gpbQty", "gncQty", "gnbQty", "otherQty",
                "day1Observation", "day1Date", "day1Time",
                "day2Observation", "day2Date", "day2Time",
                "day3Observation", "day3Date", "day3Time",
                "day4Observation", "day4Date", "day4Time",
                "day5Observation", "day5Date", "day5Time",
                "finalObservation", "finalDate", "finalTime",
                "criticalResults"
            ]

            workcard_data = dict(zip(column_names, record))

            for key, value in workcard_data.items():
                if key in self.placeholders:
                    entry_widget = self.placeholders[key]
                    if isinstance(entry_widget, customtkinter.CTkEntry):
                        # For text fields
                        entry_widget.delete(0, "end")
                        entry_widget.insert(0, value if value else "")
                    elif isinstance(entry_widget, customtkinter.CTkTextbox):
                        # For textboxes (e.g., critical results)
                        entry_widget.delete("1.0", "end")
                        entry_widget.insert("1.0", value if value else "")
                    elif isinstance(entry_widget, customtkinter.CTkOptionMenu):
                        # For dropdowns (e.g., priority)
                        entry_widget.set(value if value else "")

            if "cultureId" in workcard_data:
                culture_id_widget = self.placeholders.get("Culture ID")
                if culture_id_widget:
                    culture_id_widget.delete(0, "end")
                    culture_id_widget.insert(0, workcard_data["cultureId"])

            if "priority" in workcard_data:
                priority_widget = self.placeholders.get("Priority")
                if priority_widget:
                    priority_widget.set(workcard_data["priority"])

            gram_stain_fields = {
                "WBC": "wbcQty",
                "EPI": "epiQty",
                "GPC": "gpcQty",
                "GPB": "gpbQty",
                "GNC": "gncQty",
                "GNB": "gnbQty",
                "Other": "otherQty",
            }
            for field, column in gram_stain_fields.items():
                widget = self.placeholders.get(field)
                if widget and column in workcard_data:
                    widget.delete(0, "end")
                    widget.insert(0, workcard_data[column])

        except Exception as e:
            print(f"Error in populate_form for Work Card: {e}")

        finally:
            if connection:
                connection.close()






