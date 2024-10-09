import tkinter
import customtkinter
from lookup_frame import LookupFrame

DARK_MODE = "dark"
customtkinter.set_appearance_mode(DARK_MODE)
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        
        self.title("Change Frames")
        self.overrideredirect(True)
        self.focus_force()
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        
        self.login_container = customtkinter.CTkFrame(self, corner_radius=10)
        self.main_container = customtkinter.CTkFrame(self, corner_radius=10)
        self.signup_container = customtkinter.CTkFrame(self, corner_radius=10)

        self.create_login_frame()
        self.create_main_frame()   
        self.create_signup_frame()
        
        self.show_login_screen()

    def create_signup_frame(self):
        self.signup_label = customtkinter.CTkLabel(self.signup_container, text="Sign Up", font=customtkinter.CTkFont(size=24, weight="bold"))
        self.signup_label.pack(pady=50)

        self.username_entry = customtkinter.CTkEntry(self.signup_container, placeholder_text="First Name")
        self.username_entry.pack(pady=10)

        self.password_entry = customtkinter.CTkEntry(self.signup_container, placeholder_text="Last Name")
        self.password_entry.pack(pady=10)

        self.signup_button = customtkinter.CTkButton(self.signup_container, text="Sign Up", command=self.show_login_screen)
        self.signup_button.pack(pady=10)

        self.bt_to_login = customtkinter.CTkButton(self.signup_container, text="Back to Login", command=self.show_login_screen)
        self.bt_to_login.pack(pady=10)

    def create_login_frame(self):
        self.login_container.pack(fill=tkinter.BOTH, expand=True, padx=10, pady=10)

        self.login_label = customtkinter.CTkLabel(self.login_container, text="Scan NMU ID", font=customtkinter.CTkFont(size=32, weight="bold"))
        self.login_label.pack(pady=50)

        self.login_label = customtkinter.CTkLabel(self.login_container, text="or enter the 14 digit code on the back", font=customtkinter.CTkFont(size=12, weight="normal"))
        self.login_label.pack(pady=10)

        self.nmuIN_entry = customtkinter.CTkEntry(self.login_container, placeholder_text="Click", show="*")
        self.nmuIN_entry.pack(pady=10)

        self.nmuIN_entry.bind("<Return>", self.login) #Binds enter to the login method

        self.login_button = customtkinter.CTkButton(self.login_container, text="Login", command=self.login)
        self.login_button.pack(pady=10)

        self.bt_signup = customtkinter.CTkButton(self.login_container, text="Sign Up", command=self.show_signup_screen)
        self.bt_signup.pack(pady=10)

        self.bt_Quit = customtkinter.CTkButton(self.login_container, text="Quit", fg_color= '#EA0000', hover_color = '#B20000', command=self.close_window)
        self.bt_Quit.pack(pady=10)

    def create_main_frame(self):
        self.main_container.pack(fill=tkinter.BOTH, expand=True, padx=10, pady=10)
        
        self.left_side_panel = customtkinter.CTkFrame(self.main_container, width=150, corner_radius=10)
        self.left_side_panel.pack(side=tkinter.LEFT, fill=tkinter.Y, expand=False, padx=5, pady=5)

        self.left_side_panel.grid_columnconfigure(0, weight=1)
        self.left_side_panel.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=0)

        self.logo_label = customtkinter.CTkLabel(self.left_side_panel, text="NMU Antibiotic Report \n", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(40, 10))

        self.bt_categories = customtkinter.CTkButton(self.left_side_panel, text="Barcode Scanning", command=self.scanning)
        self.bt_categories.grid(row=1, column=0, padx=20, pady=10)

        self.bt_statement = customtkinter.CTkButton(self.left_side_panel, text="Create Patient", command=self.create)
        self.bt_statement.grid(row=3, column=0, padx=20, pady=10)

        self.bt_categories = customtkinter.CTkButton(self.left_side_panel, text="Specimen Requisition", command=self.requisition)
        self.bt_categories.grid(row=4, column=0, padx=20, pady=10)

        self.bt_categories = customtkinter.CTkButton(self.left_side_panel, text="Specimen Workcard", command=self.workcard)
        self.bt_categories.grid(row=5, column=0, padx=20, pady=10)

        self.bt_categories = customtkinter.CTkButton(self.left_side_panel, text="Simulated Biochems", command=self.biochems)
        self.bt_categories.grid(row=6, column=0, padx=20, pady=10)

        self.bt_Quit = customtkinter.CTkButton(self.left_side_panel, text="Change User", fg_color= '#EA0000', hover_color = '#B20000', command=self.show_login_screen)
        self.bt_Quit.grid(row=9, column=0, padx=20, pady=10)

        self.bt_Quit = customtkinter.CTkButton(self.left_side_panel, text="Quit", fg_color= '#EA0000', hover_color = '#B20000', command=self.close_window)
        self.bt_Quit.grid(row=10, column=0, padx=20, pady=10)

        self.right_side_panel = customtkinter.CTkFrame(self.main_container, corner_radius=10, fg_color="#000811")
        self.right_side_panel.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=5, pady=5)

        self.right_dashboard = customtkinter.CTkFrame(self.main_container, corner_radius=10, fg_color="#000811")
        self.right_dashboard.pack(in_=self.right_side_panel, side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)

        #Create lookup frame + lookup page button
        self.lookup_frame = LookupFrame(self)
        self.bt_dashboard = customtkinter.CTkButton(self.left_side_panel, text="Patient Lookup", command=self.lookup_frame.lookup)
        self.bt_dashboard.grid(row=2, column=0, padx=20, pady=10)

    def show_login_screen(self):
        self.main_container.pack_forget()  # Hide the main container
        self.signup_container.pack_forget()
        self.login_container.pack(fill=tkinter.BOTH, expand=True)

    def show_main_screen(self):
        self.login_container.pack_forget()  # Hide the login container
        self.main_container.pack(fill=tkinter.BOTH, expand=True)

    def show_signup_screen(self):
        print("Sign up button clicked")
        self.login_container.pack_forget()   # Hide the login container
        self.main_container.pack_forget()    # Hide the main container
        self.signup_container.pack(fill=tkinter.BOTH, expand=True)

    def signup(self):
        # first_name = self.first_name_entry.get()
        # last_name = self.last_name_entry.get()
        # print(f"Sign Up Successful: {first_name} {last_name}")
        self.first_name_entry.delete(0, tkinter.END)
        self.last_name_entry.delete(0, tkinter.END)
        self.show_login_screen()

    def login(self, event=None):
        nmuIN = self.nmuIN_entry.get()
        if nmuIN == "00":
            self.nmuIN_entry.delete(0, tkinter.END)
            self.show_main_screen()
        else:
            self.login_label.config(text="Login Failed. Try Again.", fg_color="red")

    def lookup(self):
        self.clear_frame()
        self.bt_from_frame1 = customtkinter.CTkButton(self.right_dashboard, text="dash", command=lambda: print("test dash"))
        self.bt_from_frame1.grid(row=0, column=0, padx=20, pady=(10, 0))

    def create(self):
        self.clear_frame()
        self.bt_from_frame3 = customtkinter.CTkButton(self.right_dashboard, text="statement", command=lambda: print("test statement"))
        self.bt_from_frame3.grid(row=0, column=0, padx=20, pady=(10, 0))

    def scanning(self):
        self.clear_frame()

    def requisition(self):
        self.clear_frame()

    def workcard(self):
        self.clear_frame()

    def biochems(self):
        self.clear_frame()

    def close_window(self):
        App.destroy(self)

    def clear_frame(self):
        for widget in self.right_dashboard.winfo_children():
            widget.destroy()


a = App()
a.mainloop()
