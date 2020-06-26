"""
Image Filtering
이미지에서의 고주파 : 밝기의 변화가 많은 곳
저주파 : 일반적인 배경
- 고주파를 제거 : Blur 처리
- 저주파를 제거 : 대상 영역을 확인
"""

# kernel 사이즈를 조정하면서 결과를 확인
import cv2
import numpy as np

def nothing(x):
    pass

img = cv2.imread('images/legend.jpg')

cv2.namedWindow('image')
cv2.createTrackbar('K', 'image', 1, 20, nothing)

while (1):
    if cv2.waitKey(1) & 0xFF == 27:  # esc
        break
    k = cv2.getTrackbarPos('K', 'image')

    # (0, 0)이면 에러가 발생함으로 1로 치환
    if k == 0:
        k = 1

    # trackbar에 의해 (1, 1) ~ (20, 20) kernel 생성
    # kernel : 행렬
    # kernel의 크기가 크면 이미지 전체가 blur 처리가 많아짐

# 픽셀의 R, G, B 값 각각을 커널을 통해 값을 변형하여 blur 처리를 진행한다고 한다.
# - 커널 사이즈가 커지면 이미지가 점점 흐려진다.
# - 이미지 영역이 커지면서 그 영역 간의 색을 비슷하게 만들기 때문인듯하다.

    kernel = np.ones((k, k), np.float32) / (k**2)
    dst = cv2.filter2D(img, -1, kernel)

    cv2.imshow('image', dst)

cv2.destroyAllWindows()
