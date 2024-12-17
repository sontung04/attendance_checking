import cv2
import pickle
import numpy
import face_recognition
import cvzone
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Load the encoding file
file = open("EncodeFile.p", "rb")
encodeListKnownWithIDs = pickle.load(file)
file.close()

encodeListKnown, studentIDs = encodeListKnownWithIDs
print(studentIDs)

SCALE = 4

while True:
    success, img = cap.read()
    
    imgS = cv2.resize(img, (0, 0), None, 1/SCALE, 1/SCALE)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    
    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)
    for encodedFace, faceLocation in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodedFace)
        faceDistance = face_recognition.face_distance(encodeListKnown, encodedFace)
        # print("matches", matches)
        # print("faceDistance", faceDistance)
        matchesIndex = numpy.argmin(faceDistance)
        if(matches[matchesIndex]):
            # Show face location
            y1, x2, y2, x1 = faceLocation
            y1 *= SCALE
            x2 *= SCALE
            y2 *= SCALE
            x1 *= SCALE
            bbox = x1, y1, x2 - x1, y2 - y1
            cvzone.cornerRect(img, bbox, rt = 0)
    cv2.imshow("Face Attendance", img)
    cv2.waitKey(1)