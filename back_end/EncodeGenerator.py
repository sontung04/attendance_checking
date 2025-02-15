import cv2
import face_recognition
import pickle
import os

def findEncodings(imageList):
    encodeList = []
    for img in imageList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
# Importing student images
imageFolderPath = 'back_end/Images'
imageFolderList = os.listdir(imageFolderPath)
for imageCollectionPath in imageFolderList:
    imageClassPath = imageFolderPath + '/' + imageCollectionPath
    print(imageClassPath)
    imagePathList = os.listdir(imageClassPath)
    
    imageList = []
    studentIDs = []
    for path in imagePathList:
        imageList.append(cv2.imread(os.path.join(imageClassPath, path)))
        studentIDs.append(os.path.splitext(path)[0])
    # Encode student images and save to a file
    print("------------ENCODING STARTED---------------")
    encodeListKnown = findEncodings(imageList)
    encodeListKnownWithIDs = [encodeListKnown, studentIDs]
    print("-----------ENCODING FINISHED---------------")

    
    file = open(f"{imageClassPath}.p", 'wb')
    pickle.dump(encodeListKnownWithIDs, file)
    file.close()
    print("---------------FILE SAVED------------------")