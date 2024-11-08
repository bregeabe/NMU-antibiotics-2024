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

        # Build each section of the work card
    
    def create_title(self):
        pass

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