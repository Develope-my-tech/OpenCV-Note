import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/home.jpg')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

hist = cv2.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])

cv2.imshow('Hist',hist)

plt.imshow(hist) #, interpolation='nearest')
plt.show()