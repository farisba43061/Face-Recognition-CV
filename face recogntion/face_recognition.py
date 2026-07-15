import cv2
import os

# -----------------------------------------------------------
# Load the Haar Cascade face detector.
# This classifier is used to detect faces in each webcam frame.
# -----------------------------------------------------------
face_detector = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml"
)

# Check if the face detector loaded successfully.
# If not, stop the program.
if face_detector.empty():
    print("Error: Face detector could not be loaded.")
    exit()

# -----------------------------------------------------------
# Create the LBPH (Local Binary Patterns Histogram)
# Face Recognizer.
# This recognizer compares detected faces with the trained model.
# -----------------------------------------------------------
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Path to the trained model
model_path = "trainer/trainer.yml"

# Check if the trained model exists
if not os.path.exists(model_path):
    print("Error: trainer.yml was not found.")
    print("Run train_model.py first.")
    exit()

# Load the trained recognition model
recognizer.read(model_path)

# -----------------------------------------------------------
# Connect each Person ID to a name.
#
# Replace "Enter Your Name Here" with your own name.
#
# Example:
# names = {
#     1: "John"
# }
# -----------------------------------------------------------
names = {
    1: "recognised"
}

# -----------------------------------------------------------
# Open the default webcam
# -----------------------------------------------------------
camera = cv2.VideoCapture(0)

# Check that the webcam opened correctly
if not camera.isOpened():
    print("Error: Camera could not be opened.")
    exit()

print("Face recognition started.")
print("Press ESC to stop.")

# -----------------------------------------------------------
# Main program loop
# -----------------------------------------------------------
while True:

    # Read one frame from the webcam
    success, frame = camera.read()

    # Stop if the frame could not be read
    if not success:
        print("Error: Could not read from the camera.")
        break

    # Convert the frame to grayscale.
    # Face recognition works better on grayscale images.
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # -------------------------------------------------------
    # Detect all faces in the current frame.
    # -------------------------------------------------------
    faces = face_detector.detectMultiScale(
        gray_frame,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(100, 100)
    )

    # Process every detected face
    for x, y, width, height in faces:

        # Crop the detected face from the grayscale image
        face_image = gray_frame[
            y:y + height,
            x:x + width
        ]

        # ---------------------------------------------------
        # Predict the person's ID and confidence value.
        #
        # person_id:
        #     The predicted ID from the trained model.
        #
        # confidence:
        #     Lower values indicate a better match.
        # ---------------------------------------------------
        person_id, confidence = recognizer.predict(face_image)

        # ---------------------------------------------------
        # If the confidence value is below 70,
        # consider the face recognized.
        # Otherwise, display "Unknown".
        # ---------------------------------------------------
        if confidence < 70:
            person_name = names.get(person_id, "Unknown")

            # Convert the confidence value into a simple
            # recognition score (0–100%)
            match_percentage = round(100 - confidence)

            # Green rectangle = recognized
            rectangle_color = (0, 255, 0)

        else:
            person_name = "not recognised"

            # Unknown faces display 0%
            match_percentage = 0

            # Red rectangle = not recognized
            rectangle_color = (0, 0, 255)

        # Draw a rectangle around the detected face
        cv2.rectangle(
            frame,
            (x, y),
            (x + width, y + height),
            rectangle_color,
            2
        )

        # Display the recognized person's name
        cv2.putText(
            frame,
            person_name,
            (x, y - 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            rectangle_color,
            2
        )

        # Display the recognition score
        cv2.putText(
            frame,
            f"Match: {match_percentage}%",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            rectangle_color,
            2
        )

    # Show the webcam feed
    cv2.imshow("Face Recognition", frame)

    # Wait for a keyboard press
    key = cv2.waitKey(1) & 0xFF

    # Exit when the ESC key is pressed
    if key == 27:
        break

# -----------------------------------------------------------
# Release the webcam.
# -----------------------------------------------------------
camera.release()

# Close all OpenCV windows.
cv2.destroyAllWindows()

print("Face recognition stopped.")