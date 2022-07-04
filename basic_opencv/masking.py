import cv2

import  numpy as np

img1=cv2.imread("camilion.jpeg")

# img1=cv2.resize(img1,(500,500))
# img2=cv2.imread("camilion.jpeg")

# img2=cv2.resize(img2,(500,500))
# img3=cv2.addWeighted(img1,0.6,img2,-1.6,0)

# cv2.imshow("img_show",img3)

gray_img1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

ret,mask=cv2.threshold(gray_img1,100,255,cv2.THRESH_BINARY_INV)
mask_inv=cv2.bitwise_not(mask)

masked_imag1=cv2.bitwise_xor(img1,img1,mask=mask_inv)
print(ret)
cv2.imshow("mask",img1)
cv2.imshow("masked_imag1",masked_imag1)
cv2.waitKey(0)
cv2.destroyAllWindows()