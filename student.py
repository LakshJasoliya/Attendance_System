from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
# import win32com.client

class Student:
    # speaker = win32com.client.Dispatch("SAPI.spVoice")
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("student")
        self.root.wm_iconbitmap("face.ico")

        # =========================variabels==================
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
       
        
        # Background image
        img3 = Image.open(r"college_images/BestFacialRecognition.jpg")
        img3 = img3.resize((1530, 710))
        self.photoimg3 = ImageTk.PhotoImage(img3)

        f_lbl3 = Label(self.root, image=self.photoimg3)
        f_lbl3.place(x=0, y=0, width=1530, height=800)

        # add title
        tital_lbl=Label(f_lbl3,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",32,"bold"),bg="white",fg="red")
        tital_lbl.place(x=0,y=0,width=1530,height=45)

        #frame

        main_frame=Frame(f_lbl3,bd=2)
        main_frame.place(x=40,y=80,width=1500,height=650)

        #left frame

        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="student Details")
        left_frame.place(x=10,y=10,width=680,height=580)

        #add image in left frame
        img_left = Image.open(r"college_images/AdobeStock_303989091.jpeg")
        img_left = img_left.resize((720, 130))  # Fixed to use img2 instead of img
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl2 = Label(left_frame, image=self.photoimg_left)
        f_lbl2.place(x=3, y=-1, width=720, height=130)


        #current cource
        c_left_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="student Details")
        c_left_frame.place(x=5,y=130,width=720,height=150)
        #Department
        dep_label=Label(c_left_frame,text="Department")
        dep_label.grid(row=0,column=0)

        dep_combo=ttk.Combobox(c_left_frame,textvariable=self.var_dep,width=17,state="readonly")
        dep_combo["values"]=("Select Department Code","71","91","31","51")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        # dep_combo=Entry(c_left_frame,textvariable=self.var_dep,width=17)
        # dep_combo.grid(row=0,column=1,padx=2,pady=10)


        
        #course
        course_label=Label(c_left_frame,text="Course")
        course_label.grid(row=0,column=2)

        course_combo=ttk.Combobox(c_left_frame,textvariable=self.var_course,width=17,state="readonly")
        course_combo["values"]=("select Course","BE","ME","DIPL","M.PHARM","B.PHARM")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10)

        #year

        year_label=Label(c_left_frame,text="year")
        year_label.grid(row=1,column=0)

        year_combo=ttk.Combobox(c_left_frame,textvariable=self.var_year,width=17,state="readonly")
        year_combo["values"]=("select year","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        semester_label=Label(c_left_frame,text="Semester")
        semester_label.grid(row=1,column=2,sticky=W)

        semester_combo=ttk.Combobox(c_left_frame,textvariable=self.var_semester,width=17,state="readonly")
        semester_combo["values"]=("Select year","SEM 1","SEM 2","SEM 3","SEM 4","SEM 5","SEM 6","SEM 7","SEM 8")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Department Code
        semester=Label(c_left_frame,text="Department Code :")
        semester.grid(row=0,column=4,sticky=W)
        semester_l=Label(c_left_frame,text="CSE:31 CIVIL:71 ",font=("Arial",7))
        semester_l.grid(row=1,column=4)
        semester_l=Label(c_left_frame,text="EC:51 ")
        semester_l.grid(row=0,column=5)
        semester_l=Label(c_left_frame,text="Electrical:51",font=("Arial",7))
        semester_l.grid(row=1,column=5)




        #Class student info
        calss_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="student Details")
        calss_student_frame.place(x=5,y=230,width=720,height=300)

        #student id
        student_id_label=Label(calss_student_frame,text="Student ID:")
        student_id_label.grid(row=0,column=0,sticky=W)

        student_entry=Entry(calss_student_frame,textvariable=self.var_std_id,width=20)
        student_entry.grid(row=0,column=1,sticky=W)

        #class div
        student_div_label=Label(calss_student_frame,text="Class Div:")
        student_div_label.grid(row=1,column=0,sticky=W)

        # studentdiv_entry=Entry(calss_student_frame,textvariable=self.var_div,width=20)
        # studentdiv_entry.grid(row=1,column=1,sticky=W)

        div_combo=ttk.Combobox(calss_student_frame,textvariable=self.var_div,width=17,state="readonly")
        div_combo["values"]=("A","B","C")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #Gender
        student_gender_label=Label(calss_student_frame,text="Gender:")
        student_gender_label.grid(row=2,column=0,sticky=W)

        # studentgender_entry=Entry(calss_student_frame,textvariable=self.var_gender,width=20)
        # studentgender_entry.grid(row=2,column=1,sticky=W)

        gender_combo=ttk.Combobox(calss_student_frame,textvariable=self.var_gender,width=17,state="readonly")
        gender_combo["values"]=("Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        #Email
        student_email_label=Label(calss_student_frame,text="EMAIL :")
        student_email_label.grid(row=3,column=0,sticky=W)

        studentemail_entry=Entry(calss_student_frame,textvariable=self.var_email,width=20)
        studentemail_entry.grid(row=3,column=1,sticky=W)

         #Adderess
        student_Address_label=Label(calss_student_frame,text="Adress :")
        student_Address_label.grid(row=4,column=0,sticky=W)

        studentadress_entry=Entry(calss_student_frame,textvariable=self.var_address,width=20)
        studentadress_entry.grid(row=4,column=1,sticky=W)

        #student name
        student_name_label=Label(calss_student_frame,text="Student Name :")
        student_name_label.grid(row=0,column=2,sticky=W,padx=10,pady=5)

        studentname_entry=Entry(calss_student_frame,textvariable=self.var_std_name,width=20)
        studentname_entry.grid(row=0,column=3,sticky=W,padx=10,pady=5)

         #Roll no
        student_roll_label=Label(calss_student_frame,text="Roll No :")
        student_roll_label.grid(row=1,column=2,sticky=W,padx=10,pady=5)

        studentroll_entry=Entry(calss_student_frame,textvariable=self.var_roll,width=20)
        studentroll_entry.grid(row=1,column=3,sticky=W,padx=10,pady=5)

        #DOB
        student_Dob_label=Label(calss_student_frame,text="DOB:")
        student_Dob_label.grid(row=2,column=2,sticky=W,padx=10,pady=5)

        studentDob_entry=Entry(calss_student_frame,textvariable=self.var_dob,width=20)
        studentDob_entry.grid(row=2,column=3,sticky=W,padx=10,pady=5)
        
        #Phone
        student_Phone_label=Label(calss_student_frame,text="Phone No:")
        student_Phone_label.grid(row=3,column=2,sticky=W,padx=10,pady=5)

        studentPhone_entry=Entry(calss_student_frame,textvariable=self.var_phone,width=20)
        studentPhone_entry.grid(row=3,column=3,sticky=W,padx=10,pady=5)

        #Teacher
        student_Teacher_label=Label(calss_student_frame,text="Teacher Name")
        student_Teacher_label.grid(row=4,column=2,sticky=W,padx=10,pady=5)

        studentTeacher_entry=Entry(calss_student_frame,textvariable=self.var_teacher,width=20)
        studentTeacher_entry.grid(row=4,column=3,sticky=W,padx=10,pady=5)

        #radio button
        self.var_radio1=StringVar()
        radio_1=ttk.Radiobutton(calss_student_frame,variable=self.var_radio1,text="take photo Sample",value="yes")
        radio_1.grid(row=5,column=0)

        #radio button
        self.var_radio2=StringVar()
        radio_1=ttk.Radiobutton(calss_student_frame,variable=self.var_radio1,text="No Photo Sample",value="no")
        radio_1.grid(row=5,column=2)

        #frame button

        button_frame=Frame(calss_student_frame,bd=2,relief=RIDGE)
        button_frame.place(x=0,y=230,width=650,height=50)

        #button for save

        btn_save=Button(button_frame,command=self.add_data,text="Save Data")
        btn_save.grid(row=0,column=0,padx=4)

        #button update
        btn_update=Button(button_frame,command=self.update_data,text="update Data")
        btn_update.grid(row=0,column=4,padx=4)

        #button delete
        btn_delete=Button(button_frame,command=self.delete_data,text="Delete Data")
        btn_delete.grid(row=0,column=2,padx=4)

        #button Reset
        btn_reset=Button(button_frame,command=self.reset_data,text="reset Data")
        btn_reset.grid(row=0,column=6,padx=4)

         #button Take photo
        btn_takephoto=Button(button_frame,command=self.generate_dataset,text="Take Photo Sample")
        btn_takephoto.grid(row=0,column=8,padx=4)

         #button Update photo Sample
        btn_updatephoto=Button(button_frame,text="Update Photo Sample")
        btn_updatephoto.grid(row=0,column=10,padx=4)




        #right frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="student Details")
        right_frame.place(x=680,y=10,width=690,height=580)
        
        
        #add image in Right frame
        img_right = Image.open(r"college_images/AdobeStock_303989091.jpeg")
        img_right = img_right.resize((720, 130))  # Fixed to use img2 instead of img
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl2 = Label(right_frame, image=self.photoimg_right)
        f_lbl2.place(x=3, y=-1, width=720, height=130)

        # ===search system=====

        Search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System")
        Search_frame.place(x=5,y=135,width=690,height=100)

        #lable Search by
        search_lable = Label(Search_frame,text="Search By:-")
        search_lable.grid(row=0,column=0)
        
        #combobox
       

        search_combo=ttk.Combobox(Search_frame,width=17,state="readonly")
        search_combo["values"]=("select","Roll_no","Phone_no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        #entry
        search_entry=Entry(Search_frame,width=20)
        search_entry.grid(row=0,column=2,sticky=W,padx=10,pady=5)

         #button search
        btn_search=Button(Search_frame,text="Take Photo Sample")
        btn_search.grid(row=0,column=3,padx=12)

         #button Show All
        btn_show=Button(Search_frame,text="Update Photo Sample")
        btn_show.grid(row=0,column=4,padx=12)

        #table frame===========================================================

        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=0,y=260,width=680,height=300)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        #add column for scrollbar
        self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        #place of scrollbar
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        #show heading
        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="StudentId")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="rollno")
        self.student_table.heading("gender",text="gender")
        self.student_table.heading("dob",text="dob")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo Status")

        self.student_table["show"]="headings"
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        
        self.student_table.column("div",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=100)
        
        self.student_table.pack(fill=BOTH,expand=1)

        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
# =====================================function declaration===================================
   

    def add_data(self):
    # Validate inputs
        if self.var_dep.get() == "select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        conn = None  # Initialize conn here
        try:
            student_id = int(self.var_std_id.get())  # Convert to int

            # Database connection
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognizer")
            my_cursor = conn.cursor()

            my_cursor.execute("INSERT INTO student1 (dep, Course, Year, Semester, Student_id, Name, Division, roll, Gender, DOB, Email, Phone, Address, Teacher, PhotoSample) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
            str(self.var_dep.get()),  # Ensure this is a string
            self.var_course.get(),
            self.var_year.get(),
            self.var_semester.get(),    
            student_id,  # Assuming this is an integer
            self.var_std_name.get(),
            self.var_div.get(),
            self.var_roll.get(),
            self.var_gender.get(),
            self.var_dob.get(),
            self.var_email.get(),
            self.var_phone.get(),
            self.var_address.get(),
            self.var_teacher.get(),
            self.var_radio1.get()
        ))


            conn.commit()
            self.fetch_data()
            messagebox.showinfo("Success", "Data added successfully", parent=self.root)

        except ValueError as ve:
            messagebox.showerror("Error", f"Value error: {str(ve)}", parent=self.root)
        except mysql.connector.Error as db_error:
            messagebox.showerror("Database Error", f"Error: {str(db_error)}", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Unexpected error: {str(e)}", parent=self.root)
        finally:
            if conn:
                conn.close()



    #    ===============================Fetch Data=====================================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT dep, Course, Year, Semester, Student_id, Name, Division, roll, Gender, DOB, Email, Phone, Address, Teacher, PhotoSample FROM student1") 
        data=my_cursor.fetchall()

        if len(data)!=0:
              self.student_table.delete(*self.student_table.get_children())                      
              for i in data:
                    self.student_table.insert("",END,values=i)
                    conn.commit()
        conn.close()
        #=============================get cursor for update  data=================================================================
    def get_cursor(self,event=""):
          cursor_focus=self.student_table.focus()
          content=self.student_table.item(cursor_focus)
          data=content["values"]
                
          self.var_dep.set(data[0]),
          self.var_course.set(data[1]),
          self.var_year.set(data[2]),
          self.var_semester.set(data[3]),
          self.var_std_id.set(data[4]),
          self.var_std_name.set(data[5]),
          self.var_div.set(data[6]),
          self.var_roll.set(data[7]),
          self.var_gender.set(data[8]),
          self.var_dob.set(data[9]),
          self.var_email.set(data[10]),
          self.var_phone.set(data[11]),
          self.var_address.set(data[12]),
          self.var_teacher.set(data[13]),
          self.var_radio1.set(data[14])

   

# ++++++++++++++++++++++++update field or data ==============================
    def update_data(self):
            # Check if all required fields are filled
            if self.var_dep.get() == "select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
                messagebox.showerror("Error", "All fields are required", parent=self.root)
            else:
                try:
                    # Confirm update action
                    update = messagebox.askyesnocancel("Update", "Do you want to update?", parent=self.root)
                    if update:  # User confirmed update
                        conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognizer")
                        my_cursor = conn.cursor()
                        my_cursor.execute("""
                            UPDATE student1 SET 
                                dep=%s, 
                                Course=%s, 
                                Year=%s, 
                                Semester=%s, 
                                Name=%s, 
                                Division=%s, 
                                roll=%s, 
                                Gender=%s, 
                                DOB=%s, 
                                Email=%s, 
                                Phone=%s, 
                                Address=%s, 
                                Teacher=%s, 
                                PhotoSample=%s 
                            WHERE Student_id=%s
                        """, (
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_std_name.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get()
                        ))

                        # Commit changes and inform user
                        conn.commit()
                        messagebox.showinfo("Success", "Student Detail Updated", parent=self.root)
                        self.fetch_data()  # Refresh data
                        conn.close()
                    elif update is False:  # User canceled update
                        return
                except Exception as es:
                    messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


    # ==============================Delete function==================================

    def delete_data(self):
        if self.var_std_id.get()=="":
              messagebox.showerror("error","id must be required",parent=self.root)
        else:
              try:
                    delete=messagebox.askokcancel("student delete","do you want to delete this student",parent=self.root)
                    if delete>0:
                          conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognizer")
                          my_cursor = conn.cursor()
                          sql="delete from student1 where Student_id=%s"
                          val=(self.var_std_id.get(),)
                          my_cursor.execute(sql,val)
                    else:
                          if not delete:
                                return
                    conn.commit()
                    self.fetch_data()
                    conn.close()      
                    messagebox.showinfo("delete","successfuly deleted student details",parent=self.root)
              except Exception as es:
                    messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)                    
                          
# ========================RESET function=============================
    def reset_data(self):
          self.var_dep.set("Select Department")
          self.var_course.set("Select Course")
          self.var_year.set("Select Yaar")
          self.var_semester.set("Select Sem")
          self.var_std_id.set("")
          self.var_std_name.set("")
          self.var_div.set("Select Division")
          self.var_roll.set("")
          self.var_gender.set("Select Gender")
          self.var_dob.set("")
          self.var_email.set("")
          self.var_phone.set("")
          self.var_address.set("")
          self.var_teacher.set("")
          self.var_radio1.set("")
        
        # ========================Generate data set take photo sample ================================
    
    def generate_dataset(self):
    # Validate inputs
        if self.var_dep.get() == "select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        try:
            # Connect to the database
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognizer")
            my_cursor = conn.cursor()

            # Fetch student record from the database
            student_id = self.var_std_id.get()
            my_cursor.execute("SELECT * FROM student1 WHERE Student_id=%s", (student_id,))
            student = my_cursor.fetchone()

            if not student:
                messagebox.showerror("Error", "Student not found in the database", parent=self.root)
                return

            # Update student record in the database
            my_cursor.execute(
                """
                UPDATE student1 SET 
                    dep=%s, 
                    Course=%s, 
                    Year=%s, 
                    Semester=%s, 
                    Name=%s, 
                    Division=%s, 
                    roll=%s, 
                    Gender=%s, 
                    DOB=%s, 
                    Email=%s, 
                    Phone=%s, 
                    Address=%s, 
                    Teacher=%s, 
                    PhotoSample=%s 
                WHERE Student_id=%s
                """,
                (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    student_id
                )
            )
            conn.commit()

            # Load face classifier
            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            # Ensure the data folder exists
            os.makedirs("data", exist_ok=True)

            # Initialize webcam
            cap = cv2.VideoCapture(0)
            img_id = 0

            while True:
                ret, my_frame = cap.read()
                if not ret:
                    raise Exception("Failed to capture image from webcam.")

                # Convert to grayscale and detect faces
                gray_frame = cv2.cvtColor(my_frame, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5)

                for (x, y, w, h) in faces:
                    face_cropped_image = my_frame[y:y+h, x:x+w]
                    img_id += 1

                    # Resize and save the cropped face image in the data folder
                    face_resized = cv2.resize(face_cropped_image, (450, 450))
                    file_name_path = os.path.join("data", f"user.{student_id}.{img_id}.jpg")
                    cv2.imwrite(file_name_path, face_resized)

                    # Display the image ID on the cropped face
                    text = str(img_id)
                    position = (10, 30)
                    color = (0, 255, 0)
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    font_scale = 1
                    thickness = 2

                    cv2.putText(face_resized, text, position, font, font_scale, color, thickness)
                    cv2.imshow("Cropped Face", face_resized)

                # Stop loop if Enter key is pressed or after 100 images
                if cv2.waitKey(1) == 13 or img_id >= 50:
                    break

            cap.release()
            cv2.destroyAllWindows()

            # Optionally, refresh UI data
            self.fetch_data()
            self.reset_data()

        except Exception as e:
            messagebox.showerror("Error", str(e), parent=self.root)

        finally:
            if conn:
                conn.close()
if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()