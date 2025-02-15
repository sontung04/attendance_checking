import cv2
import pickle
import numpy
import face_recognition
import cvzone

class_ID = '154016'
SCALE = 4
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Unable to access the webcam.")
    exit()
cap.set(3, 1600)
cap.set(4, 1080)

file = open(f"back_end/154000.p", "rb")
encode_list_known_with_IDs = pickle.load(file)
file.close()
encode_list_known, studentIDs = encode_list_known_with_IDs
print(studentIDs)
print("cam is set")

while True:
    success, img = cap.read()
    if success:
        imgS = cv2.resize(img, (0, 0), None, 1/SCALE, 1/SCALE)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    
        face_current_frame = face_recognition.face_locations(imgS)
        encode_current_frame = face_recognition.face_encodings(imgS, face_current_frame)
        
        for encoded_face, face_location in zip(encode_current_frame, face_current_frame):
            matches = face_recognition.compare_faces(encode_list_known, encoded_face, 0.4)
            faceDistance = face_recognition.face_distance(encode_list_known, encoded_face)
            matchesIndex = numpy.argmin(faceDistance)
            print(faceDistance)
            if(matches[matchesIndex]):
                matched_student_ID = studentIDs[matchesIndex]
                print("recognized student:", matched_student_ID)
                y1, x2, y2, x1 = face_location
                y1 *= SCALE
                x2 *= SCALE
                y2 *= SCALE
                x1 *= SCALE
                bbox = x1, y1, x2 - x1, y2 - y1
                cvzone.cornerRect(img, bbox, rt = 0)
            else:
                print("No known face detected")
        cv2.imshow("Face Attendance", img)
        cv2.waitKey(1)