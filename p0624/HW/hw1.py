import cv2
from pytesseract import *

img = cv2.imread('img/c2.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), -1)
edged = cv2.Canny(gray, 100, 200)

contours, hierarchy = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for i in range(len(contours)):
    cnt = contours[i]
    area = cv2.contourArea(cnt) # contour line의 면적
    x, y, w, h = cv2.boundingRect(cnt) # contour area를 포함한 최소의 사각형
    rect_area = w*h
    aspect_ratio = float(w)/h   # ratio = width/height

    box1 = []


    if aspect_ratio >= 3 and aspect_ratio <= 4:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 1)
        roi = img[y:y+h, x:x+w]

        txt = image_to_string(roi, lang='kor')
        if len(txt)>=8:
            print(txt.strip())
            cv2.imshow('roi', img)
            cv2.waitKey(0)
            break
