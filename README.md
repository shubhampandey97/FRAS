## ✅ `README.md`

```markdown
# Face Recognition Attendance System 🧑‍🎓📸

A desktop-based **Face Recognition Attendance System** built using Python, OpenCV, Dlib, Tkinter, and MySQL. It automates attendance marking using real-time face detection and recognition through a webcam.

---

## 🔧 Technologies Used

- **Python 3.10**
- **OpenCV** (image processing, face detection)
- **Dlib / Haarcascade** (face detection & recognition)
- **Tkinter** (Python GUI)
- **MySQL** (student & attendance data)
- **Pillow** (image handling)
- **CSV** (attendance log export/import)

---

## 💡 Features

✅ Register student with full details  
✅ Capture and save face samples  
✅ Train model using LBPH algorithm  
✅ Recognize and mark attendance in real-time  
✅ Export and import attendance CSV files  
✅ Chatbot for basic user interaction  
✅ Developer profile screen  
✅ Clean GUI-based workflow

---

## 🗃️ Folder Structure

```

face\_recognition\_system/
│
├── main.py                    # Main dashboard
├── student\_details.py         # Register/update/delete students
├── face\_recognition.py        # Real-time recognition & attendance
├── train.py                   # Train LBPH face recognizer
├── attendance.py              # View/export/import attendance
├── chatbot.py                 # FAQ chatbot
├── developer.py               # Developer profile screen
├── Images/                    # All GUI images
├── data/                      # Stored face images (user.id.count.jpg)
├── classifier.xml             # Trained LBPH face recognition model
├── haarcascade\_frontalface\_default.xml  # Face detection model
├── shubh.csv                  # Attendance CSV log
└── README.md

````

---

## 📂 Database Configuration

### ➕ Required Table

Create a MySQL database:

```sql
CREATE DATABASE face_recognizer;

USE face_recognizer;

CREATE TABLE student (
    Dep VARCHAR(50),
    Course VARCHAR(50),
    Year VARCHAR(50),
    Semester VARCHAR(50),
    Student_id VARCHAR(50) PRIMARY KEY,
    Name VARCHAR(100),
    Division VARCHAR(10),
    Roll VARCHAR(20),
    Gender VARCHAR(10),
    Dob VARCHAR(20),
    Email VARCHAR(100),
    Phone VARCHAR(20),
    Address VARCHAR(255),
    Teacher VARCHAR(100),
    PhotoSample VARCHAR(10)
);
````

Update the DB config in your code (`host`, `username`, `password`) as per your system.

---

## ▶️ How to Run

1. Ensure MySQL is running and `face_recognizer` DB is set up.
2. Install required libraries:

```bash
pip install opencv-python pillow mysql-connector-python
```

3. Place Haar Cascade XML in project root (download from OpenCV GitHub if needed).
4. Run the main dashboard:

```bash
python main.py
```

---

## 🧪 Workflow

### 👤 1. Student Registration

* Enter full student details
* Capture photo samples (100)
* Saved in `data/` folder

### 🧠 2. Train Model

* Trains `LBPH` model from face samples
* Outputs `classifier.xml`

### 🧾 3. Face Recognition

* Uses webcam
* If face matches: logs attendance in `shubh.csv` and displays name, ID, time

### 📋 4. Attendance Management

* View, import, export `.csv` attendance records

### 🤖 5. ChatBot

* Responds to basic questions like:

  * What is your name?
  * How does face recognition work?

---

## 📸 Required Images

Place all the following inside the `Images/` folder:

```
Images/
├── smart-attendance.jpg
├── clg.jpg
├── facialrecognition.png
├── background.jpg
├── students.jpg
├── photos.jpg
├── Train.jfif
├── developer.jfif
├── girl.jpeg
├── shuats.jpg
├── dev.jpg
├── 1568579834677.jpg
├── chat.jfif
├── exit.jpg
├── face_detector1.jpg
```

---

## 🧑‍💻 Developer Info

**Name**: Shubham Pandey
**Roll No.**: 17BTCSE027
**University**: SHUATS Allahabad

---

## 📝 License

This project is intended for academic/demo use.
Feel free to adapt and enhance it.

