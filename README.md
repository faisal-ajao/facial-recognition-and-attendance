# 👤 Facial Recognition and Attendance System

This project implements a real-time facial recognition and attendance system using Python, OpenCV, and the `face_recognition` library. It detects faces via webcam, compares them with known faces, and logs attendance automatically.

---

## 🚀 Features
- Real-time face detection and recognition.
- Logs attendance with timestamps in a CSV file.
- Highlights recognized faces in green and unknown faces in red.
- Adjustable webcam brightness using a trackbar.
- Supports multiple known faces.

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/faisal-ajao/facial-recognition-and-attendance.git
cd facial-recognition-and-attendance

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt
```

## ▶️ Usage

### Basic Face Recognition
Run:
```
python basic_face_recognition.py
```
- Compares `elon.jpg` with `elon_test.jpg` and displays face rectangles and distance scores.

### Attendance Project
Run:
```
python attendance_project.py
```
- Opens webcam, recognizes faces, and logs attendance in `attendance.csv`.

---

## 📊 Output Example (Video)
[![Watch the output](https://img.youtube.com/vi/1zLKt2gpCck/hqdefault.jpg)](https://youtu.be/1zLKt2gpCck?feature=shared)

---

## 📂 Project Structure
```
facial-recognition-and-attendance/
├── known_faces/             # Folder with reference images
├── attendance.csv           # Attendance log
├── basic_face_recognition.py
├── attendance_project.py
├── recognition_helpers.py
├── README.md
└── requirements.txt 
```

---

## 🧠 Tech Stack
- Python 3.11.5
- OpenCV
- face_recognition
- NumPy


---

## 📜 License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

## Install dependencies
```bash
pip install -r requirements.txt
```
