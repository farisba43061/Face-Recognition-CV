# Face Recognition CV

## Overview

Face Recognition CV is a real-time computer vision project built with **Python** and **OpenCV**. The application captures face images using a webcam, trains an LBPH face recognition model, and recognizes the trained person in real time.

---

## Features

- Real-time face detection
- Face image collection
- Face recognition using the LBPH Face Recognizer
- Displays the person's name and recognition score
- Live webcam recognition

---

## Technologies Used

- Python
- OpenCV
- OpenCV Contrib
- NumPy
- Pillow
- Haar Cascade Classifier

---

## Project Structure

```text
Face Recognition/
│
├── dataset/
├── trainer/
├── capture_faces.py
├── train_model.py
├── face_recognition.py
├── haarcascade_frontalface_default.xml
└── README.md
```

---

## Installation

Install the required Python libraries:

```powershell
python -m pip install opencv-python
python -m pip install opencv-contrib-python
python -m pip install numpy
python -m pip install pillow
```

Or install everything at once:

```powershell
python -m pip install opencv-python opencv-contrib-python numpy pillow
```

---

## Required File

Download the following file from the official OpenCV GitHub repository:

```text
haarcascade_frontalface_default.xml
```

Place the XML file in the main project folder alongside the Python files.

---

## What Each File Does

### `capture_faces.py`

- Opens the webcam.
- Detects the user's face.
- Captures approximately 100 grayscale face images.
- Saves the images inside the **dataset** folder.

---

### `train_model.py`

- Reads every image inside the **dataset** folder.
- Detects the face in each image.
- Trains the LBPH Face Recognizer.
- Saves the trained model as:

```text
trainer/trainer.yml
```

---

### `face_recognition.py`

- Opens the webcam.
- Detects faces in real time.
- Loads the trained model.
- Recognizes trained faces.
- Displays the person's name and recognition score.

Before running the program, replace:

```python
names = {
    1: "Enter Your Name Here"
}
```

with your own name.

---

### `dataset/`

Stores all captured face images.

---

### `trainer/`

Stores the trained face recognition model (`trainer.yml`).

---

### `haarcascade_frontalface_default.xml`

The Haar Cascade classifier used to detect frontal human faces.

---

## How to Use

### Step 1: Open the Project

Open the project folder in Visual Studio Code.

---

### Step 2: Install the Required Libraries

```powershell
python -m pip install opencv-python opencv-contrib-python numpy pillow
```

---

### Step 3: Create the Required Folders

Create these folders inside the project directory if they do not already exist:

```text
Face Recognition/
│
├── dataset/
└── trainer/
```

- **dataset/** stores the captured face images.
- **trainer/** stores the trained recognition model.

---

### Step 4: Download the Haar Cascade File

Download:

```text
haarcascade_frontalface_default.xml
```

Place it inside the project folder with the Python files.

---

### Step 5: Enter Your Name

Open **face_recognition.py**.

Replace:

```python
names = {
    1: "Enter Your Name Here"
}
```

with your own name.

Example:

```python
names = {
    1: "John"
}
```

---

### Step 6: Capture Your Face Images

Run:

```powershell
python capture_faces.py
```

Look directly at the webcam and slowly move your head:

- Left
- Right
- Up
- Down
- Slightly closer
- Slightly farther away

The program automatically stops after capturing approximately **100 face images**.

You can also press **Esc** to stop.

---

### Step 7: Train the Recognition Model

Run:

```powershell
python train_model.py
```

This creates:

```text
trainer/trainer.yml
```

---

### Step 8: Start Face Recognition

Run:

```powershell
python face_recognition.py
```

The webcam will open and recognize the trained face.

Press **Esc** to close the application.

---

## Using a Different Person

To train the project for another person:

1. Delete every image inside the **dataset** folder.
2. Delete **trainer/trainer.yml**.
3. Change the name inside `face_recognition.py`.
4. Run `capture_faces.py`.
5. Run `train_model.py`.
6. Run `face_recognition.py`.

---

## Important Notes

- Use good lighting.
- Keep your face fully visible.
- Capture images from multiple angles.
- Do not move too quickly while capturing images.
- A lower LBPH confidence value means a better match.
- Click the camera window before pressing **Esc**.

---

## Track

This project was developed as part of the **Artificial Intelligence and Robotics Track**.

---

## Author

**Faris Bahussain**
