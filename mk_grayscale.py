import cv2

img = cv2.imread('spbob1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

cv2.imshow('Gambar Original',img)
cv2.imshow('Gambar grayscale',gray)

cv2.waitKey(0)
cv2.destroyAllWindows()