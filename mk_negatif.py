import cv2

img = cv2.imread('spbob1.jpg')
img_negative = 255-img

cv2.imshow('Gambar original',img)
cv2.imshow('Gambar negatif',img_negative)

cv2.waitKey(0)
cv2.destroyAllWindows()