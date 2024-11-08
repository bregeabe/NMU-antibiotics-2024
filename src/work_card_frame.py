import customtkinter

class Work_Card_Frame:
    def __init__(self, main_screen):
        self.main_screen = main_screen
        self.right_dashboard = main_screen.right_dashboard

        self.mainFont = customtkinter.CTkFont(size=16)
        self.headerFont = customtkinter.CTkFont(size=18, weight="bold")

    def build(self):
        # Clear any existing widgets in the dashboard
        self.main_screen.clear_frame()
        print("displaying workcard")

        #Configure the grid
        self.right_dashboard.grid_columnconfigure(0, weight=1)

        # Build each section of the work card
        self.create_title()
    
    def create_title(self):
        aFont = customtkinter.CTkFont(size=30, weight="bold")
        title_label = customtkinter.CTkLabel(self.right_dashboard, text="NMU Lab Microbiology Work Card", font=aFont)
        title_label.grid(row=0, column=0, columnspan=2, pady=(10, 20), sticky="ew")


    def create_prefilled_section(self):
        pass

    def create_non_prefilled_section(self):
        pass

    def create_culture_id(self):
        pass

    def create_priority(self):
        pass

    def create_direct_gram_stain(self):
        pass

    def create_button_section(self):
        pass