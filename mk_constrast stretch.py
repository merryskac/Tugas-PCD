import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def getGrayColor(rgb):
    return rgb[0]
def setGrayColor(color):
    return [color,color,color]

img = Image.open('spbob1.jpg')
gray = Image.open('spbob1.jpg').convert("L")
gray = np.asarray(gray)
img = np.asarray(img)


r1 = 100
s1 = 50
r2 = 150
s2 = 200

ukuran = img.shape
zero = np.zeros((ukuran[0],ukuran[1],ukuran[2]))

for i in range(len(img)):
    for j in range(len(img[i])):
        x = getGrayColor(img[i][j])
        if 0<=x and x<=r1:
            zero[i][j] = setGrayColor(s1/r1*x)
        elif r1<x and x<=r2:
            zero[i][j] = setGrayColor(((s2-s1)/(r2-r1))*(x-r1)+s1)
        elif r2<x and x<=255:
            zero[i][j] = setGrayColor(((255-s2)/(255-r2))*(x-r2)+s2)

plt.subplot(2,2,1)
plt.imshow(img)
plt.subplot(2,2,2)
plt.imshow(np.uint8(zero))
plt.subplot(2,2,3)
plt.imshow(gray, cmap='gray', vmin=0,vmax=255)
plt.show()
