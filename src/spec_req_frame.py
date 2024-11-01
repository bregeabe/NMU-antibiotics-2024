import customtkinter

class Specimen_Requisition:

    def __init__(self, main_screen):
        self.main_screen = main_screen
        self.right_dashboard = main_screen.right_dashboard

        self.mainFont = customtkinter.CTkFont(size=16)

    def build_left_labels(self):
        self.name_label = customtkinter.CTkLabel(self.left_spec_frame, text="Name:", font=self.mainFont)
        self.name_label.grid(column=0, row=0, sticky="w", padx=10, pady=10)

        self.dob_label = customtkinter.CTkLabel(self.left_spec_frame, text="Date of Birth:", font=self.mainFont)
        self.dob_label.grid(column=0, row=1, sticky="w", padx=10, pady=10)

        self.mrn_label = customtkinter.CTkLabel(self.left_spec_frame, text="Medical Record Number:", font=self.mainFont)
        self.mrn_label.grid(column=0, row=2, sticky="w", padx=10, pady=10)

        self.sex_label = customtkinter.CTkLabel(self.left_spec_frame, text="Sex:", font=self.mainFont)
        self.sex_label.grid(column=0, row=3, sticky="w", padx=10, pady=10)

        self.ordering_provider_label = customtkinter.CTkLabel(self.left_spec_frame, text="Ordering Provider:", font=self.mainFont)
        self.ordering_provider_label.grid(column=0, row=4, sticky="w", padx=10, pady=10)

        self.diagnosis_label = customtkinter.CTkLabel(self.left_spec_frame, text="Diagnosis:", font=self.mainFont)
        self.diagnosis_label.grid(column=0, row=5, sticky="w", padx=10, pady=10)

        self.collection_date_label = customtkinter.CTkLabel(self.left_spec_frame, text="Collection Date:", font=self.mainFont)
        self.collection_date_label.grid(column=0, row=6, sticky="w", padx=10, pady=10)

        self.collection_time_label = customtkinter.CTkLabel(self.left_spec_frame, text="Collection Time:", font=self.mainFont)
        self.collection_time_label.grid(column=0, row=7, sticky="w", padx=10, pady=10)

        self.source_label = customtkinter.CTkLabel(self.left_spec_frame, text="Specimen Source/Type:", font=self.mainFont)
        self.source_label.grid(column=0, row=8, sticky="w", padx=10, pady=10)

        self.tests_ordered_label = customtkinter.CTkLabel(self.left_spec_frame, text="Tests Ordered:", font=self.mainFont)
        self.tests_ordered_label.grid(column=0, row=9, sticky="w", padx=10, pady=10)

        self.therapy_label = customtkinter.CTkLabel(self.left_spec_frame, text="Is Patient Receiving Therapy?:", font=self.mainFont)
        self.therapy_label.grid(column=0, row=10, sticky="w", padx=10, pady=10)

    def build_left_entries(self):
        self.name_label = customtkinter.CTkEntry(self.left_spec_frame, placeholder_text="Name:", font=self.mainFont, width=200)
        self.name_label.grid(column=1, row=0, padx=10, pady=10)

        self.dob_label = customtkinter.CTkEntry(self.left_spec_frame, placeholder_text="MM/DD/YYYY", font=self.mainFont, width=200)
        self.dob_label.grid(column=1, row=1, padx=10, pady=10)

        self.mrn_label = customtkinter.CTkEntry(self.left_spec_frame, placeholder_text="Medical Record Number:", font=self.mainFont, width=200)
        self.mrn_label.grid(column=1, row=2, padx=10, pady=10)

        self.sex_label = customtkinter.CTkEntry(self.left_spec_frame, placeholder_text="Male / Female", font=self.mainFont, width=200)
        self.sex_label.grid(column=1, row=3, padx=10, pady=10)

        self.ordering_provider_label = customtkinter.CTkEntry(self.left_spec_frame, placeholder_text="Ordering Provider:", font=self.mainFont, width=200)
        self.ordering_provider_label.grid(column=1, row=4, padx=10, pady=10)

        self.diagnosis_label = customtkinter.CTkEntry(self.left_spec_frame, placeholder_text="Diagnosis:", font=self.mainFont, width=200)
        self.diagnosis_label.grid(column=1, row=5, sticky="w", padx=10, pady=10)

        self.collection_date_label = customtkinter.CTkEntry(self.left_spec_frame, placeholder_text="MM/DD/YYYY", font=self.mainFont, width=200)
        self.collection_date_label.grid(column=1, row=6, padx=10, pady=10)

        self.collection_time_label = customtkinter.CTkEntry(self.left_spec_frame, placeholder_text="13:33", font=self.mainFont, width=200)
        self.collection_time_label.grid(column=1, row=7, padx=10, pady=10)

        self.source_label = customtkinter.CTkEntry(self.left_spec_frame, placeholder_text="Specimen Source/Type:", font=self.mainFont, width=200)
        self.source_label.grid(column=1, row=8, padx=10, pady=10)

        self.tests_ordered_label = customtkinter.CTkEntry(self.left_spec_frame, placeholder_text="Tests Ordered:", font=self.mainFont, width=200)
        self.tests_ordered_label.grid(column=1, row=9, padx=10, pady=10)

        self.therapy_label = customtkinter.CTkEntry(self.left_spec_frame, placeholder_text="Is Patient Receiving Therapy?:", font=self.mainFont, width=200)
        self.therapy_label.grid(column=1, row=10, padx=10, pady=10)

    def build_right_labels(self):
        self.time_label = customtkinter.CTkLabel(self.right_spec_frame, text="Time Received in Lab:", font=self.mainFont)
        self.time_label.grid(column=0, row=0, sticky="w", padx=10, pady=10)

        self.acceptable_label = customtkinter.CTkLabel(self.right_spec_frame, text="Is the Specimen Accpetable?:", font=self.mainFont)
        self.acceptable_label.grid(column=0, row=1, sticky="w", padx=10, pady=10)

    def build_right_entries(self):
        self.time_entry = customtkinter.CTkEntry(self.right_spec_frame, placeholder_text="13:33", font=self.mainFont, width=200)
        self.time_entry.grid(column=1, row=0, padx=10, pady=10)

        self.acceptable_entry = customtkinter.CTkEntry(self.right_spec_frame, placeholder_text="Yes / No", font=self.mainFont, width=200)
        self.acceptable_entry.grid(column=1, row=1, padx=10, pady=10)

    def build_frames(self):
        self.left_spec_frame = customtkinter.CTkFrame(self.right_dashboard, fg_color="#232323")
        self.left_spec_frame.place(relx=0.05, rely=0.1, relwidth=0.43, relheight=0.7)

        self.right_spec_frame = customtkinter.CTkFrame(self.right_dashboard, fg_color="#232323")
        self.right_spec_frame.place(relx=0.52, rely=0.1, relwidth=0.43, relheight=0.7)

        self.build_left_labels()
        self.build_left_entries()

        for i in range(11):
            self.right_spec_frame.grid_rowconfigure(i, weight=0)
        self.right_spec_frame.grid_columnconfigure((0, 1), weight=1)      

        self.build_right_labels()
        self.build_right_entries()

        self.right_spec_frame.grid_rowconfigure((0,1), weight=0)
        self.right_spec_frame.grid_columnconfigure((0, 1), weight=1)

    def build(self):
        self.main_screen.clear_frame()

        self.spec_req_label = customtkinter.CTkLabel(self.right_dashboard, text="Specimen Requisition", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.spec_req_label.pack(pady=30)

        self.build_frames()
