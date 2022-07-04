import cv2

import  numpy as np

img=cv2.imread("bull.jpg")

img=cv2.resize(img,(300,300))
## line line 4 and line_8 brehman algo
## line AA Gausian Line
res_image_linear=cv2.resize(img,None,fx=2.5,fy=1.5,interpolation=cv2.INTER_LINEAR)
res_image_cubic=cv2.resize(img,None,fx=2.5,fy=1.5,interpolation=cv2.INTER_CUBIC)


cv2.imshow("linear",res_image_linear)
cv2.imshow("cubic",res_image_cubic)
cv2.waitKey(0)
cv2.destroyAllWindows()