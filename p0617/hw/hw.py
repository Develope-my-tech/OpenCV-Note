import os
import cv2
import datetime

path = "./image"
file_list = os.listdir(path)
n = len(file_list)
idx = 0 # 첫번째 파일을 불러옴
cnt = 0

img = cv2.imread(path+"/"+file_list[idx], cv2.IMREAD_COLOR)
cv2.imshow('image', img)

while True:
    k = cv2.waitKey(0) & 0xFF

    if k == ord('n'):
        idx += 1
        if idx == n:
            idx = 0
        img = cv2.imread(path + "/" + file_list[idx], cv2.IMREAD_COLOR)
        cv2.imshow('image', img)
    elif k == ord('p'):
        idx -= 1
        if idx == -1:
            idx = n-1
        img = cv2.imread(path + "/" + file_list[idx], cv2.IMREAD_COLOR)
        cv2.imshow('image', img)
    elif k == ord('c'):
        cap = cv2.VideoCapture(0)
        ret, img = cap.read()
        cv2.imshow('image', img)
    elif k == ord('s'):
        cv2.imwrite(path+'/'+"new"+str(cnt)+".jpg", img)
        cnt += 1
        file_list = os.listdir(path)
        n = len(file_list)
    elif k == ord('q'):
        break

cv2.destroyAllWindows()


