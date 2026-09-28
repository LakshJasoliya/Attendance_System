# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk
# from tkinter import messagebox
# import mysql.connector
# import cv2
# import os
# import numpy as np
# # import win32com.client

# class Train:
#     # speaker = win32com.client.Dispatch("SAPI.spVoice")
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("Train Data")

#         # Title label
#         title_lbl = Label(self.root, text="PRINT DATASET", font=("times new roman", 32, "bold"), bg="white", fg="red")
#         title_lbl.place(x=0, y=0, width=1530, height=45)

#         # Top image
#         img_top = Image.open(r"college_images\BestFacialRecognition.jpg")
#         img_top = img_top.resize((1530, 325))
#         self.photoimg_top = ImageTk.PhotoImage(img_top)
#         f_lbl_top = Label(self.root, image=self.photoimg_top)
#         f_lbl_top.place(x=0, y=55, width=1530, height=325)

#         # Bottom image
#         img_bottom = Image.open(r"college_images\BestFacialRecognition.jpg")
#         img_bottom = img_bottom.resize((1530, 325))
#         self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
#         f_lbl_bottom = Label(self.root, image=self.photoimg_bottom)
#         f_lbl_bottom.place(x=0, y=440, width=1530, height=325)

#         # Train data button
#         btn_train_data = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2",
#                                 font=("times new roman", 30, "bold"), bg="blue", fg="white")
#         btn_train_data.place(x=0, y=380, width=1530, height=60)

#     def train_classifier(self):
#         data_dir = "data"
#         path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
#         faces = []
#         ids = []

#         for image in path:
#             img = Image.open(image).convert('L')  # Convert to grayscale
#             image_np = np.array(img, 'uint8')
#             id = int(os.path.split(image)[1].split('.')[1])  # Extract ID from filename

#             faces.append(image_np)
#             ids.append(id)
#             cv2.imshow("Training", image_np)
#             cv2.waitKey(1)  # Display each image for a short time

#         ids = np.array(ids)

#         # Train classifier
#         clf = cv2.face.LBPHFaceRecognizer_create()
#         clf.train(faces, ids)
#         clf.write("classifier.xml")  # Save the trained model
#         cv2.destroyAllWindows()

#         messagebox.showinfo("Result", "Training completed")

# if __name__ == "__main__":
#     root = Tk()
#     obj = Train(root)
#     root.mainloop()

# gif ui ================================================================================================================================================

# import tkinter as tk
# from tkinter import ttk
# from tkinter import *
# from PIL import Image, ImageTk, ImageSequence
# import threading

# class StudentManagementSystem:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Student Management System")
#         self.root.geometry("1530x790+0+0")
        
#         # Animated Background
#         self.bg_img = Image.open(r"college_images/animated_background.gif")
#         self.frames = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(self.bg_img)]
#         self.frame_index = 0
        
#         self.bg_label = Label(self.root, image=self.frames[self.frame_index])
#         self.bg_label.place(x=0, y=0, width=1530, height=800)
#         self.animate()
        
#         # Title Label
#         title_lbl = Label(self.bg_label, text="STUDENT MANAGEMENT SYSTEM", font=("Times New Roman", 32, "bold"), bg="#04293A", fg="white")
#         title_lbl.place(x=0, y=0, width=1530, height=50)
        
#         # Main Frame
#         main_frame = Frame(self.bg_label, bd=2, bg="white")
#         main_frame.place(x=40, y=80, width=1440, height=650)
        
#         # Left Frame
#         left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("Arial", 12, "bold"))
#         left_frame.place(x=10, y=10, width=700, height=580)
        
#         img_left = Image.open(r"college_images/AdobeStock_303989091.jpeg")
#         img_left = img_left.resize((700, 130))
#         self.photoimg_left = ImageTk.PhotoImage(img_left)
        
#         f_lbl2 = Label(left_frame, image=self.photoimg_left)
#         f_lbl2.place(x=3, y=-1, width=700, height=130)
        
#         # Student Course Information
#         c_left_frame = LabelFrame(left_frame, bd=2, bg="white", relief=RIDGE, text="Course Information", font=("Arial", 10, "bold"))
#         c_left_frame.place(x=5, y=140, width=680, height=150)
        
#         # Department
#         dep_label = Label(c_left_frame, text="Department", font=("Arial", 10, "bold"), bg="white")
#         dep_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        
#         dep_combo = ttk.Combobox(c_left_frame, width=20, state="readonly", font=("Arial", 10))
#         dep_combo["values"] = ("Select Department", "CSE", "IT", "ECE", "Civil", "Mech")
#         dep_combo.current(0)
#         dep_combo.grid(row=0, column=1, padx=10, pady=5, sticky=W)
        
#         # Course
#         course_label = Label(c_left_frame, text="Course", font=("Arial", 10, "bold"), bg="white")
#         course_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        
#         course_combo = ttk.Combobox(c_left_frame, width=20, state="readonly", font=("Arial", 10))
#         course_combo["values"] = ("Select Course", "B.Tech", "M.Tech", "Diploma", "MBA")
#         course_combo.current(0)
#         course_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        
#         # Right Frame
#         right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Records", font=("Arial", 12, "bold"))
#         right_frame.place(x=720, y=10, width=700, height=580)
        
#         # Table Frame
#         table_frame = Frame(right_frame, bd=2, relief=RIDGE)
#         table_frame.place(x=0, y=260, width=680, height=300)
        
#         scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
#         scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        
#         self.student_table = ttk.Treeview(table_frame, columns=("dep", "course", "year", "sem", "id", "name", "roll", "gender", "dob", "email", "phone", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        
#         scroll_x.pack(side=BOTTOM, fill=X)
#         scroll_y.pack(side=RIGHT, fill=Y)
#         scroll_x.config(command=self.student_table.xview)
#         scroll_y.config(command=self.student_table.yview)
        
#         self.student_table.pack(fill=BOTH, expand=1)
        
#         # Exit Button
#         exit_btn = Button(self.root, text="Exit", command=self.root.quit, font=("Arial", 12, "bold"), bg="red", fg="white", width=10)
#         exit_btn.place(x=1400, y=750)
    
#     def animate(self):
#         self.frame_index = (self.frame_index + 1) % len(self.frames)
#         self.bg_label.config(image=self.frames[self.frame_index])
#         self.root.after(100, self.animate)

# if __name__ == "__main__":
#     root = tk.Tk()
#     obj = StudentManagementSystem(root)
#     root.mainloop()
import tkinter as tk
from tkinter import ttk, messagebox
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x500")
        self.root.title("Train Data")
        self.root.configure(bg="#2C3E50")
        
        # Title label
        title_lbl = tk.Label(self.root, text="TRAIN DATASET", font=("Arial", 20, "bold"), bg="#2980B9", fg="white")
        title_lbl.pack(fill=tk.X, pady=10)
        
        # Train data button
        btn_train_data = tk.Button(self.root, text="START TRAINING", command=self.train_classifier, cursor="hand2",
                                   font=("Arial", 15, "bold"), bg="#E74C3C", fg="white", padx=20, pady=10)
        btn_train_data.pack(pady=50)
        
        # Status label
        self.status_label = tk.Label(self.root, text="", font=("Arial", 12, "bold"), bg="#2C3E50", fg="white")
        self.status_label.pack()

    def train_classifier(self):
        self.status_label.config(text="Training in progress...")
        self.root.update_idletasks()
        
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []
        
        for image in path:
            img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
            id = int(os.path.split(image)[1].split('.')[1])
            faces.append(img)
            ids.append(id)
        
        ids = np.array(ids)
        
        # Train classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        
        self.status_label.config(text="Training Completed Successfully!")
        messagebox.showinfo("Result", "Training completed successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    obj = Train(root)
    root.mainloop()