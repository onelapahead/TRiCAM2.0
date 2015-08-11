# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 14:46:11 2015

@author: SU_ANGE
"""

import cv2


cap = cv2.VideoCapture("C:\Users\SU_ANGE\Documents\GitHub\\TRiCAM2.0\\test_video\\test.mp4")
counter = 0
while True:
    counter += 1
    ret, frame = cap.read()

    #frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #frame = cv2.equalizeHist(frame)
    #cv2.imshow("frame",frame)
    #cv2.imwrite("C:\Users\SU_ANGE\Documents\GitHub\\TRiCAM2.0\\captures\\starbucks"+str(counter)+".jpg",frame)
    cv2.imwrite("C:\Users\SU_ANGE\Documents\GitHub\\TRiCAM2.0\\captures\\starbucks_color_s"+str(counter)+".jpg",frame)
    ch = 0xFF & cv2.waitKey(5)
    if ch == 27:
        break
cv2.destroyAllWindows()