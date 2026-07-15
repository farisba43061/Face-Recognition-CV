import cv2
import os

# -----------------------------------------------------------
# Load the Haar Cascade face detector from the XML file.
# This classifier is used to detect human faces.
# -----------------------------------------------------------
face_detector = cv2.CascadeClassifier(
    "haarcascade_frontalface_default.xml"
)

# Check if the face detector was loaded successfully.
# If not, stop the program.
if face_detector.empty():
    print("Error: Face detector could not be loaded.")
    exit()

# -----------------------------------------------------------
# Create the "dataset" folder if it does not already exist.
# All captured face images will be saved here.
# -----------------------------------------------------------
os.makedirs("dataset", exist_ok=True)

# -----------------------------------------------------------
# Open the default webcam (camera 0).
# -----------------------------------------------------------
camera = cv2.VideoCapture(0)

# Verify that the webcam opened correctly.
if not camera.isOpened():
    print("Error: Camera could not be opened.")
    exit()

# -----------------------------------------------------------
# Enter your own ID number here.
# If you plan to support multiple people later,
# give each person a unique ID.
#
# Example:
# person_id = 1
# -----------------------------------------------------------
person_id = 1

# Counter to keep track of how many face images have been saved.
image_count = 0

print("Camera started.")
print("Look at the camera and slowly move your head.")
print("Press ESC to stop.")

# -----------------------------------------------------------
# Main program loop
# -----------------------------------------------------------
while True:

    # Capture one frame from the webcam
    success, frame = camera.read()

    # Stop the program if the frame could not be read
    if not success:
        print("Error: Could not read camera frame.")
        break

    # Convert the image to grayscale.
    # Face detection works better on grayscale images.
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # -------------------------------------------------------
    # Detect all faces in the current frame.
    #
    # scaleFactor:
    #   Controls how much the image size is reduced at each scale.
    #
    # minNeighbors:
    #   Higher values reduce false detections.
    #
    # minSize:
    #   Ignore faces smaller than 100 × 100 pixels.
    # -------------------------------------------------------
    faces = face_detector.detectMultiScale(
        gray_frame,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(100, 100)
    )

    # Process every detected face
    for x, y, width, height in faces:

        # Draw a green rectangle around the detected face
        cv2.rectangle(
            frame,
            (x, y),
            (x + width, y + height),
            (0, 255, 0),
            2
        )

        # Increase the image counter
        image_count += 1

        # Crop only the detected face from the grayscale image
        face_image = gray_frame[
            y:y + height,
            x:x + width
        ]

        # ---------------------------------------------------
        # Save the cropped face image.
        #
        # Filename format:
        # person.<ID>.<Image Number>.jpg
        #
        # Example:
        # person.1.25.jpg
        # ---------------------------------------------------
        filename = f"dataset/person.{person_id}.{image_count}.jpg"

        cv2.imwrite(filename, face_image)

        # Display the number of captured images
        cv2.putText(
            frame,
            f"Images: {image_count}/100",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    # Display the webcam feed
    cv2.imshow("Capture Faces", frame)

    # Wait 1 millisecond for a keyboard press
    key = cv2.waitKey(1) & 0xFF

    # Exit the program when the ESC key is pressed
    if key == 27:
        break

    # Automatically stop after collecting 100 face images
    if image_count >= 100:
        break

# -----------------------------------------------------------
# Release the webcam so other programs can use it.
# -----------------------------------------------------------
camera.release()

# Close all OpenCV windows.
cv2.destroyAllWindows()

# Display a completion message
print(f"Finished. {image_count} face images were saved.")

print("\nNext Steps:")
print("1. Run train_model.py to train the face recognition model.")
print("2. Run face_recognition.py to recognize the trained face.")