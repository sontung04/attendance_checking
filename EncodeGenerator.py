import cv2
import face_recognition
import pickle
import os

# Importing student images
imageFolderPath = 'Images'
imagePathList = os.listdir(imageFolderPath)
imageList = []
studentIDs = []
for path in imagePathList:
    imageList.append(cv2.imread(os.path.join(imageFolderPath, path)))
    studentIDs.append(os.path.splitext(path)[0])


def findEncodings(imageList):
    encodeList = []
    for img in imageList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

# Encode student images and save to a file
print("------------ENCODING STARTED---------------")
encodeListKnown = findEncodings(imageList)
encodeListKnownWithIDs = [encodeListKnown, studentIDs]
print("-----------ENCODING FINISHED---------------")

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIDs, file)
file.close
print("---------------FILE SAVED------------------")