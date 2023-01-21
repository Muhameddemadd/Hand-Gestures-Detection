from functools import total_ordering
from msilib.schema import Class
import cv2
import mediapipe as mp
import pyautogui
import serial 
import time

ser = serial.Serial('COM5',115200)
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)
screen_width, screen_height = pyautogui.size()

thumbx=[]
thumby=[]
tipIds = [4, 8, 12, 16, 20]
fingers=[]


def get_id(frame):
    landmark_list=[]
    frame_height, frame_width, _ = frame.shape
    output = hand_detector.process(frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
                landmark_list.append([id, x, y])

        return landmark_list




while True:
    _,frame =cap.read()
    frame2 = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_height, frame_width, _ = frame.shape
    landmark_list = get_id(rgb_frame)

    if landmark_list is not None:

        # finger counter
        if len(landmark_list) != 0:
            fingers = []
            #thumb
            if landmark_list[tipIds[0]][1] > landmark_list[tipIds[0] - 1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            #4 fingers
            for id in range(1, 5):
                if landmark_list[tipIds[id]][2] < landmark_list[tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
        totalFingers = fingers.count(1)
        if totalFingers==5:
            cv2.putText(frame2, ("ON"), (10, 80), cv2.FONT_HERSHEY_PLAIN,10, (255, 0, 0), 10)
        else:
            cv2.putText(frame2, ("OFF"), (10, 80), cv2.FONT_HERSHEY_PLAIN,10, (255, 0, 0), 10)

        #Directions
        for id in landmark_list:
            if id[0]==8:
                x = id[1]
                y = id[2]
                cv2.circle(img=frame, center=(x,y), radius=10, color=(255, 0, 255),thickness=3)
                index1_x = screen_width/frame_width*x
                index1_y = screen_height/frame_height*y
                xx1 = int(index1_x)
                yy1 = int(index1_y)
                thumbx.append(xx1)
                thumby.append(yy1)
                        
                if len(thumbx)>5 and len(thumby)>5:
                    if abs(thumbx[-1] - thumbx[-5])>110:
                        if  thumbx[-1]>=thumbx[-4]:
                                cv2.putText(frame2, ("left"), (45, 200), cv2.FONT_HERSHEY_PLAIN,10, (255, 0, 0), 25)
                        else:
                                cv2.putText(frame2, ("right"), (45, 200), cv2.FONT_HERSHEY_PLAIN,10, (255, 0, 0), 25)
                    else:
                        if abs(thumby[-1] - thumby[-5])>80:
                            if  thumby[-1]>=thumby[-4]:
                                cv2.putText(frame2, ("down"), (45, 200), cv2.FONT_HERSHEY_PLAIN,10, (255, 0, 0), 25)
                                for e in range(2200):
                                    ser.write(b'H')
                            else:
                                cv2.putText(frame2, ("up"), (45, 200), cv2.FONT_HERSHEY_PLAIN,10, (255, 0, 0), 25)
                                for v in range(2200 ):
                                    ser.write(b'L')
                                  

        
          
    

    cv2.imshow("frame",frame2)
    cv2.waitKey(1)





