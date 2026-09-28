import customtkinter as ctk
from tkinter import messagebox
import os

# --- 1. Import all your existing modules ---
# Make sure these match the exact names of your python files and classes
from student import Student
from f_r import f_d
from attendencs import atd
from train import Train

# --- 2. Set the Aesthetic Profile ---
ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("dark-blue")

class ModernFaceRecognitionSystem(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Window Setup ---
        self.title("Facial Recognition System")
        self.geometry("1050x650")
        self.iconbitmap("face.ico") if os.path.exists("face.ico") else None

        # Grid layout (1 row, 2 columns for a Sidebar layout)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # ==========================================
        # SIDEBAR NAVIGATION
        # ==========================================
        self.sidebar_frame = ctk.CTkFrame(self, width=220, corner_radius=0, fg_color="#121212")
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(7, weight=1) 

        self.logo_label = ctk.CTkLabel(
            self.sidebar_frame, 
            text="Admin Panel", 
            font=ctk.CTkFont(family="Helvetica", size=24, weight="bold")
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(30, 40))

        # --- Sidebar Buttons ---
        button_style = {
            "fg_color": "transparent", 
            "border_width": 1, 
            "text_color": "#DCE4EE", 
            "hover_color": "#2b2b2b",
            "font": ctk.CTkFont(family="Helvetica", size=14),
            "anchor": "w"
        }

        self.btn_student = ctk.CTkButton(self.sidebar_frame, text="  Student Details", command=self.open_student, **button_style)
        self.btn_student.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        self.btn_detector = ctk.CTkButton(self.sidebar_frame, text="  Face Detector", command=self.open_detector, **button_style)
        self.btn_detector.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        self.btn_attendance = ctk.CTkButton(self.sidebar_frame, text="  Attendance Log", command=self.open_attendance, **button_style)
        self.btn_attendance.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

        self.btn_train = ctk.CTkButton(self.sidebar_frame, text="  Train Dataset", command=self.open_train, **button_style)
        self.btn_train.grid(row=4, column=0, padx=20, pady=10, sticky="ew")

        self.btn_photos = ctk.CTkButton(self.sidebar_frame, text="  View Photos", command=self.open_photos, **button_style)
        self.btn_photos.grid(row=5, column=0, padx=20, pady=10, sticky="ew")

        # Exit Button 
        self.btn_exit = ctk.CTkButton(
            self.sidebar_frame, 
            text="Exit System", 
            fg_color="#C0392B", 
            hover_color="#922B21", 
            font=ctk.CTkFont(family="Helvetica", size=14, weight="bold"),
            command=self.exit_system
        )
        self.btn_exit.grid(row=8, column=0, padx=20, pady=30, sticky="ew")

        # ==========================================
        # MAIN CONTENT AREA
        # ==========================================
        self.main_frame = ctk.CTkFrame(self, fg_color="#1e1e1e", corner_radius=15)
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.title_lbl = ctk.CTkLabel(
            self.main_frame, 
            text="FACIAL RECOGNITION\nATTENDANCE SYSTEM", 
            font=ctk.CTkFont(family="Helvetica", size=38, weight="bold"), 
            text_color="#F0F0F0",
            justify="center"
        )
        self.title_lbl.pack(pady=(150, 20))

        self.sub_lbl = ctk.CTkLabel(
            self.main_frame, 
            text="Select a module from the sidebar menu to begin configuring the system.", 
            font=ctk.CTkFont(family="Helvetica", size=16), 
            text_color="#888888"
        )
        self.sub_lbl.pack()

    # ==========================================
    # ROUTING FUNCTIONS (These open your screens)
    # ==========================================
    def open_student(self):
        self.new_window = ctk.CTkToplevel(self)
        self.app = Student(self.new_window)

    def open_detector(self):
        self.new_window = ctk.CTkToplevel(self)
        self.app = f_d(self.new_window)

    def open_attendance(self):
        self.new_window = ctk.CTkToplevel(self)
        self.app = atd(self.new_window)

    def open_train(self):
        self.new_window = ctk.CTkToplevel(self)
        self.app = Train(self.new_window)

    def open_photos(self):
        if os.path.exists("data"):
            os.startfile("data")
        else:
            messagebox.showerror("Error", "Data folder not found!")

    def exit_system(self):
        if messagebox.askyesno("Confirm Exit", "Are you sure you want to close the application?"):
            self.destroy()

if __name__ == "__main__":
    app = ModernFaceRecognitionSystem()
    app.mainloop()