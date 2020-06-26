import cv2
import random
from matplotlib import pyplot as plt

img = cv2.imread('image/contour_test.jpg')

imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray,125,255,0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    #각 Contour Line을 구분하기 위해서 Color Random생성
    b = random.randrange(1,255)
    g = random.randrange(1,255)
    r = random.randrange(1,255)

    cnt = contours[i]
    img = cv2.drawContours(img, [cnt], -1,(b,g,r), 2)

titles = ['Result']
images = [img]

for h in hierarchy:
    print(h)
# [[ 1 -1 -1 -1]
#  [ 2  0 -1 -1]
#  [ 3  1 -1 -1]
#  [ 4  2 -1 -1]
#  [ 5  3 -1 -1]
#  [ 6  4 -1 -1]
#  [ 7  5 -1 -1]
#  [ 8  6 -1 -1]
#  [-1  7 -1 -1]]

for i in range(1):
    plt.subplot(1,1,i+1), plt.title(titles[i]), plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])

plt.show()