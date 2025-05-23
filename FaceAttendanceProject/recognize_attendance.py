# import cv2
# import numpy as np
# import os
# from datetime import datetime
# import csv
# import pandas as pd

# # Load trained model
# recognizer = cv2.face.LBPHFaceRecognizer_create()
# recognizer.read('trainer.yml')

# # Load face detector
# cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
# face_cascade = cv2.CascadeClassifier(cascade_path)

# # Keep track of logged IDs and unknowns in this session
# logged_ids = set()
# unknown_logged = False

# # Attendance logging function
# def mark_attendance(id):
#     filename = 'Attendance.csv'
#     now = datetime.now()
#     dt_string = now.strftime('%Y-%m-%d %H:%M:%S')

#     # Create file with header if it doesn't exist
#     if not os.path.exists(filename):
#         with open(filename, 'w', newline='') as f:
#             writer = csv.writer(f)
#             writer.writerow(['ID', 'DateTime'])

#     df = pd.read_csv(filename)

#     # Append new attendance record
#     new_entry = pd.DataFrame([[id, dt_string]], columns=['ID', 'DateTime'])
#     df = pd.concat([df, new_entry], ignore_index=True)
#     df.to_csv(filename, index=False)

# # Start webcam
# cap = cv2.VideoCapture(0)

# print("🔍 Recognizing... Press 'q' to quit.")

# while True:
#     ret, frame = cap.read()
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.2, 5)

#     for (x, y, w, h) in faces:
#         id, confidence = recognizer.predict(gray[y:y+h, x:x+w])

#         if confidence < 60:
#             # Log attendance only if this ID not logged yet
#             if id not in logged_ids:
#                 mark_attendance(id)
#                 logged_ids.add(id)
#             label = f"User {id}"
#         else:
#             # For unknown faces, log only once per session
#             if not unknown_logged:
#                 mark_attendance('Unknown')
#                 unknown_logged = True
#             label = "Unknown"

#         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
#         cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

#     cv2.imshow('Face Recognition Attendance', frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()
import cv2
import numpy as np
import os
from datetime import datetime
import csv
import pandas as pd

# Example mapping from ID to name
id_to_name = {
    1: "Alice",
    2: "Bob",
    3: "Charlie"
    # Add your other IDs and names here
}

# Load trained model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')

# Load face detector
cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

logged_ids = set()
unknown_logged = False

def mark_attendance(id):
    filename = 'Attendance.csv'
    now = datetime.now()
    dt_string = now.strftime('%Y-%m-%d %H:%M:%S')

    # Get name for ID or "Unknown"
    name = id_to_name.get(id, "Unknown") if id != 'Unknown' else "Unknown"

    if not os.path.exists(filename):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['ID', 'Name', 'DateTime'])

    df = pd.read_csv(filename)
    new_entry = pd.DataFrame([[id, name, dt_string]], columns=['ID', 'Name', 'DateTime'])
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(filename, index=False)

cap = cv2.VideoCapture(0)

print("🔍 Recognizing... Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)

    for (x, y, w, h) in faces:
        id, confidence = recognizer.predict(gray[y:y+h, x:x+w])

        if confidence < 60:
            if id not in logged_ids:
                mark_attendance(id)
                logged_ids.add(id)
            label = f"{id_to_name.get(id, 'User ' + str(id))}"
        else:
            if not unknown_logged:
                mark_attendance('Unknown')
                unknown_logged = True
            label = "Unknown"

        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, label, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    cv2.imshow('Face Recognition Attendance', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
