"""
Edge detection
- sobel&Scharr Filter : Gaussian smoothing과 미분을 이용한 방법
노이즈가 있는 이미지에 적용하는 것이 좋다. x, y축을 미분하는 방법으로 경계값을 계산
?? ? ?
- Laplacian 함수 : 이미지의 가로 세로에 대한 Gradient를 2차 미분한 값
"""

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('images/dave.jpg')
canny = cv2.Canny(img, 30, 70)

laplacian = cv2.Laplacian(img, cv2.CV_8U)
sobelx = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=3)

images = [img, laplacian, sobelx, sobely, canny]
titles = ['Original', 'Laplacian', 'Sobel X', 'Sobel Y', 'Canny']

for i in range(5):
    plt.subplot(2, 3, i+1),plt.imshow(images[i]),plt.title([titles[i]])
    plt.xticks([]),plt.yticks([])

plt.show()