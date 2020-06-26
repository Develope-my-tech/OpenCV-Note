import cv2
from matplotlib import pyplot as plt

img = cv2.imread("lena.jpg", cv2.IMREAD_COLOR)

b, g, r = cv2.split(img)
# img 파일을 b, g, r로 분리

img2 = cv2.merge([r, g, b])
# b, r을 바꿔서 merge
# matplot은 r, g, b 이기때문에
# [g, b, r] : 파랑색
# [r, g, b] : 빨강
# [b, g, r] : 파랑

plt.imshow(img2)
plt.xticks([])
plt.yticks([])
plt.show()