# Face Recognition Attendance System

A Python-based **Face Recognition Attendance System** that uses **OpenCV**, **face_recognition**, and **NumPy** to detect faces in real-time using a webcam and automatically mark attendance in a CSV file.

This project is ideal for college demos, portfolio projects, mini-projects, and learning computer vision fundamentals.

---

## 🚀 Repository Name

**`face-recognition-attendance-system`**

---

## 📸 Features

* Real-time face detection using webcam
* Automatic face recognition using pre-encoded images
* Attendance stored in CSV format with timestamp
* Detects multiple faces in a single frame
* Only marks attendance once per person per session

---

## 🧾 Requirements

Install all required libraries using:

```
pip install -r requirements.txt
```

### **requirements.txt** (Add this in your repo)

```
opencv-python
face_recognition
numpy
```

---

## 📂 Project Structure

```
face-recognition-attendance-system/
 ├── images/
 │    ├── yash.jpg
 │    ├── vishal.jpg
 │    ├── sanskar.jpg
 │    └── ritika.jpg
 ├── attendance/
 │    └── (CSV files will be saved here)
 ├── main.py
 ├── requirements.txt
 └── README.md
```

---

## ▶️ How to Run

1. Clone the repository:

```
git clone https://github.com/your-username/face-recognition-attendance-system.git
```

2. Go to the project folder:

```
cd face-recognition-attendance-system
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run the script:

```
python main.py
```

5. Press **Q** to exit the window.

---

## 📌 How It Works

1. The script loads known images and converts them into face encodings.
2. Webcam feed starts and faces are detected frame-by-frame.
3. Each detected face is compared with known faces.
4. If a match is found:

   * Name is shown on screen
   * Attendance is stored in `Attendance_YYYY-MM-DD.csv`

---

## 🧑‍💻 Code Explanation

* `face_recognition.face_encodings()` → Converts face into numerical encoding
* `compare_faces()` → Matches current face with known faces
* `np.argmin()` → Finds best match using minimum distance
* `csv_writer.writerow()` → Stores attendance

---

## 📄 Output Example (CSV)

```
Name,Time
Yash Pathak,10:43:27
Vishal Dabi,10:45:12
```

---

## 📢 Future Improvements

* Add GUI dashboard
* Add database instead of CSV
* Integrate with student management system
* Add face training GUI

---

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first.

---

## 📜 License

This project is open-source and available under the **MIT License**.

---

## ✨ Author

**Yash Pathak**

If you like this project, don't forget to ⭐ the repository!
