# from tkinter import *
# from tkinter import ttk
# from PIL import Image, ImageTk
# from tkinter import messagebox
# import mysql.connector
# import cv2
# import os
# import csv
# from tkinter import filedialog
# mydata=[]
# class atd:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1530x790+0+0")
#         self.root.title("HAjari")
#         self.root.wm_iconbitmap("face.ico")

#         # variabels 
#         self.var_id=StringVar()
#         self.var_name=StringVar()
#         self.var_dep=StringVar()
#         self.var_roll=StringVar()
#         self.var_date=StringVar()
#         self.var_Time=StringVar()
#         self.var_att=StringVar()

#      # Create the first frame
#         frame1 = Frame(root, bg="lightblue", bd=2, relief=SOLID)
#         frame1.place(x=10, y=10, width=1000, height=1000)  # Position and size the frame

#         # Add widgets to the first frame
#         label1 = Label(frame1, text="ID",font=("Arial", 14), bg="lightblue")
#         label1.grid(row=0,column=0,padx=10,pady=5)

#         entry1 = Entry(frame1,textvariable=self.var_id, font=("Arial", 12))
#         entry1.grid(row=0,column=1,padx=10,pady=5)
#         # label &&&&&& Entry

#         label2 = Label(frame1, text="ROLL", font=("Arial", 14), bg="lightblue")
#         label2.grid(row=2,column=0,padx=10,pady=5)

#         entry2 = Entry(frame1, textvariable=self.var_roll,font=("Arial", 12))
#         entry2.grid(row=2,column=1,padx=10,pady=5)

#         # label &&&&&& Entry

#         label3 = Label(frame1, text="NAME", font=("Arial", 14), bg="lightblue")
#         label3.grid(row=4,column=0,padx=10,pady=5)

#         entry3 = Entry(frame1, textvariable=self.var_name,font=("Arial", 12))
#         entry3.grid(row=4,column=1,padx=10,pady=5)

#         # label &&&&&& Entry

#         label4 = Label(frame1, text="DEPARTMENT", font=("Arial", 14), bg="lightblue")
#         label4.grid(row=6,column=0,padx=10,pady=5)

#         entry4 = Entry(frame1, textvariable=self.var_dep,font=("Arial", 12))
#         entry4.grid(row=6,column=1,padx=10,pady=5)

#         # label &&&&&& Entry

#         label5 = Label(frame1, text="TIME", font=("Arial", 14), bg="lightblue")
#         label5.grid(row=8,column=0,padx=10,pady=5)

#         entry5 = Entry(frame1, textvariable=self.var_Time,font=("Arial", 12))
#         entry5.grid(row=8,column=1,padx=10,pady=5)

#         # label &&&&&& Entry

#         label6 = Label(frame1, text="DATE", font=("Arial", 14), bg="lightblue")
#         label6.grid(row=10,column=0,padx=10,pady=5)

#         entry6 = Entry(frame1, textvariable=self.var_date,font=("Arial", 12))
#         entry6.grid(row=10,column=1,padx=10,pady=5)


#         # label &&&&&& Entry

        


#         #Gender
#         student_gender_label=Label(frame1,text="Attendenc Status:",font=("Arial", 14), bg="lightblue")
#         student_gender_label.grid(row=14,column=0)

#         # studentgender_entry=Entry(calss_student_frame,textvariable=self.var_gender,width=20)
#         # studentgender_entry.grid(row=2,column=1,sticky=W)

#         gender_combo=ttk.Combobox(frame1,width=17,textvariable=self.var_att,state="readonly",text="Status")
#         gender_combo["values"]=("Present","Absunt")
#         gender_combo.current(0)
#         gender_combo.grid(row=14,column=1,padx=2,pady=10,sticky=W)


#         # buttons frame   

#         button_frame=Frame(frame1,bd=2,relief=RIDGE,bg="lightblue",border=None)
#         button_frame.place(x=0,y=400,width=1000,height=600)

#         # Button FOR CLICKING
#         button1 = Button(button_frame, text="Import CSV", command=self.csv_in,font=("Arial", 12),width=15,bg="blue",fg="yellow")
#         button1.grid(row=0,column=1,padx=50,pady=5)

#         # Button FOR CLICKING
#         button2 = Button(button_frame, text="Export CSV",command=self.export_cvs, font=("Arial", 12),width=15,bg="blue",fg="yellow")
#         button2.grid(row=0,column=2,padx=50,pady=5)

      

#         # Button FOR CLICKING
#         button4 = Button(button_frame, text="Reset", command=self.reset,font=("Arial", 12),width=15,bg="blue",fg="yellow")
#         button4.grid(row=0,column=4,padx=50,pady=5)








#         # Create the second frame
#         frame2 = Frame(root, bg="lightgreen", bd=2, relief=SOLID)
#         frame2.place(x=710, y=10, width=800, height=1000)  # Position and size the frame

#         # Add widgets to the second frame
#         label2 = Label(frame2, text="Frame 2", font=("Arial", 14), bg="lightgreen")
#         label2.pack(pady=10)

#         entry2 = Entry(frame2, font=("Arial", 12))
#         entry2.pack(pady=10)

#         button2 = Button(frame2, text="Submit Frame 2", font=("Arial", 12))
#         button2.pack(pady=5)


#         #table frame===========================================================

#         table_frame=Frame(frame2,bd=2,bg="white",relief=RIDGE)
#         table_frame.place(x=0,y=260,width=680,height=300)

#         scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
#         scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
#         #add column for scrollbar
#         self.Attendence_report=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
#         #place of scrollbar
#         scroll_x.pack(side=BOTTOM,fill=X)
#         scroll_y.pack(side=RIGHT,fill=Y)
#         scroll_x.config(command=self.Attendence_report.xview)
#         scroll_y.config(command=self.Attendence_report.yview)

#         # handeling
#         self.Attendence_report.heading("id",text="ID")
#         self.Attendence_report.heading("roll",text="ENROLLMENT")
#         self.Attendence_report.heading("name",text="NAME")
#         self.Attendence_report.heading("department",text="DEPARTMENT")
#         self.Attendence_report.heading("time",text="TIME")
#         self.Attendence_report.heading("date",text="DATA")
#         self.Attendence_report.heading("attendance",text="ATTENDANCE")

#         self.Attendence_report["show"]="headings"
        

#         # width set

#         self.Attendence_report.column("id",width=100)
#         self.Attendence_report.column("roll",width=100)
#         self.Attendence_report.column("name",width=100)
#         self.Attendence_report.column("department",width=100)
#         self.Attendence_report.column("time",width=100)
#         self.Attendence_report.column("date",width=100)
#         self.Attendence_report.column("attendance",width=100)

#         self.Attendence_report.pack(fill=BOTH,expand=1)

#         self.Attendence_report.bind("<ButtonRelease>",self.get_Cur)
#         # self.fetch_data()
            


#     # IMPORT CSV CODINGGGGGG fetch data
#     def fetch_data(self,rows):
#         self.Attendence_report.delete(*self.Attendence_report.get_children())
#         for i in rows:
#             self.Attendence_report.insert("",END,values=i)

#     def csv_in(self):
#         global mydata
#         mydata.clear()
#         fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Attendence CSV",filetypes=(("CSV File","csv"),("All File","*.*")),parent=self.root)
#         with open(fln) as myfile:
#             csv_r=csv.reader(myfile,delimiter=",")
#             for i in csv_r:
#                 mydata.append(i)
#             self.fetch_data(mydata)

#     # export csv data
#     def export_cvs(self):
#         try:
#             if len(mydata)<1:
#                 messagebox.showerror("Empty set","No Data Found For Expoer",parent=self.root)
#                 return False
#             fln_expo=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Attendence CSV",filetypes=(("CSV File","csv"),("All File","*.*")),parent=self.root)
#             with open(fln_expo,mode="w",newline="") as myfile1:
#                 expo=csv.writer(myfile1,delimiter=",")
#                 for i in mydata:
#                     expo.writerow(i)
#                 messagebox.showinfo("dataEXPORTED","DATA WAS ADDED",parent=self.root)
#         except Exception as sl:
#             messagebox.showerror("Error",f"Due to{str(sl)}",parent=self.root)


#     #  get Cursour
#     def get_Cur(self,cc="empty"):
#         cursur_row=self.Attendence_report.focus()
#         content=self.Attendence_report.item(cursur_row)
#         rows=content['values']
#         self.var_id.set(rows[0])
#         self.var_roll.set(rows[1])
#         self.var_name.set(rows[2])
#         self.var_dep.set(rows[3])
#         self.var_Time.set(rows[4])
#         self.var_date.set(rows[5])
#         self.var_att.set(rows[6])

        
#     # restet filed
#     def reset(self):
#         self.var_id.set("")
#         self.var_roll.set("")
#         self.var_name.set("")
#         self.var_dep.set("")
#         self.var_Time.set("")
#         self.var_date.set("")
#         self.var_att.set("")

    
# if __name__ == "__main__":
#     root = Tk()
#     obj = atd(root)
#     root.mainloop()




from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
# import win32com.client

mydata = []

class atd:
    
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("HAjari")
        self.root.wm_iconbitmap("face.ico")

        # Variables
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_dep = StringVar()
        self.var_roll = StringVar()
        self.var_date = StringVar()
        self.var_Time = StringVar()
        self.var_att = StringVar()
        self.var_image_path = StringVar()

        # Frame 1
        frame1 = Frame(root, bg="lightblue", bd=2, relief=SOLID)
        frame1.place(x=10, y=10, width=1000, height=1000)

        # Add widgets to Frame 1
        Label(frame1, text="ID", font=("Arial", 14), bg="lightblue").grid(row=0, column=0, padx=10, pady=5)
        Entry(frame1, textvariable=self.var_id, font=("Arial", 12)).grid(row=0, column=1, padx=10, pady=5)

        Label(frame1, text="ROLL", font=("Arial", 14), bg="lightblue").grid(row=2, column=0, padx=10, pady=5)
        Entry(frame1, textvariable=self.var_roll, font=("Arial", 12)).grid(row=2, column=1, padx=10, pady=5)

        Label(frame1, text="NAME", font=("Arial", 14), bg="lightblue").grid(row=4, column=0, padx=10, pady=5)
        Entry(frame1, textvariable=self.var_name, font=("Arial", 12)).grid(row=4, column=1, padx=10, pady=5)

        Label(frame1, text="DEPARTMENT", font=("Arial", 14), bg="lightblue").grid(row=6, column=0, padx=10, pady=5)
        Entry(frame1, textvariable=self.var_dep, font=("Arial", 12)).grid(row=6, column=1, padx=10, pady=5)

        Label(frame1, text="TIME", font=("Arial", 14), bg="lightblue").grid(row=8, column=0, padx=10, pady=5)
        Entry(frame1, textvariable=self.var_Time, font=("Arial", 12)).grid(row=8, column=1, padx=10, pady=5)

        Label(frame1, text="DATE", font=("Arial", 14), bg="lightblue").grid(row=10, column=0, padx=10, pady=5)
        Entry(frame1, textvariable=self.var_date, font=("Arial", 12)).grid(row=10, column=1, padx=10, pady=5)

        Label(frame1, text="Attendance Status:", font=("Arial", 14), bg="lightblue").grid(row=12, column=0, padx=10, pady=5)
        gender_combo = ttk.Combobox(frame1, width=17, textvariable=self.var_att, state="readonly")
        gender_combo["values"] = ("Present", "Absent")
        gender_combo.current(0)
        gender_combo.grid(row=12, column=1, padx=10, pady=5)

        Label(frame1, text="Image Path:", font=("Arial", 14), bg="lightblue").grid(row=14, column=0, padx=10, pady=5)
        Entry(frame1, textvariable=self.var_image_path, font=("Arial", 12)).grid(row=14, column=1, padx=10, pady=5)
        Button(frame1, text="Browse Image", command=self.browse_image, font=("Arial", 12), bg="blue", fg="yellow").grid(row=14, column=2, padx=10, pady=5)

        # Button Frame
        button_frame = Frame(frame1, bd=2, relief=RIDGE, bg="lightblue")
        button_frame.place(x=0, y=400, width=1000, height=600)

        Button(button_frame, text="Import CSV", command=self.csv_in, font=("Arial", 12), width=15, bg="blue", fg="yellow").grid(row=0, column=1, padx=50, pady=5)
        Button(button_frame, text="Export CSV", command=self.export_cvs, font=("Arial", 12), width=15, bg="blue", fg="yellow").grid(row=0, column=2, padx=50, pady=5)
        Button(button_frame, text="Reset", command=self.reset, font=("Arial", 12), width=15, bg="blue", fg="yellow").grid(row=0, column=3, padx=50, pady=5)

        # Frame 2
        frame2 = Frame(root, bg="lightgreen", bd=2, relief=SOLID)
        frame2.place(x=710, y=10, width=800, height=1000)

        table_frame = Frame(frame2, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=0, y=260, width=680, height=300)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.Attendence_report = ttk.Treeview(
            table_frame,
            columns=("id", "roll", "name", "department", "time", "date", "attendance", "image"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Attendence_report.xview)
        scroll_y.config(command=self.Attendence_report.yview)

        self.Attendence_report.heading("id", text="ID")
        self.Attendence_report.heading("roll", text="ROLL")
        self.Attendence_report.heading("name", text="NAME")
        self.Attendence_report.heading("department", text="DEPARTMENT")
        self.Attendence_report.heading("time", text="TIME")
        self.Attendence_report.heading("date", text="DATE")
        self.Attendence_report.heading("attendance", text="ATTENDANCE")
        self.Attendence_report.heading("image", text="IMAGE PATH")
        self.Attendence_report["show"] = "headings"

        self.Attendence_report.pack(fill=BOTH, expand=1)
        self.Attendence_report.bind("<ButtonRelease>", self.get_Cur)

    def browse_image(self):
        filename = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Select Image File",
            filetypes=(("Image Files", "*.png;*.jpg;*.jpeg;*.bmp"), ("All Files", "*.*")),
        )
        self.var_image_path.set(filename)

    def fetch_data(self, rows):
        self.Attendence_report.delete(*self.Attendence_report.get_children())
        for i in rows:
            self.Attendence_report.insert("", END, values=i)

    def csv_in(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Open CSV",
            filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")),
        )
        with open(fln) as myfile:
            csv_r = csv.reader(myfile, delimiter=",")
            for i in csv_r:
                mydata.append(i)
            self.fetch_data(mydata)

    def export_cvs(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("Error", "No data found to export!", parent=self.root)
                return False
            fln_expo = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Save CSV",
                filetypes=(("CSV Files", "*.csv"), ("All Files", "*.*")),
            )
            with open(fln_expo, mode="w", newline="") as myfile1:
                expo = csv.writer(myfile1, delimiter=",")
                for i in mydata:
                    expo.writerow(i)
                messagebox.showinfo("Export Successful", "Data exported successfully.", parent=self.root)
        except Exception as sl:
            messagebox.showerror("Error", f"Due to: {str(sl)}", parent=self.root)

    def get_Cur(self, event=""):
        cursor_row = self.Attendence_report.focus()
        content = self.Attendence_report.item(cursor_row)
        rows = content["values"]
        if rows:
            self.var_id.set(rows[0])
            self.var_roll.set(rows[1])
            self.var_name.set(rows[2])
            self.var_dep.set(rows[3])
            self.var_Time.set(rows[4])
            self.var_date.set(rows[5])
            self.var_att.set(rows[6])
            self.var_image_path.set(rows[7])

    def reset(self):
        self.var_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_Time.set("")
        self.var_date.set("")
        self.var_att.set("")
        self.var_image_path.set("")

if __name__ == "__main__":
    root = Tk()
    obj = atd(root)
    root.mainloop()
