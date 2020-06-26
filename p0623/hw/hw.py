import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('picture.jpg')
image = img.copy()

image = cv2.resize(img, dsize=(600, 500), interpolation=cv2.INTER_AREA)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)    # 블러처리 이후
edged = cv2.Canny(gray, 75, 200)    # edge 검출 (Canny Edge Detection)

# cv2.imshow('edge', edged)
# cv2.waitKey(0)

cnts, _ = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
# cv2.RETR_LIST : contours line을 찾지만 hierachy 관계를 구성하지 않음.

cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:5] # 최대 5개의 찾은 윤곽선을 가져옴
# cv2.contourArea : contour가 그린 면적

for c in cnts:
    peri = cv2.arcLength(c, True)   # contour가 그리는 길이를 반환
    approx = cv2.approxPolyDP(c, 0.02*peri, True)

    if len(approx) == 4:
        screenCnt = approx
        break

cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
# cv2.imshow('edge', image)
# cv2.waitKey(0)

print(screenCnt)
tmp = []
color = [(255,0,0), (0,255,0), (0,0,255), (0,0,0)]
for i in range(4):
    tmp.append(list(*screenCnt[i]))
    cv2.circle(image, tuple(*screenCnt[i]), 5, color[i],-1)

print(tmp) # 검출된 꼭지점 (buttom_left, buttom_right, top_right, top_left 순)
cv2.imshow('edge', image)
cv2.waitKey(0)

buttom_left, buttom_right, top_right, top_left = tmp

w1 = abs(buttom_right[0]-buttom_left[0])
w2 = abs(top_right[0]-top_left[0])
h1 = abs(top_right[1]-buttom_right[1])
h2 = abs(top_left[1]-buttom_left[1])

maxw = max([w1, w2])
maxh = max([h1, h2])

pts1 = np.float32([top_left, top_right, buttom_right, buttom_left])
pts2 = np.float32([[0,0],[maxw-1,0],[maxw-1,maxh-1],[0, maxh-1]])


M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(image, M, (maxw, maxh))

plt.subplot(121),plt.imshow(img),plt.title('image')
plt.subplot(122),plt.imshow(dst),plt.title('Perspective')
plt.show()