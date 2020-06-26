import cv2
import numpy as np

img = cv2.imread('02_test.jpg')
sticker = cv2.imread('02_stiky.png')
print(sticker.shape)
w = 145
h = 169
img[250:250 + w, 420:420 + h] = sticker
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
