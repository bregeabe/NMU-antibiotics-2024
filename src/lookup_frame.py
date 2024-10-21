import customtkinter
import sqlite3

class LookupFrame:
    def __init__(self, main_screen):
        # Store a reference to the main application
        self.main_screen = main_screen
        
        # This frame will hold all lookup UI components
        self.right_dashboard = self.main_screen.right_dashboard

    def build_search_frame(self):
        self.main_screen.search_frame = customtkinter.CTkFrame(self.main_screen.patient_frame, corner_radius=0, height=50, fg_color="#232323")
        self.main_screen.result_label = customtkinter.CTkLabel(self.main_screen.search_frame, text="Search Results", font=customtkinter.CTkFont(size=22, weight="bold"))
        self.main_screen.search_button = customtkinter.CTkButton(self.main_screen.search_frame, text="Search", width=200)
        self.main_screen.search_bar = customtkinter.CTkEntry(self.main_screen.search_frame, placeholder_text="Search...", width=200)

    def build_labels_frame(self):
        
        self.main_screen.labels_frame = customtkinter.CTkFrame(self.main_screen.patient_frame, height=50, corner_radius=0, fg_color="#333333")
        self.main_screen.name_label = customtkinter.CTkLabel(self.main_screen.labels_frame, text="Name", font=customtkinter.CTkFont(size=18), width=200)
        self.main_screen.dob_label = customtkinter.CTkLabel(self.main_screen.labels_frame, text="DOB", font=customtkinter.CTkFont(size=18), width=50)
        self.main_screen.sex_label = customtkinter.CTkLabel(self.main_screen.labels_frame, text="Sex", font=customtkinter.CTkFont(size=18), width=50)
        self.main_screen.mrn_label = customtkinter.CTkLabel(self.main_screen.labels_frame, text="MRN", font=customtkinter.CTkFont(size=18), width=50)
        self.main_screen.spec_req_label = customtkinter.CTkLabel(self.main_screen.labels_frame, text="Specimen Req", font=customtkinter.CTkFont(size=18), width=100)
        self.main_screen.work_card_label = customtkinter.CTkLabel(self.main_screen.labels_frame, text="Work Card", font=customtkinter.CTkFont(size=18), width=100)

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
    
    def build_frames(self):
        self.main_screen.lookup_label = customtkinter.CTkLabel(self.main_screen.right_dashboard, text="Patients", font=customtkinter.CTkFont(size=30, weight="bold"))

        self.main_screen.patient_frame = customtkinter.CTkScrollableFrame(self.main_screen.right_dashboard, corner_radius=10, fg_color="#333333")

        self.build_search_frame()

        self.build_labels_frame()

    def place_frames(self):
        self.main_screen.lookup_label.pack(pady=30)
        self.main_screen.patient_frame.place(relx=0.051, rely=0.1, relwidth=0.9, relheight=0.8) # For some odd reason, relx=0.5 leaves a tiny pixel behind on the right

        self.place_search_frame()

        self.place_labels_frame()

    def get_spec_req(self):
        pass
    
    def get_work_card(self):
        pass    

    def lookup(self):
        self.main_screen.clear_frame()

        self.build_frames()
        self.place_frames()

        # Grab all the patients
        # For each patient, create a new frame, layout all the labels

        connection = sqlite3.connect('antibiotics.db')
        db = connection.cursor()
    
        db.execute('SELECT * FROM Patients')
        patients = db.fetchall()
        # This is currently very slow, will optimize soon
        rowcount = 2
        for patient in patients:
            temp_frame = customtkinter.CTkFrame(self.main_screen.patient_frame, fg_color="#333333", height=50, corner_radius=0)
            customtkinter.CTkLabel(temp_frame, text=patient[2], font=customtkinter.CTkFont(size=16), width=200).grid(column=0, row=0)
            customtkinter.CTkLabel(temp_frame, text=patient[3], font=customtkinter.CTkFont(size=16), width=50).grid(column=1, row=0)
            customtkinter.CTkLabel(temp_frame, text=patient[4], font=customtkinter.CTkFont(size=16), width=50).grid(column=2, row=0)
            customtkinter.CTkLabel(temp_frame, text=patient[1], font=customtkinter.CTkFont(size=16), width=50).grid(column=3, row=0)
            customtkinter.CTkButton(temp_frame, text="Specimen Req", command=self.get_spec_req, font=customtkinter.CTkFont(size=16), width=125).grid(column=4, row=0)
            customtkinter.CTkButton(temp_frame, text="Work Card", command=self.get_work_card, font=customtkinter.CTkFont(size=16), width=100).grid(column=5, row=0)
            temp_frame.grid(column=0,row=rowcount,sticky="ew", pady=5)
            temp_frame.grid_columnconfigure((0,1,2,3,4,5), weight=1)
            rowcount += 1
        connection.close()

        self.main_screen.patient_frame.grid_rowconfigure((0,1,2), weight=0, minsize=50 )
        self.main_screen.patient_frame.grid_columnconfigure((0), weight=1, uniform="column")