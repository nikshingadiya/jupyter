# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 21:47:24 2021

@author: nikhil
"""
from imutils.object_detection import non_max_suppression
from imutils import paths
import numpy as np
import argparse
import imutils
import cv2

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cap = cv2.VideoCapture("runing.mp4")

while True:

    ret, frame = cap.read()
    if ret:

        frame = cv2.resize(frame, (400, 300))
        # cv2.imshow("frame",frame)
        (rects, weights) = hog.detectMultiScale(
            frame, winStride=(4, 4), padding=(4, 4), scale=1.5)

        orig = frame.copy()

        for (x, y, w, h) in rects:
            cv2.rectangle(orig, (x, y), (x + w, y + h), (0, 0, 255), 2)

        cv2.imshow("ori_pre", orig)
        rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
        pick = non_max_suppression(rects, probs=None, overlapThresh=0.65)

        for (xA, yA, xB, yB) in pick:
            cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)
        cv2.imshow("final", frame)
    else:
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
