import customtkinter
import sqlite3
import dbCalls

class Grade_window():

    def __init__(self, main_screen, user_patient_id):
        self.main_screen = main_screen
        self.main_font = customtkinter.CTkFont(size=18)
        self.user_patient_id = user_patient_id

    def create_window(self):
        self.grade_window = customtkinter.CTkToplevel(self.main_screen)
        self.grade_window.geometry("600x400")
        self.grade_window.title("Patient grade")

    def create_grade_widgets(self, background_frame):
        grade_label = customtkinter.CTkLabel(background_frame, text="Grade: ", font=self.main_font)
        grade_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.grade_box = customtkinter.CTkEntry(background_frame, width=100)
        self.grade_box.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        feedback_label = customtkinter.CTkLabel(background_frame, text="Feedback: ", font=self.main_font)
        feedback_label.grid(row=1, column=0, padx= 10, pady=0, columnspan=2)

        self.feedback_box = customtkinter.CTkTextbox(background_frame)
        self.feedback_box.grid(row=2, column=0, padx= 10, pady = 10, sticky="nsew", columnspan=2)

    def create_button_section(self, aFrame):

        button_frame = customtkinter.CTkFrame(aFrame)
        button_frame.grid(row=4, column=0, columnspan=8, padx=10, pady=10, sticky="ew")

        cancel_button = customtkinter.CTkButton(button_frame, text="Cancel", command=self.cancel)
        cancel_button.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        save_button = customtkinter.CTkButton(button_frame, text="Save", command=self.save)
        save_button.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        button_frame.grid_columnconfigure((0,1), weight=1)


    def create(self):
        self.create_window()

        background_frame = customtkinter.CTkFrame(self.grade_window)
        background_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.grade_window.grid_columnconfigure((0), weight=1)
        self.grade_window.grid_rowconfigure((0), weight=1)

        self.create_grade_widgets(background_frame)

        background_frame.columnconfigure((0,1), weight=1)
        background_frame.rowconfigure((0,1,2), weight=1)

        self.create_button_section(background_frame)
        # add save and cancel button.
        self.populate_data()

    def cancel(self):
        self.grade_window.destroy()

    def save(self):
        grade = self.grade_box.get().strip()
        feedback = self.feedback_box.get("1.0", "end-1c").strip()

        try:
            # Connect to the database
            connection = sqlite3.connect('antibiotics.db')
            db = connection.cursor()

            # Update the database
            db.execute('''
                UPDATE UserPatients
                SET grade = ?, feedback = ?
                WHERE userPatientId = ?
            ''', (grade, feedback, self.user_patient_id))

            connection.commit()
            connection.close()

            self.grade_window.destroy()

        except sqlite3.Error as e:
            print("Database Error", f"An error occurred: {e}")

    def populate_data(self):
        try:
            # Connect to the database
            connection = sqlite3.connect('antibiotics.db')
            db = connection.cursor()

            # Query for the grade and feedback using user_patient_id
            db.execute('SELECT grade, feedback FROM UserPatients WHERE userPatientId = ?', (self.user_patient_id,))
            result = db.fetchone()

            # If data is found, populate the fields
            grade, feedback = result
            if grade:
                self.grade_box.insert(0, grade)  # Insert grade into the entry box
            if feedback:
                self.feedback_box.insert("1.0", feedback)  # Insert feedback into the textbox

        except sqlite3.Error as e:
            print(f"Error fetching data: {e}")
        finally:
            if connection:
                connection.close()