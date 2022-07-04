import cv2

import  numpy as np

canvas=np.zeros((500,500,3))


## line line 4 and line_8 brehman algo
## line AA Gausian Line
cv2.line(canvas,(100,100),(200,200),color=(255,0,0),thickness=5,lineType=12)


arr=np.array([[200,34],[400,89],[300,46]])
arr=arr.reshape((-1,1,2))
print(arr)
cv2.polylines(canvas,[arr],False,(0,255,0),3)
cv2.imshow("canvas",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()