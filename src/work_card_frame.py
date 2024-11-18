import customtkinter
from culture_notes import Culture_Notes

class Work_Card_Frame:
    def __init__(self, main_screen):
        self.main_screen = main_screen
        self.right_dashboard = main_screen.right_dashboard

        self.mainFont = customtkinter.CTkFont(size=16)
        self.headerFont = customtkinter.CTkFont(size=18, weight="bold")

        self.notes = Culture_Notes(main_screen)

    def build(self):
        self.main_screen.clear_frame()
        
        self.right_dashboard.grid_columnconfigure(0, weight=1)

        # Build each section of the work card
        self.create_title()
        self.create_prefilled_section()
        self.create_non_prefilled_section()

    
    def create_title(self):
        aFont = customtkinter.CTkFont(size=30, weight="bold")
        title_label = customtkinter.CTkLabel(self.right_dashboard, text="NMU Lab Microbiology Work Card", font=aFont)
        title_label.grid(row=0, column=0, columnspan=2, pady=(10, 20), sticky="ew")


    def create_prefilled_section(self):
        prefilled_frame = customtkinter.CTkFrame(self.right_dashboard)
        prefilled_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")
        
        for col in range(4): 
            prefilled_frame.grid_columnconfigure(col, weight=1)

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
        self.create_culture_readout(non_prefilled_frame)

        self.create_button_section(non_prefilled_frame)


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

    def create_date_and_time(self, culture_readout_frame, i):
        date_label = customtkinter.CTkLabel(culture_readout_frame, text="Date:", font=self.mainFont)
        date_label.grid(row=i + 1, columnspan=1, column=4, padx=(5, 10), pady=10, sticky="ew")

        date_entry = customtkinter.CTkEntry(culture_readout_frame)
        date_entry.grid(row=i + 1, columnspan=1, column=5, padx=(10, 5), pady=10, sticky="ew")

        time_label = customtkinter.CTkLabel(culture_readout_frame, text="Time:", font=self.mainFont)
        time_label.grid(row=i + 1, columnspan=1, column=6, padx=(5, 10), pady=10, sticky="ew")

        time_entry = customtkinter.CTkEntry(culture_readout_frame)
        time_entry.grid(row=i + 1, columnspan=1, column=7, padx=(10, 5), pady=10, sticky="ew")

    def create_culture_readout(self, aFrame):
        culture_readout_frame = customtkinter.CTkFrame(aFrame)
        culture_readout_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

        culture_readout_label = customtkinter.CTkLabel(culture_readout_frame, text="Culture Readout", font=self.headerFont)
        culture_readout_label.grid(row=0, column=0, columnspan=2, padx=25, pady=10, sticky="w")

        for col in range(12):
            culture_readout_frame.grid_columnconfigure(col, weight=1)

        for i in range(5):
            day_label = customtkinter.CTkLabel(culture_readout_frame, text=f"Day {i+1}:", font=self.mainFont)
            day_label.grid(row=i + 1, column=0, padx=(10, 5), pady=10, sticky="e")

            day_entry = customtkinter.CTkEntry(culture_readout_frame, placeholder_text=f"Observations for Day {i+1}")
            day_entry.grid(row=i + 1, columnspan=3, column=1, padx=(5, 10), pady=10, sticky="ew")

            self.create_date_and_time(culture_readout_frame, i)

        final_label = customtkinter.CTkLabel(culture_readout_frame, text="Final: ", font=self.mainFont)
        final_label.grid(row=6, column=0, padx=(10, 5), pady=10, sticky="e")

        final_entry = customtkinter.CTkEntry(culture_readout_frame, placeholder_text="Final observations")
        final_entry.grid(row=6, columnspan=3, column=1, padx=(5, 10), pady=10, sticky="ew")

        self.create_date_and_time(culture_readout_frame, 5)

        critical_results_frame = customtkinter.CTkFrame(aFrame)
        critical_results_frame.grid(row=2, column=4, columnspan=4, padx=10, pady=10, sticky="nsew")
        critical_results_frame.grid_columnconfigure(0, weight=1)  # Make sure the column expands
        critical_results_frame.grid_rowconfigure(1, weight=1)  # Ensure row expands vertically

        critical_results_label = customtkinter.CTkLabel(critical_results_frame, text="Critical Results", font=self.headerFont)
        critical_results_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        critical_results_entry = customtkinter.CTkTextbox(critical_results_frame, height=60)
        critical_results_entry.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

    def go_to_biochems(self):
        pass

    def go_to_culture_notes(self):
        self.notes.build()

    def create_button_section(self, non_prefilled_frame):

        button_frame = customtkinter.CTkFrame(non_prefilled_frame)
        button_frame.grid(row=4, column=0, columnspan=8, padx=10, pady=10, sticky="ew")

        # Configure middle columns to take up the extra space
        for col in range(2, 6):
            button_frame.grid_columnconfigure(col, weight=1)
        
        culture_notes_button = customtkinter.CTkButton(button_frame, text="Culture Notes and Tests", command=self.go_to_culture_notes)
        culture_notes_button.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        
        cancel_button = customtkinter.CTkButton(button_frame, text="Cancel", command=self.cancel)
        cancel_button.grid(row=0, column=6, padx=5, pady=5, sticky="e")

        save_button = customtkinter.CTkButton(button_frame, text="Save", command=self.save)
        save_button.grid(row=0, column=7, padx=5, pady=5, sticky="e")

    def cancel(self):
        self.main_screen.clear_frame()
        self.main_screen.lookup()

    def save(self):
        self.main_screen.clear_frame()
        self.main_screen.lookup()