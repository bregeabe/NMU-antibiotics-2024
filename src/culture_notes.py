import customtkinter

class Culture_Notes:
    def __init__(self, main_screen):
        self.main_screen = main_screen
        self.right_dashboard = main_screen.right_dashboard

        self.mainFont = customtkinter.CTkFont(size=16)
        self.headerFont = customtkinter.CTkFont(size=18, weight="bold")

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

    def create_culture_workup(self):
        self.culture_frame = customtkinter.CTkFrame(self.biochem_frame)
        self.culture_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        customtkinter.CTkLabel(self.culture_frame, text="Culture Workup", font=self.headerFont).grid(row=0, column=0, sticky="w", padx=10)
        self.culture_entry = customtkinter.CTkTextbox(self.culture_frame, width=375, height=60)
        self.culture_entry.grid(row=1, column=0, padx=10, pady=10)

    def create_colony_desc(self):
        self.colony_frame = customtkinter.CTkFrame(self.biochem_frame)
        self.colony_frame.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        customtkinter.CTkLabel(self.colony_frame, text="Colony Description", font=self.headerFont).grid(row=0, column=0, sticky="w", padx=10)
        self.colony_entry = customtkinter.CTkTextbox(self.colony_frame, width=375, height=60)
        self.colony_entry.grid(row=1, column=0, padx=10, pady=10)

    def create_biochem_desc(self):
        self.reactions_frame = customtkinter.CTkFrame(self.biochem_frame)
        self.reactions_frame.grid(row=0, column=2, padx=10, pady=10, sticky="ew")
        customtkinter.CTkLabel(self.reactions_frame, text="Biochemical Reactions Noted", font=self.headerFont).grid(row=0, column=0, sticky="w", padx=10)
        self.reactions_entry = customtkinter.CTkTextbox(self.reactions_frame, width=375, height=60)
        self.reactions_entry.grid(row=1, column=0, padx=10, pady=10)

    def create_notes(self):
        self.create_culture_workup()
        self.create_colony_desc()
        self.create_biochem_desc()


        # Add initial 6 tests
        for i in range(6):
            self.add_biochem_test(i)
        
        # Configure columns and rows to take up space evenly
        self.biochem_frame.grid_columnconfigure((0, 1, 2), weight=1)
        self.biochem_frame.grid_rowconfigure((1, 2), weight=1)


    def add_biochem_test(self, test_number):
        # Calculate row and column based on the test count
        row, col = divmod(test_number, 3)

        # Frame for each biochem test, placed in a specific row and column
        test_frame = customtkinter.CTkFrame(self.biochem_frame)
        test_frame.grid(row=row + 1, column=col, padx=10, pady=5, sticky="nsew")  # Offset row by 1 for correct positioning

        # Add input fields for the test within this test_frame
        customtkinter.CTkLabel(test_frame, text=f"Biochem Test {test_number + 1}", font=self.headerFont).grid(padx=5, row=0, column=0, columnspan=2, sticky="w")

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
        conditions_entry.grid(row=5, column=1, padx=5, pady=10)


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
        self.main_screen.workcard()

    def save(self):
        self.main_screen.clear_frame()
        self.main_screen.workcard()
