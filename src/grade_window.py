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

        grade_box = customtkinter.CTkEntry(background_frame, width=100)
        grade_box.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        feedback_label = customtkinter.CTkLabel(background_frame, text="Feedback: ", font=self.main_font)
        feedback_label.grid(row=1, column=0, padx= 10, pady=0, columnspan=2)

        feedback_box = customtkinter.CTkTextbox(background_frame)
        feedback_box.grid(row=2, column=0, padx= 10, pady = 10, sticky="nsew", columnspan=2)

    def create(self):
        self.create_window()

        background_frame = customtkinter.CTkFrame(self.grade_window)
        background_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.grade_window.grid_columnconfigure((0), weight=1)
        self.grade_window.grid_rowconfigure((0), weight=1)

        self.create_grade_widgets(background_frame)

        background_frame.columnconfigure((0,1), weight=1)
        background_frame.rowconfigure((0,1,2), weight=1)
        # add save and cancel button.