import customtkinter

class Work_Card_Frame:
    def __init__(self, main_screen):
        self.main_screen = main_screen
        self.right_dashboard = main_screen.right_dashboard

        self.mainFont = customtkinter.CTkFont(size=16)
        self.headerFont = customtkinter.CTkFont(size=18, weight="bold")

    def build(self):
        self.main_screen.clear_frame()
        
        self.right_dashboard.grid_columnconfigure(0, weight=1)

        # Build each section of the work card
        self.create_title()
        self.create_prefilled_section()
        self.create_non_prefilled_section()
        self.create_direct_gram_stain
    
    def create_title(self):
        aFont = customtkinter.CTkFont(size=30, weight="bold")
        title_label = customtkinter.CTkLabel(self.right_dashboard, text="NMU Lab Microbiology Work Card", font=aFont)
        title_label.grid(row=0, column=0, columnspan=2, pady=(10, 20), sticky="ew")


    def create_prefilled_section(self):
        prefilled_frame = customtkinter.CTkFrame(self.right_dashboard)
        prefilled_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")
        
        for col in range(4):  # Four columns for a compact layout
            prefilled_frame.grid_columnconfigure(col, weight=1)

        # Pre-filled fields in a more compact, multi-column layout
        fields = [
            ("Data Collected:", "mm/dd/yy"),
            ("Time Collected:", "HH:MM"),
            ("Tech:", ""),
            ("Patient Name:", ""),
            ("MRN:", ""),
            ("Doctor:", ""),
            ("Sex:", ""),
            ("Specimen Source:", "Description of the source")
        ]

        prefilled_frame.grid_rowconfigure(0, minsize=10)  # Spacer row at the top
        prefilled_frame.grid_rowconfigure(100, minsize=10)  # Spacer row at the bottom

        # Place fields in two items per row for a compact layout
        # Fields is a list of tuples, so place it according to that layout
        for i, (label, placeholder) in enumerate(fields):
            row, col = divmod(i, 4)  # Two rows, four columns
            field_label = customtkinter.CTkLabel(prefilled_frame, text=label, font=self.mainFont)
            field_label.grid(row=row * 2, column=col, padx=(10, 5), pady=2, sticky="w")
            
            field_entry = customtkinter.CTkEntry(prefilled_frame, placeholder_text=placeholder)
            field_entry.grid(row=row * 2 + 1, column=col, padx=(5, 10), pady=2, sticky="ew")


    def create_non_prefilled_section(self):
        non_prefilled_frame = customtkinter.CTkFrame(self.right_dashboard)
        non_prefilled_frame.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")
        non_prefilled_frame.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1)

        self.create_culture_id(non_prefilled_frame)
        self.create_priority(non_prefilled_frame)
        self.create_direct_gram_stain(non_prefilled_frame)

    def create_culture_id(self, aFrame):
        culture_id_label = customtkinter.CTkLabel(aFrame, text="Culture ID:", font=self.mainFont)
        culture_id_label.grid(row=0, column=0, padx=(10, 5), pady=5, sticky="w")

        culture_id_entry = customtkinter.CTkEntry(aFrame, placeholder_text="1-20")
        culture_id_entry.grid(row=0, column=1, padx=(5, 10), pady=5, sticky="ew")

    def create_priority(self, aFrame):
        priority_label = customtkinter.CTkLabel(aFrame, text="Priority:", font=self.mainFont)
        priority_label.grid(row=0, column=2, padx=(10, 5), pady=5, sticky="w")

        priority_entry = customtkinter.CTkOptionMenu(aFrame, values=["STAT", "ROUTINE"])
        priority_entry.grid(row=0, column=3, padx=(5, 10), pady=5, sticky="ew")

    def create_direct_gram_stain(self, aFrame):
        gram_stain_frame = customtkinter.CTkFrame(aFrame)
        gram_stain_frame.grid(row=1, column=0, columnspan=8, padx=10, pady=10, sticky="ew")

        gram_stain_label = customtkinter.CTkLabel(gram_stain_frame, text="Direct Gram Stain:", font=self.mainFont)
        gram_stain_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="w")

        gram_stain_options = ["WBCs", "EPIs", "GPC", "GPB", "GNC", "GNB", "Other"]

        for col in range(len(gram_stain_options) * 2):  # Multiply by 2 for label-entry pairs
            gram_stain_frame.grid_columnconfigure(col, weight=1, uniform="stain")

        for i, option in enumerate(gram_stain_options):
            label = customtkinter.CTkLabel(gram_stain_frame, text=option, font=self.mainFont)
            label.grid(row=0, column=(i * 2)+1, padx=(5, 2), pady=2, sticky="e")

            entry = customtkinter.CTkEntry(gram_stain_frame, width=40, placeholder_text="Qty")
            entry.grid(row=0, column=(i * 2) + 2, padx=(2, 10), pady=2, sticky="w")


    def create_button_section(self):
        pass