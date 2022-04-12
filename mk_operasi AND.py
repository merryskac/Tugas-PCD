import cv2
import numpy as np

img1 = cv2.imread('image1.jpg')
img2 = cv2.imread('image2.jpg')

bitAnd = cv2.bitwise_and(img1,img2)
cv2.imshow("Image 1", img1)
cv2.imshow("Image 2", img1)
cv2.imshow("Bitwise AND", bitAnd)

cv2.waitKey(0)

