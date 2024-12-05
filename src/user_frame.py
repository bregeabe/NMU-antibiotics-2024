import customtkinter
import sqlite3
import dbCalls

class Users_Frame:
    def __init__(self, main_screen):
        self.main_screen = main_screen
        self.right_dashboard = main_screen.right_dashboard
        self.mainFont = customtkinter.CTkFont(size=16)

    def build_search_frame(self):
        self.search_frame = customtkinter.CTkFrame(self.create_patient_frame, corner_radius=0, height=50, fg_color="#232323")
        self.result_label = customtkinter.CTkLabel(self.search_frame, text="Search Results", font=customtkinter.CTkFont(size=22, weight="bold"))
        self.search_button = customtkinter.CTkButton(self.search_frame, text="Search", width=200, command=self.search)
        self.search_bar = customtkinter.CTkEntry(self.search_frame, placeholder_text="Search...", width=200)
        self.search_bar.bind("<Return>", self.search)

    def build_labels_frame(self):
        aFont = customtkinter.CTkFont(size=18)
        self.labels_frame = customtkinter.CTkFrame(self.patient_frame, height=50, corner_radius=0, fg_color="#333333")
        self.first_name_label = customtkinter.CTkLabel(self.labels_frame, text="First name", font=aFont, width=150)
        self.last_name_label = customtkinter.CTkLabel(self.labels_frame, text="Last name", font=aFont, width=150)
        self.viewed_label = customtkinter.CTkLabel(self.labels_frame, text="Viewed", font=aFont, width=90)
        self.create_label = customtkinter.CTkLabel(self.labels_frame, text="View as user", font=aFont, width=150)

    def place_search_frame(self):
        self.search_frame.grid(column=0, row=0, sticky="ew", padx=15)
        self.result_label.pack(pady=10, padx=15, side='left')
        self.search_button.pack(pady=10, padx=15, side='right')
        self.search_bar.pack(pady=10, padx=15, side='right')

    def place_labels_frame(self):
        self.labels_frame.grid(row=0, column=0, sticky="ew")
        self.first_name_label.grid(row=0,column=0)
        self.last_name_label.grid(row=0,column=1)
        self.viewed_label.grid(row=0,column=2)
        self.create_label.grid(row=0,column=3)

        self.labels_frame.grid_columnconfigure((0,1,2,3), weight=1)
        self.labels_frame.grid_rowconfigure((0), weight=1)

    def build_frames(self):
        self.lookup_label = customtkinter.CTkLabel(self.right_dashboard, text="Users", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.create_patient_frame = customtkinter.CTkFrame(self.right_dashboard, corner_radius=10, fg_color="#232323")
        self.build_search_frame()
        self.patient_frame = customtkinter.CTkScrollableFrame(self.create_patient_frame, corner_radius=10, fg_color="#333333")
        self.build_labels_frame()

    def place_frames(self):
        self.lookup_label.pack(pady=30)
        self.create_patient_frame.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.8)
        self.create_patient_frame.grid_columnconfigure((0), weight=1)
        self.patient_frame.place(relx=0.025, rely=0.075, relwidth=0.95, relheight=0.9)
        self.place_search_frame()
        self.place_labels_frame()

    def update_viewed_status(self, userId, checkbox_var):
        print("Saving view checkbox...")
        connection = sqlite3.connect('antibiotics.db')
        db = connection.cursor()
        try:
            query = "UPDATE users SET hasBeenViewed = ? WHERE nmuIn = ?"
            db.execute(query, (checkbox_var.get(), userId))
            connection.commit()
        finally:
            connection.close()

    # Creates the new user row, put in a method for reusing in search
    def add_user_row(self, user, rowcount):
        temp_frame = customtkinter.CTkFrame(self.patient_frame, height=50, corner_radius=0, fg_color="#333333")
        customtkinter.CTkLabel(temp_frame, text=user[2], font=self.mainFont, width=150).grid(column=0, row=0)
        customtkinter.CTkLabel(temp_frame, text=user[3], font=self.mainFont, width=150).grid(column=1, row=0)
        checkbox_var = customtkinter.IntVar(value=user[5])
        customtkinter.CTkCheckBox(temp_frame, text="Viewed", font=self.mainFont, width=90, variable=checkbox_var, command = lambda userId=user[1] : self.update_viewed_status(userId, checkbox_var)).grid(column=2,row=0)
        customtkinter.CTkButton(temp_frame, text="View as", command=lambda userId=user[1] : self.main_screen.view_as(userId), font=self.mainFont, width=150).grid(column=3, row=0)
        temp_frame.grid(column=0,row=rowcount,sticky="ew", pady=5)
        temp_frame.grid_columnconfigure((0,1,2,3), weight=1)

    def build(self):
        self.main_screen.clear_frame()
        self.build_frames()
        self.place_frames()
        
        connection = sqlite3.connect('antibiotics.db')
        db = connection.cursor()

        users = dbCalls.getAllUsers(db, True)

        for rowcount, user in enumerate(users, 1):
            self.add_user_row(user, rowcount)
        connection.close()
        self.patient_frame.grid_rowconfigure((0,1,2), weight=0, minsize=50 )
        self.patient_frame.grid_columnconfigure((0), weight=1, uniform="column")

# event=none because we dont need the event of pressing enter, just call this function
    def search(self, event=None):
        #Get the users input and remove all white space
        entry = self.search_bar.get().strip()
        #Clear the patient frame for new entries
        for widget in self.patient_frame.winfo_children():
            widget.destroy()

        #Place back the labels at the top of the frame
        self.build_labels_frame()
        self.place_labels_frame()

        #Search for their entry in the db
        connection = sqlite3.connect('antibiotics.db')
        db = connection.cursor()
        query = "SELECT * FROM users WHERE name LIKE ? OR mrn LIKE ? OR dob LIKE ?"
        users = db.execute(query, (f"%{entry}%", f"%{entry}%", f"%{entry}%")).fetchall()
        connection.close()

        #if anything was found, show that information. Otherwise, say nothing was found
        if users:
            for rowcount, user in enumerate(users, 1):
                self.add_user_row(user, rowcount)
        else:
            customtkinter.CTkLabel(self.patient_frame, text="No results found", font=self.mainFont).grid(column=0, row=2, pady=10)

        #make sure the frame looks correct and you cannot scroll pass where patients are.
        self.patient_frame.grid_rowconfigure((0, 1, 2), weight=0, minsize=50)
        self.patient_frame.grid_columnconfigure((0), weight=1, uniform="column")