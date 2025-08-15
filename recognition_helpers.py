import cv2
import face_recognition

from datetime import datetime


# --- Function to compute facial encodings for a list of images ---
def find_encodings(images):
    """
    Takes a list of images and returns a list of corresponding face encodings.
    Each encoding is a 128-d vector representing facial features.
    """
    encodings_list_known = []

    for image in images:
        # Convert image from BGR (OpenCV default) to RGB (face_recognition requirement)
        image = cv2.cvtColor(src=image, code=cv2.COLOR_BGR2RGB)

        # Compute the face encoding; num_jitters=2 improves accuracy slightly
        face_encoding = face_recognition.face_encodings(face_image=image)[0]

        encodings_list_known.append(face_encoding)

    print("Encodings Completed")
    return encodings_list_known


# --- Function to log attendance for recognized faces ---
def mark_attendance(name):
    """
    Records the name and timestamp of a recognized face into attendance.csv.
    Ensures each person is logged only once per session.
    """
    with open(file="attendance.csv", mode="r+") as file:
        names_found = []

        # Read all existing entries
        for line in file.readlines():
            line = line.split(sep=",")
            names_found.append(line[0])

        # Add new entry if the name is not already recorded
        if name not in names_found:
            now = datetime.now()
            now = now.strftime("%H:%M:%S")  # Format time as HH:MM:SS
            file.writelines(f"\n{name},{now}")
