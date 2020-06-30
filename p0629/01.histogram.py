import cv2
from matplotlib import pyplot as plt

img1 = cv2.imread('img/faker.jpg', 0)   # 0 : gray, 1 : rgb, -1 : origin
img2 = cv2.imread("img/teddy.jpg", 0)

hist1 = cv2.calcHist([img1], [0], None, [256], [0, 256])
hist2 = cv2.calcHist([img2], [0], None, [256], [0, 256])

plt.subplot(221),plt.imshow(img1, 'gray'), plt.title('Red Line')
plt.subplot(222),plt.imshow(img2, 'gray'), plt.title('Green Line')
plt.subplot(223),plt.plot(hist1, color='r'), plt.plot(hist2, color='g')
plt.xlim([0, 256])
plt.show()