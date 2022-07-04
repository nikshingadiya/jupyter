import cv2
import numpy as np
x=np.zeros((500,500))
x[:,:]=0
x[100:200,100:300]=255

cv2.imshow("img",x)
cv2.waitKey(0)
cv2.destroyAllWindows()