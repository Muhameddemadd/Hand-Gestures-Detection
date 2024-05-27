from predict import Classifier
import cv2
from hands import hand_detector
import math
import serial 
import time
import numpy as np


#ser = serial.Serial('COM3',115200)
classifier = Classifier("model_path","labels_path" )
detector = hand_detector()
offset = 20
imgSize = 300
counter = 0
labels = ["up","down", "right", "left","open","close"]
cap = cv2.VideoCapture(1)


while True:
                
    success, img = cap.read()
    img = cv2.flip(img, 1)

    #img = cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
    imgOutput = img.copy()
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

        imgCropShape = imgCrop.shape

        aspectRatio = h / w

        if aspectRatio > 1:
            k = imgSize / h
            wCal = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            imgResizeShape = imgResize.shape
            wGap = math.ceil((imgSize - wCal) / 2)
            imgWhite[:, wGap:wCal + wGap] = imgResize
            prediction, index = classifier.getPrediction(imgWhite, draw=False)
            
           

        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            imgResizeShape = imgResize.shape
            hGap = math.ceil((imgSize - hCal) / 2)
            imgWhite[hGap:hCal + hGap, :] = imgResize
            prediction, index = classifier.getPrediction(imgWhite, draw=False)
            

        cv2.rectangle(imgOutput, (x - offset, y - offset-50),(x - offset+90, y - offset-50+50), (255, 0, 255), cv2.FILLED)
        cv2.putText(imgOutput, labels[index], (x, y -26), cv2.FONT_HERSHEY_COMPLEX, 1.7, (255, 255, 255), 2)
        cv2.rectangle(imgOutput, (x-offset, y-offset),(x + w+offset, y + h+offset), (255, 0, 255), 4)




    cv2.imshow("Image", imgOutput)
    cv2.waitKey(1)


