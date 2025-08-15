import os
import cv2
import face_recognition
import numpy as np

from recognition_helpers import find_encodings, mark_attendance

# --- Load known face images and names ---
images = []
names = []
files_list = os.listdir(path="known_faces")  # List all files in known_faces folder

for file in files_list:
    image = cv2.imread(filename=f"known_faces/{file}")  # Read each image
    images.append(image)
    name = os.path.splitext(file)[0]  # Extract name without file extension
    names.append(name)

print(names)

# Compute encodings for all known faces
encodings_list_known = find_encodings(images)


# --- Trackbar callback function (required but not used) ---
def empty(e):
    pass


# --- Setup OpenCV window with brightness trackbar ---
cv2.namedWindow(winname="frame")
cv2.createTrackbar("Brightness", "frame", 50, 100, empty)

# --- Initialize webcam ---
webcam = cv2.VideoCapture(0)
webcam.set(propId=cv2.CAP_PROP_FPS, value=60)

while True:
    # Read frame from webcam
    is_successful, frame = webcam.read()

    # Get brightness value from trackbar and adjust frame
    brightness = cv2.getTrackbarPos(trackbarname="Brightness", winname="frame")
    frame = cv2.convertScaleAbs(src=frame, alpha=brightness / 50)

    # Resize frame for faster face recognition
    resized_frame = cv2.resize(src=frame, dsize=None, fx=0.25, fy=0.25)
    resized_frame = cv2.cvtColor(src=resized_frame, code=cv2.COLOR_BGR2RGB)

    # Detect faces in the frame
    faces = face_recognition.face_locations(img=resized_frame)

    # Compute encodings for detected faces
    encodings_list_unknown = face_recognition.face_encodings(
        face_image=resized_frame, known_face_locations=faces
    )

    # --- Compare each detected face with known faces ---
    for face_encoding, face in zip(encodings_list_unknown, faces):
        results = face_recognition.compare_faces(
            known_face_encodings=encodings_list_known,
            face_encoding_to_check=face_encoding,
            tolerance=0.4,
        )

        # Compute face distances to find best match
        face_distance = face_recognition.face_distance(
            face_encodings=encodings_list_known, face_to_compare=face_encoding
        )
        index = np.argmin(face_distance)  # Index of closest match

        print(face_distance)  # Debug: print distances

        # --- Determine if face is recognized ---
        if face_distance[index] <= 0.45:
            name = names[index].upper()
            color = (0, 255, 0)  # Green for recognized
            mark_attendance(name)  # Log attendance
        else:
            name = "NOT FOUND"
            color = (0, 0, 255)  # Red for unrecognized

        # Scale face coordinates back to original frame size
        y1, x2, y2, x1 = face
        y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

        # Draw rectangle around the face
        cv2.rectangle(img=frame, pt1=(x1, y1), pt2=(x2, y2), color=color, thickness=3)

        # Calculate size for name label
        (text_width, text_height), baseline = cv2.getTextSize(
            text=name,
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=(x2 - x1) / 300,
            thickness=2,
        )

        # Draw filled rectangle for text background
        cv2.rectangle(
            img=frame,
            pt1=(x1, y2 - text_height - 12),
            pt2=(x2, y2),
            color=color,
            thickness=cv2.FILLED,
        )

        # Put name text above rectangle
        cv2.putText(
            img=frame,
            text=name,
            org=(x1 + 6, y2 - 6),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=(x2 - x1) / 300,
            color=(255, 255, 255),
            thickness=2,
        )

    # Display webcam frame
    cv2.imshow(winname="frame", mat=frame)

    # Exit on pressing ESC key
    key = cv2.waitKey(delay=1)
    if key == 27:
        break

# Release webcam and close windows
webcam.release()
cv2.destroyAllWindows()
