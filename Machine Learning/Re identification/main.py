# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 11:55:21 2021

@author: nikhil
"""
import cv2

from distance import EuclideanDistTracker

cap = cv2.VideoCapture("demo.mp4")
tracker=EuclideanDistTracker()

# Object detection from Stable camera
object_detector = cv2.createBackgroundSubtractorMOG2(history=200)

while True:
    ret, frame = cap.read()
    
    if ret:
        frame=cv2.resize(frame,(1280,720))
        
        height, width,_ = frame.shape
        # Extract Region of interest
    
        # 1. Object Detection
        mask = object_detector.apply(frame)
        _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        list_object=[]
        
        
        if len(contours) != 0:
            for cnt in contours:
                area=cv2.contourArea(cnt)
                if area>500:
                    x,y,w,h=cv2.boundingRect(cnt)
                    list_object.append([x,y,w,h])
                
               
            # cv2.resizeWindow("frame")
            
            
            box_ids = tracker.update(list_object)
            
            for box_id in box_ids:
                
                x,y,w,h,id =box_id
                
                cv2.putText(frame,str(id),(x,y-15),cv2.FONT_HERSHEY_PLAIN,1,(0,0,255),3)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                
            cv2.imshow("frame",frame)
            
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()