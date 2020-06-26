import cv2
import numpy as np
from pip._vendor.msgpack.fallback import xrange
from PIL import Image
from pytesseract import *

img = cv2.imread('img/c1.jpg')#이미지 파일에서 영상을 읽어들인다. 각 픽셀정보
img = cv2.resize(img, (600,420)) #img를 크기를 600*420으로 재조정

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#흑백처리
blur = cv2.GaussianBlur(gray, (3,3), 0)#잡음제거
#threshold
canny = cv2.Canny(blur, 75, 200)#윤곽추축

#컨투어 작업
contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for i in xrange(len(contours)):
   cnt = contours[i]
   print(i)

   area = cv2.contourArea(cnt)#컨투어 영역의 넓이
   rect = cv2.minAreaRect(cnt)#컨투어 영역을 포함한 최소의 사각형을 추출
   box = cv2.boxPoints(rect)#위에서 추출한 사각형의 4개 좌표를 반환(좌표타입은 float)
   box = np.int0(box)  #위에서 추출한 4좌표의 타입을 int로 변환 == int()
   h = box[0][1]-box[1][1]
   w = box[2][0]-box[1][0]
   if w==0:
       continue
   if 1/6 <= h/w <=1/4 and area>=500:  #번호판 추출 조건
       img = cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
       roi = img[box[1][1]:box[0][1], box[1][0]:box[2][0]]#조건에 맞는 컨투어 영역을 잘라서 roi에 저장

res = Image.fromarray(roi)  #로이 영상을 이미지로 변환
text = pytesseract.image_to_string(res,lang='eng')#테스트 추출
print(text)

cv2.imshow('res1', roi)

cv2.waitKey(0)
cv2.destroyAllWindows()
