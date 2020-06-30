import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img/cake.jpg', 0)
img2 = img.copy()
template = cv2.imread('img/cake_straw.PNG', 0)

# template 이미지의 가로/세로
w, h = template.shape[::-1]

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED','cv2.TM_SQDIFF','cv2.TM_SQDIFF_NORMED']

for meth in methods:
    img = img2.copy()
    method = eval(meth)

    # matchTemplate(원본 이미지, 템플릿 이미지, 템플릿 매칭 플래그)
    # 원본이미지, 템플릿 이미지 = 8비트의 단일 채널 이미지지
    # 결과값 = 32 비트의 단일 채널 이미지 (계산값이기 때문에 float 형태로 들어가서 그런듯 하다.)
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(img, top_left, bottom_right, 255, 5)

    plt.subplot(121), plt.title(meth), plt.imshow(res, cmap='gray'), plt.yticks([]), plt.xticks([])
    plt.subplot(122), plt.imshow(img, cmap='gray')
    plt.show()