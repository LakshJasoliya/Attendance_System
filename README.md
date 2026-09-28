<div align="center">

# 🎓 Attendance System Using Face Recognition

**Mark student attendance automatically, just by looking at the camera.**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-Face%20Recognition-5C3EE8?logo=opencv&logoColor=white)
![CustomTkinter](https://img.shields.io/badge/UI-CustomTkinter-1f6aa5)
![MySQL](https://img.shields.io/badge/Database-MySQL%20(XAMPP)-4479A1?logo=mysql&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-CSV%20Reports-150458?logo=pandas&logoColor=white)

</div>

---

## 📖 About the Project

Taking attendance in class by calling names or passing a sheet of paper wastes time, and it is easy to cheat (one student signing for a friend).

This project solves that problem. **A student just sits in front of the camera, and the computer recognizes their face and marks them present.** No paper, no roll call, no proxy attendance.

I integrated, debugged and modernized this desktop application as an academic project. It uses machine learning to learn each student's face, then recognizes them in real time and saves the attendance in a database. The teacher can also download the attendance as a spreadsheet (CSV) file.

---

## 🧑‍🏫 How It Works ?

1. **Register** – The student enters their details: name, enrollment number, branch, teacher name, date of birth, year and semester.
2. **Face Photo Capture** – The camera takes about **50 photos of the student's face in 1–2 minutes**. Many photos from different angles help the system recognize the face accurately later.
3. **Training** – The computer studies all the saved photos and learns what each student looks like.
4. **Attendance** – When the student appears in front of the camera, the system recognizes them and **automatically counts their attendance**.
5. **Reports** – Attendance is saved in a database and can be downloaded as a CSV file (opens in Excel).

```
Enter Details  →  Capture ~50 Face Photos  →  Train the Model  →  Camera Recognizes Face  →  Attendance Saved ✅
```

---

## ✨ Features

- 🧾 Student registration form (name, enrollment no., branch, teacher, DOB, year, semester)
- 📸 Automatic face sample collection (~50 images per student)
- 🧠 Face recognition using the **LBPH** machine learning algorithm
- 🎥 Real-time face detection using **Haar Cascades**
- 🗄️ Attendance stored in a **MySQL** database
- 📥 Downloadable attendance reports in **CSV** format
- 🖥️ Modern, clean desktop interface built with **CustomTkinter**

---

## 🛠️ Tools & Technologies

| Technology | Used For |
|---|---|
| **Python** | Main programming language |
| **OpenCV** | Face detection (Haar Cascades) and face recognition (LBPH Recognizer) |
| **CustomTkinter** | Modern desktop user interface |
| **MySQL (XAMPP)** | Local database to store student and attendance records |
| **Pandas** | Creating and exporting attendance CSV files |

---

## ⚙️ Installation & Setup

### 1. Prerequisites
- [Python 3.8+](https://www.python.org/downloads/)
- [XAMPP](https://www.apachefriends.org/) (for MySQL)
- A working webcam

### 2. Clone the repository
```bash
git clone https://github.com/LakshJasoliya/Attendance_System.git
cd Attendance_System
```

### 3. Install the required libraries
```bash
pip install opencv-contrib-python customtkinter pandas mysql-connector-python pillow numpy
```

### 4. Set up the database
1. Open **XAMPP Control Panel** and start **Apache** and **MySQL**.
2. Open `http://localhost/phpmyadmin` in your browser.
3. Create a new database and import/create the tables used by the project.

### 5. Run the application
```bash
python main.py
```
> Replace `main.py` with the name of your main project file.

---

## 🚀 Usage

1. Launch the app and fill in the student details.
2. Click **Take Photo Samples** and look at the camera until ~50 photos are captured.
3. Click **Train Model** to teach the system the new faces.
4. Click **Take Attendance** and stand in front of the camera.
5. Export the attendance as a CSV file whenever needed.

---

## 🔮 Future Improvements

- Cloud database support
- Email/SMS notification of attendance
- Admin login and multi-teacher dashboard
- Attendance analytics and charts

---

## 👨‍💻 Author

**Laksh Jasoliya**
GitHub: [@LakshJasoliya](https://github.com/LakshJasoliya)

---

<div align="center">

⭐ If you like this project, please give it a star!

</div>
