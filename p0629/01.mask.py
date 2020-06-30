# 특정 영역에 Mask를 적용시켜 히스토그램 분석하기.

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img/faker.jpg')

# mask 생성하기
mask = np.zeros(img.shape[:2], np.uint8)
mask[94:251, 223:377] = 255

# 이미지에 mask가 적용된 결과
masked_img = cv2.bitwise_and(img, img, mask=mask)

# 원본 이미지의 histogram
hist_full = cv2.calcHist([img], [1], None, [256], [0, 256])

# mask를 적용한 histogram
hist_mask = cv2.calcHist([img], [1], mask, [256], [0,256])

plt.subplot(221),plt.imshow(img, 'gray'), plt.title('Origimal Image') # plt.subplot(2, 2, 1)
plt.subplot(222),plt.imshow(mask, 'gray'), plt.title('Mask')
plt.subplot(223),plt.imshow(masked_img, 'gray'), plt.title('Masked Image')
# 'gray' 부분 있으나 없으나 상관이 없음...

plt.subplot(224),plt.title('Histogram')
plt.plot(hist_full, color='r'),plt.plot(hist_mask, color='b')
# color='r' : 빨간줄, color='b' : 파란 줄
plt.xlim([0, 256])

plt.show()