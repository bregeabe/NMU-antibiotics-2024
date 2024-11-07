import customtkinter

class Specimen_Requisition:

    def __init__(self, main_screen):
        self.main_screen = main_screen
        self.right_dashboard = main_screen.right_dashboard

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
        placeholders = ["First last", "MM/DD/YYYY", "******", "Male / Female", "Dr. ...", "Check up, ...", "MM/DD/YYYY", "Military time", "Urine, sputum, ...", "Urine culture, ...", "Yes / No"]
        for i, placeholder in enumerate(placeholders):
            entry = customtkinter.CTkEntry(self.left_spec_frame, placeholder_text=placeholder, font=self.mainFont, width=250)
            entry.grid(column=1, row=i+1, padx=10, pady=5)

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

    # Define the actions for the buttons
    def cancel_action(self):
        self.main_screen.clear_frame()
        self.main_screen.lookup()
        print("Cancelled. Returning to previous screen.")
        
    def submit_action(self):
        self.main_screen.clear_frame()
        self.main_screen.lookup()
        print("Submitted. Data saved.")
