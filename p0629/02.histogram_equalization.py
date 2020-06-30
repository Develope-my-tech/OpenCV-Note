import cv2
import numpy as np
from  matplotlib import pyplot as plt

img = cv2.imread('img/foggy.jpg')

hist, bins = np.histogram(img.flatten(), 256, [0, 256])

cdf = hist.cumsum()     # cdf의 값이 0인 경우 mask 처리를 하여 계산에서 제외
# print('hist', hist)   # 도수
# print('bins', bins)   # 구분

cdf = hist.cumsum() 	# [1,2,3,4,5,...] => [1,3,6,10....]

cdf_m = np.ma.masked_equal(cdf, 0)
# cdf의 값이 0인 경우는 mask 처리를 하여 계산에서 제외
# mask처리가 되면 Numpy 계산에서 제외가 됨
# 위에는 cdf array에서 값이 0인 부분을 mask 처리

#History Equalization 공식
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())

# Mask 처리를 했던 부분을 다시 0으로 변환
cdf = np.ma.filled(cdf_m,0).astype('uint8')

img2 = cdf[img]
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.subplot(122),plt.imshow(img2),plt.title('Equalization')
plt.show()