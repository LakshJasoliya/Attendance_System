
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector
import cv2
from datetime import datetime
# import win32com.client
import os
# speaker = win32com.client.Dispatch("SAPI.spVoice")
class f_d:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")

        # Title label
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 32, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open(r"college_images/face_detector1.jpg")
        img_top = img_top.resize((650, 700))
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl_top = Label(self.root, image=self.photoimg_top)
        f_lbl_top.place(x=0, y=55, width=650, height=700)

        img_side = Image.open(r"college_images/clock.jpg")
        img_side = img_side.resize((900, 700))
        self.photoimg_side = ImageTk.PhotoImage(img_side)
        f_lbl_side = Label(self.root, image=self.photoimg_side)
        f_lbl_side.place(x=650, y=55, width=900, height=700)

        btn_face_recognition = Button(f_lbl_side, text="Face Recognition", cursor="hand2", command=self.face_recog,
                                       font=("times new roman", 18, "bold"), bg="blue", fg="white")
        btn_face_recognition.place(x=0, y=300, width=200, height=40)


        # MARK ATTENDENCE IN CSV FILE FOR THE MARK ATTTTT================================================================

    def mark_attend(self, roll, name, dep, face_image):
    # Define directory for attendance photos
        photo_dir = "attendance_photos"
        if not os.path.exists(photo_dir):
            os.makedirs(photo_dir)
        
        # Save the face image with a unique filename
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        photo_filename = f"{photo_dir}/{roll}_{timestamp}.jpg"
        cv2.imwrite(photo_filename, face_image)

        # Ensure the attendance directory exists
        
        attendance_dir = "attendance"
        if not os.path.exists(attendance_dir):
            os.makedirs(attendance_dir)

        # Ensure the present.csv file exists, create if necessary
        current_date=datetime.now().strftime("%Y-%m-%d")
        attendance_file=f"{attendance_dir}/attendance_{current_date}.csv"
        if not os.path.exists(attendance_file):
            with open(attendance_file, "w", newline="\n") as f:
                # Write headers if the file is created
                f.write("Attendance_id,Roll,Name,Department,Time,Date,Status,Photo\n")
        
        # Open file in read-write mode ("r+")
        with open(attendance_file, "r+", newline="\n") as f:
            my_data = f.readlines()
            roll_list = [line.split(",")[1].strip() for line in my_data]  # Adjust index for roll (2nd column)
            
            if roll not in roll_list:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtstring = now.strftime("%H:%M:%S")
                
                # Determine the new attendance_id
                attendance_id = len(my_data) + 1 if my_data else 1
                
                # Ensure proper newline formatting
                if not my_data or my_data[-1].endswith("\n"):
                    f.write(f"{attendance_id},{roll},{name},{dep},{dtstring},{d1},Present,{photo_filename}\n")
                else:
                    f.write(f"\n{attendance_id},{roll},{name},{dep},{dtstring},{d1},Present,{photo_filename}")





    # =========================== Database Query ============================
    def query_database(self, student_id):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognizer")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT Name, roll, dep FROM student1 WHERE Student_id=%s", (student_id,))
            result = my_cursor.fetchone()
            return {"name": result[0], "roll": result[1], "dep": result[2]} if result else None
        except mysql.connector.Error as err:
            print(f"Database error: {err}")
            return None
        finally:
            if conn:
                conn.close()

   # ======================== Draw Boundary & Recognize ====================    COMPLETE WORK CODE AND THE PRECTICE THE NEW CODE
    def draw_boundary(self, img, classifier, scaleFactor, minNeighbors, color, clf):
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
        
        for (x, y, w, h) in features:
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
            id, predict = clf.predict(gray_image[y:y + h, x:x + w])
            confidence = int((100 * (1 - predict / 300)))

            if confidence >= 80:  # Face recognized with sufficient confidence
                details = self.query_database(id)
                if details:
                    roll, name, dep = details["roll"], details["name"], details["dep"]
                    cv2.putText(img, f"Roll: {roll}", (x, y - 50), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)                 
                    cv2.putText(img, f"Name: {name}", (x, y - 25), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)                    
                    cv2.putText(img, f"Dep: {dep}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)
                    

                    # Pass the cropped face image (face region) to mark_attend
                    face_image = img[y:y + h, x:x + w]
                    self.mark_attend(roll, name, dep, face_image)

            else:  # Face not recognized
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                cv2.putText(img, "UNKNOWN FACE", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 2)

        return img


    # ============================== Face Recognition =======================
    def face_recog(self):
        facecascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        videocap = cv2.VideoCapture(0)
        if not videocap.isOpened():
            print("Error: Could not open video.")
            return

        while True:
            ret, img = videocap.read()
            if not ret:
                print("Failed to capture image.")
                break

            img = self.draw_boundary(img, facecascade, 1.1, 10, (0, 255, 0), clf)
            cv2.imshow("WELCOME TO FACE RECOGNITION", img)

            if cv2.waitKey(1) == 27:  # ESC key to stop
                break

        videocap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = f_d(root)
    root.mainloop()
