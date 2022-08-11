import cv2

import cv2
# Loading the image
img = cv2.imread('./data_image/bull.jpg')
  
 # Converting image to grayscale
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  
# Applying SIFT detector
sift = cv2.xfeatures2d.SIFT_create() 
kp = sift.detect(gray, None)
  
# Marking the keypoint on the image using circles
img1=cv2.drawKeypoints(gray ,
                      kp ,
                      img ,
                      flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
  
cv2.imwrite('image-with-keypoints.jpg', img1)
cv2.imshow("image_detect",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()