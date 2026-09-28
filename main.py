from tkinter import *
from tkinter import ttk
from student import Student
from f_r import f_d
from attendencs import atd
from train import Train
import os
from devloper import Devloper
from tkinter import messagebox

class Face_Recognition_System:
    
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.configure(bg='#1e1e1e')
        
        # Title
        self.title_lbl = Label(self.root, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", 
                               font=("times new roman", 32, "bold"), bg="#282828", fg="white")
        self.title_lbl.place(x=0, y=0, width=1530, height=60)
        
        # Button Frame
        self.frame = Frame(self.root, bg="#1e1e1e")
        self.frame.place(x=100, y=100, width=1300, height=600)
        
        # Buttons
        buttons = [
            ("Student Details", self.student_details, 100, 100),
            ("Face Detector", self.face_d, 400, 100),
            ("Attendance", self.attendence, 700, 100),
            ("Train Data", self.train, 100, 300),
            ("Photos", self.open_img, 400, 300),
            ("Developer", self.devp, 700, 300),
            ("Exit", self.exit_window, 1000, 200)
        ]
        
        for text, command, x, y in buttons:
            btn = Button(self.frame, text=text, command=command, font=("Arial", 14, "bold"), bg="#444444", 
                         fg="white", width=15, height=2, relief=RIDGE, cursor="hand2")
            btn.place(x=x, y=y, width=180, height=50)
        
        # Animation
        self.animate_bg()
        
    def animate_bg(self):
        colors = ["#1e1e1e", "#2a2a2a", "#1e1e1e", "#121212"]
        self.root.configure(bg=colors[0])
        colors.append(colors.pop(0))
        self.root.after(1000, self.animate_bg)
        
    def open_img(self):
        os.startfile("data")
        
    def exit_window(self):
        response = messagebox.askyesno("Exit Confirmation", "Are you sure you want to exit?")
        if response:
            self.root.destroy()
    
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
    
    def train(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)
        
    def face_d(self):
        self.new_window = Toplevel(self.root)
        self.app = f_d(self.new_window)
        
    def attendence(self):
        self.new_window = Toplevel(self.root)
        self.app = atd(self.new_window)
    
    def devp(self):
        self.new_window = Toplevel(self.root)
        self.app = Devloper(self.new_window)
        
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
