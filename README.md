[Readme.md](https://github.com/user-attachments/files/20416782/Readme.md)
# 🎯 Face Recognition Attendance System

## Powered by Python, OpenCV & LBPH Face Recognition

## 📌 Overview

An AI-powered attendance system that __uses real-time face recognition via webcam__ to log student or employee presence automatically into a CSV file.

Built using Python and OpenCV’s LBPH (Local Binary Patterns Histograms) algorithm for high-speed and efficient facial identification.

## 🛠️ Tech Stack
```
| Tech   | Purpose                         |
| ------ | ------------------------------- |
| Python | Core programming language       |
| OpenCV | Face detection and recognition  |
| NumPy  | Array processing                |
| Pandas | Efficient CSV data manipulation |
```
## 🚀 Key Features

- ✅ Real-time face detection & recognition
- ✅ Attendance recorded with timestamp
- ✅ Duplicate entry prevention
- ✅ Handles both known and unknown faces
- ✅Clean CSV export for easy integration with Excel or databases

## nstall dependencies:
```
pip install opencv-python opencv-contrib-python numpy pandas
```
## 📂 Project Structure
```
FaceRecognitionAttendance/
│
├── capture_dataset.py       # Collects face images for training
├── train_model.py           # Trains the LBPH face recognizer
├── recognize_attendance.py  # Recognizes faces and marks attendance
├── trainer.yml              # Trained facial recognition model
├── Attendance.csv           # Output file logging attendance
├── labels.csv               # Stores mapping of ID to names
└── README.md                # Project documentation (this file)
```
## 🧑‍💻 Usage Instructions

__1️⃣ Register a New User__

Run the following to capture face images:
```
python capture_dataset.py
```
- You’ll be prompted to enter __User ID__ and __Name__
- Automatically __captures 2 images of the face to ensure initial accuracy__
- Images will be stored __automatically in the dataset/ folder__

__2️⃣ Train the Model__

Use the collected images to train the recognition model:
```
python train_model.py
```
- Generates __trainer.yml__ for recognition
- Creates or updates labels.csv for ID–Name mapping

__3️⃣ Start Attendance Logging__

Begin live face recognition and attendance marking:
```
python recognize_attendance.py
```
- Activates the webcam
- Detects and recognizes registered faces
- Logs the data into __Attendance.csv__ with:
     - ID
     - Name
     - Timestamp
- __Also logs unknown individuals__
Press __'q'__ to stop.

## 📝 Sample Output (Attendance.csv)
```
| ID | Name    | DateTime            |
| -- | ------- | ------------------- |
| 1  | Alice   | 2025-05-23 09:01:23 |
| 2  | Bob     | 2025-05-23 09:02:10 |
| -1 | Unknown | 2025-05-23 09:03:47 |
```

__✅ Each user is recorded once per session to avoid duplicate entries.__


## 📌 Tips for Better Accuracy

- Ensure proper lighting during image capture
- Capture varied angles and expressions
- Use a clean background
- Retrain the model when new users are added

## 🤝 Contributing

Contributions are welcome! Fork the repo and raise a pull request.

## 📬 Contact

__Developer:__ _Keerthi Annapaneni_

__Email:__ _annapanenikeerthi4@gmail.com_







