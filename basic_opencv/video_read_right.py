import cv2

import numpy as np

cap =cv2.VideoCapture(-1)

fourcc=cv2.VideoWriter_fourcc(*"mp4v")
height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)

fps=cap.get(cv2.CAP_PROP_FPS)
out=cv2.VideoWriter(fps=fps,apiPreference = 0,fourcc=fourcc,filename="jj.mp4",frameSize=(int(width),int(height)))

if cap.isOpened():
    
    while cap.isOpened():

        ret,frame=cap.read()
        print(ret)
        if ret:
            cv2.imshow("windw",frame)
            out.write(frame)
            if cv2.waitKey(2)==27:
                break
        else:
            break

cap.release()
out.release()
cv2.destroyAllWindows()

