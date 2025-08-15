import cv2
import face_recognition

# --- Load and process the reference image ---
reference_image = face_recognition.load_image_file("elon.jpg")
reference_image = cv2.cvtColor(src=reference_image, code=cv2.COLOR_BGR2RGB)

# Detect face location and compute encoding
ref_face_location = face_recognition.face_locations(reference_image)[0]
ref_face_encoding = face_recognition.face_encodings(reference_image)[0]

# Draw rectangle around the reference face
cv2.rectangle(
    img=reference_image,
    pt1=(ref_face_location[3], ref_face_location[0]),
    pt2=(ref_face_location[1], ref_face_location[2]),
    color=(255, 0, 255),
    thickness=2,
)

# --- Load and process the test image ---
test_image = face_recognition.load_image_file("elon_test.jpg")
test_image = cv2.cvtColor(src=test_image, code=cv2.COLOR_BGR2RGB)

# Detect face location and compute encoding
test_face_location = face_recognition.face_locations(test_image)[0]
test_face_encoding = face_recognition.face_encodings(test_image)[0]

# Draw rectangle around the test face
cv2.rectangle(
    img=test_image,
    pt1=(test_face_location[3], test_face_location[0]),
    pt2=(test_face_location[1], test_face_location[2]),
    color=(255, 0, 255),
    thickness=2,
)

# --- Compare faces ---
result = face_recognition.compare_faces(
    known_face_encodings=[ref_face_encoding], face_encoding_to_check=test_face_encoding
)[0]

if result:
    color = (0, 230, 0)
else:
    color = (0, 0, 255)

face_distance = face_recognition.face_distance(
    face_encodings=[ref_face_encoding], face_to_compare=test_face_encoding
)[0]

# Overlay result and distance on test image
cv2.putText(
    img=test_image,
    text=f"{result} {round(face_distance, 2)}",
    org=(50, 50),
    fontFace=cv2.FONT_HERSHEY_COMPLEX,
    fontScale=1,
    color=color,
    thickness=2,
)

# --- Display images ---
cv2.imshow(winname="Reference Image", mat=reference_image)
cv2.imshow(winname="Test Image", mat=test_image)

cv2.waitKey(delay=0)
cv2.destroyAllWindows()
