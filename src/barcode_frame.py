import customtkinter

class BarcodeFrame:
    def __init__(self, main_screen):
        self.main_screen = main_screen
        self.right_dashboard = self.main_screen.right_dashboard

    def build_barcode_frame(self):
        self.main_screen.barcode_frame = customtkinter.CTkFrame(self.main_screen.right_dashboard, corner_radius=10, fg_color="#333333")
        self.main_screen.scan_label = customtkinter.CTkLabel(self.main_screen.barcode_frame, text="Scan a specimens barcode", font=customtkinter.CTkFont(size=24, weight="bold"))
        self.main_screen.barcode_entry = customtkinter.CTkEntry(self.main_screen.barcode_frame, placeholder_text="click", width=300)

    def place_barcode_frame(self):
        self.main_screen.barcode_frame.pack(pady=100, padx=20, fill="both", expand=True)
        self.main_screen.scan_label.pack(pady=20)
        self.main_screen.barcode_entry.pack(pady=20)

    def barcode(self):
        self.main_screen.clear_frame()
        self.build_barcode_frame()
        self.place_barcode_frame()
