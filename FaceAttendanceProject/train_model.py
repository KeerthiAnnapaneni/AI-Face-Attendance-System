import cv2
import numpy as np
import os

path = 'dataset'
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def get_images_and_labels(path):
    image_paths = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]
    face_samples = []
    ids = []

    for image_path in image_paths:
        gray_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if gray_img is None:
            continue
        id = int(os.path.split(image_path)[-1].split(".")[1])  # Extract user ID
        faces = detector.detectMultiScale(gray_img)
        for (x, y, w, h) in faces:
            face_samples.append(gray_img[y:y+h, x:x+w])
            ids.append(id)

    return face_samples, ids

faces, ids = get_images_and_labels(path)
recognizer.train(faces, np.array(ids))
recognizer.write('trainer.yml')
print("\n✅ Model training completed and saved as trainer.yml")

