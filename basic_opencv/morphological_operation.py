import cv2

import  numpy as np

img1=cv2.imread("./data_image/lion.jpg",0)
kernel=np.ones((3,3))

ersion_img=cv2.erode(img1,kernel=kernel,iterations=1)
dilate_img=cv2.dilate(img1,kernel=kernel,iterations=1)


cv2.imshow("orignal_image",img1)
cv2.imshow("erode_image",ersion_img)
cv2.imshow("dilate_image",dilate_img)


cv2.waitKey(0)
cv2.destroyAllWindows()