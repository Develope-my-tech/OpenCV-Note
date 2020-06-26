'''
affine transformation
선의 평행선은 유지가 되면서 이미지를 변환하는 작업
이동, 확대, scale, 반전까지 포함된 변환
3개의 Match가 되는 점이 있으면 변환 행렬을 구할 수 있습니다.
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/legend.jpg')
row, col, ch = img.shape

pts1 = np.float32([[200, 100], [400, 100], [200, 200]])
pts2 = np.float32([[200, 300], [400, 200], [200, 400]])

# pts1의 좌표에 표시. affine 변환 후 이동 점 확인
cv2.circle(img, (200, 100), 10, (255, 0, 0), -1)
cv2.circle(img, (400, 100), 10, (0, 255, 0), -1)
cv2.circle(img, (200, 200), 10, (0, 0, 255), -1)

M = cv2.getAffineTransform(pts1, pts2)
# print(M)
# [[  1.    0.    0. ]
#  [ -0.5   1.  300. ]]

dst = cv2.warpAffine(img, M, (col, row))    # 변환된 이미지

plt.subplot(121), plt.imshow(img), plt.title('image')
plt.subplot(122), plt.imshow(dst), plt.title('Affine')
plt.show()
