import cv2
import os
import numpy as np
from PIL import Image

# -----------------------------------------------------------
# Load the Haar Cascade face detector.
# This detector is used to locate faces in the training images.
# -----------------------------------------------------------
detector = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml"
)

# -----------------------------------------------------------
# Create the LBPH (Local Binary Patterns Histogram)
# Face Recognizer.
# This model will be trained using the captured face images.
# -----------------------------------------------------------
recognizer = cv2.face.LBPHFaceRecognizer_create()


# -----------------------------------------------------------
# Function:
# Reads all images inside the dataset folder,
# detects the faces, and returns:
#   1. A list of cropped face images.
#   2. A list of the corresponding Person IDs.
# -----------------------------------------------------------
def get_images_and_labels(path):

    # Stores the cropped face images
    face_samples = []

    # Stores the Person IDs
    ids = []

    # Loop through every image inside the dataset folder
    for file_name in os.listdir(path):

        # Create the full path to the image
        image_path = os.path.join(path, file_name)

        # Open the image and convert it to grayscale
        # Face recognition works best using grayscale images.
        gray_image = Image.open(image_path).convert("L")

        # Convert the image into a NumPy array
        image_numpy = np.array(gray_image, "uint8")

        # ---------------------------------------------------
        # Extract the Person ID from the filename.
        #
        # Example filename:
        # person.1.25.jpg
        #
        # Person ID = 1
        # ---------------------------------------------------
        person_id = int(file_name.split(".")[1])

        # Detect faces in the training image
        faces = detector.detectMultiScale(image_numpy)

        # Save every detected face and its Person ID
        for (x, y, w, h) in faces:

            # Crop only the detected face
            face_samples.append(image_numpy[y:y+h, x:x+w])

            # Save the matching Person ID
            ids.append(person_id)

    # Return all detected faces and their IDs
    return face_samples, ids


print("Training model...")

# -----------------------------------------------------------
# Load all training images from the dataset folder
# -----------------------------------------------------------
faces, ids = get_images_and_labels("dataset")

# -----------------------------------------------------------
# Train the LBPH Face Recognizer using:
#   - The detected face images
#   - Their corresponding Person IDs
# -----------------------------------------------------------
recognizer.train(faces, np.array(ids))

# Create the trainer folder if it does not already exist
os.makedirs("trainer", exist_ok=True)

# -----------------------------------------------------------
# Save the trained recognition model.
#
# This file will later be loaded by:
# face_recognition.py
# -----------------------------------------------------------
recognizer.write("trainer/trainer.yml")

print("Training completed successfully!")
print("Faces used:", len(faces))