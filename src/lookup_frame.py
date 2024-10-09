import customtkinter

class LookupFrame:
    def __init__(self, main_screen):
        # Store a reference to the main application
        self.main_screen = main_screen
        
        # This frame will hold all lookup UI components
        self.right_dashboard = self.main_screen.right_dashboard
    
    def create_frames(self):
        # ! Create look up label ! 
        self.main_screen.lookup_label = customtkinter.CTkLabel(self.main_screen.right_dashboard, text="Patients", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.main_screen.lookup_label.pack(pady=30)

        # ! frame to list patients ! 
        self.main_screen.patient_frame = customtkinter.CTkFrame(self.main_screen.right_dashboard, corner_radius=10, fg_color="#232323")
        self.main_screen.patient_frame.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.8)

        # ! frame to search for patients ! 
        self.main_screen.lookup_frame = customtkinter.CTkFrame(self.main_screen.right_dashboard, corner_radius=0, height=50, fg_color="#333333")
        self.main_screen.lookup_frame.place(relx=0.05, rely=0.1, relwidth=0.9)

        # ! Label 'Results' !
        self.main_screen.result_label = customtkinter.CTkLabel(self.main_screen.lookup_frame, text="Search Results", font=customtkinter.CTkFont(size=22, weight="bold"))
        self.main_screen.result_label.pack(pady=10, padx=15, side='left')

        # ! Search button !
        self.main_screen.search_button = customtkinter.CTkButton(self.main_screen.lookup_frame, text="Search", width=200)
        self.main_screen.search_button.pack(pady=10, padx=15, side='right')

        # ! Search Bar !
        self.main_screen.search_bar = customtkinter.CTkEntry(self.main_screen.lookup_frame, placeholder_text="Search...", width=200)
        self.main_screen.search_bar.pack(pady=10, padx=15, side='right')


        
    def lookup(self):
        self.main_screen.clear_frame()

        self.create_frames()

        # ! Row-ify patients !
        # Needed to configure the amount of rows for patients
        '''amount_of_patients = 5  # get_amount_of_patients
        amount_of_rows = []
        for i in range(1, amount_of_patients):
            amount_of_rows.append(i)

        # ! Layout the grid !
        self.main_screen.lookup_frame.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6,7,8,9,10), weight=1, uniform="column")
        self.main_screen.patient_frame.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6,7,8,9,10), weight=1, uniform="column")
        self.main_screen.patient_frame.grid_rowconfigure(tuple(amount_of_rows), weight=1, uniform="row")
        '''