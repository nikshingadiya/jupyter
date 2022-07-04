import cv2

import  numpy as np

img=cv2.imread("bull.jpg")

img=cv2.resize(img,(500,500))
size=10
kernel=np.zeros((size,size))
kernel[int((size-1)/2),:]=np.ones(size)

kernel=kernel/size

motion_image=cv2.filter2D(img,ddepth=-1,kernel=kernel)

cv2.imshow("motion_image",motion_image)
cv2.imshow("original_img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()