import cv2
import pickle
import face_recognition.face_detection_cli
import numpy
import face_recognition
import cvzone
from PIL import Image
from . import show_result
from GUI import face_check

SCALE = 4

def processing(img, class_ID):
    imgS = cv2.resize(img, (0, 0), None, 1/SCALE, 1/SCALE)
    
    face_current_frame = face_recognition.face_locations(imgS)
    encode_current_frame = face_recognition.face_encodings(imgS, face_current_frame)
    
    for encoded_face, face_location in zip(encode_current_frame, face_current_frame):
        matches = face_recognition.compare_faces(encode_list_known, encoded_face, 0.4)
        faceDistance = face_recognition.face_distance(encode_list_known, encoded_face)
        matchesIndex = numpy.argmin(faceDistance)
        if(matches[matchesIndex]):
            matched_student_ID = studentIDs[matchesIndex]
            show_result.find_result(matched_student_ID, class_ID)
            face_location_illust(img, face_location)
        else:
            print("No known face detected")

def face_location_illust(img, face_location):
    y1, x2, y2, x1 = face_location
    y1 *= SCALE
    x2 *= SCALE
    y2 *= SCALE
    x1 *= SCALE
    bbox = x1, y1, x2 - x1, y2 - y1
    cvzone.cornerRect(img, bbox, rt = 0)
    
def scanning(class_ID):
    success, img = cap.read()
    if success:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        processing(img, class_ID)
        face_check.update_frame(Image.fromarray(img), class_ID)
    
cap = cv2.VideoCapture(0)

# Load the encoding file
file = open("back_end/EncodeFile.p", "rb")
encode_list_known_with_IDs = pickle.load(file)
file.close()
encode_list_known, studentIDs = encode_list_known_with_IDs
print(studentIDs)

def open_cam():
    global cap
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Unable to access the webcam.")
        exit()
    cap.set(3, 1600)
    cap.set(4, 1080)
    print(studentIDs)
    print("cam is set")
    
def close_cam():
    if cap.isOpened():
        cap.release()
        cv2.destroyAllWindows()
        print("cam released")