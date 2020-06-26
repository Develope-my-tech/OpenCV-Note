"""
- Perspective(원근법) 변환 : 직선의 성질만 유지, 선의 평행성은 유지 되지 않는 변환
- 기차길을 서로 평행하지만 원근 변환을 거치면 평행성은 유지가 되지 못하고,
하나의 점에서 만나는 것처럼 보인다.
- 4개의 Point의 input 값과 이동할 output Point가 필요
- cv2.getPerspectiveTransform() : 반환 행렬을 구하기 위한 함수
- cv2.warpPerspective() : 변환 행렬 값을 적용하여 최종 결과 이미지를 얻는 함수
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/test1.jpg')
# [x, y] 좌표점을 4 * 2 행렬로 작성

# 이동할 좌표
pts1 = np.float32([[504,1003],[243,1525],[1000,1000],[1280,1685]])

pts2 = np.float32([[10,10],[10,1000],[1000,10],[1000,1000]])

# pts1의 좌표에 표시. perspective 변환 후 이동 점 확인.
cv2.circle(img, (504,1003), 20, (255,0,0),-1)
cv2.circle(img, (243,1524), 20, (0,255,0),-1)
cv2.circle(img, (1000,1000), 20, (0,0,255),-1)
cv2.circle(img, (1280,1685), 20, (0,0,0),-1)

M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(img, M, (1100, 1100))

plt.subplot(121),plt.imshow(img),plt.title('image')
plt.subplot(122),plt.imshow(dst),plt.title('Perspective')
plt.show()