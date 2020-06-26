import cv2

img1 = cv2.imread('04_sticky.png')
img2 = cv2.imread('04_sticky2.png')
img3 = cv2.bitwise_and(img1, img2)
img4 = cv2.bitwise_or(img1, img2)
img5 = cv2.bitwise_not(img2)
img6 = cv2.bitwise_xor(img1, img2)

# w, h, c = img1.shape
# img = np.zeros((w*2, h*3, 3), np.uint8)
# imgh = cv2.hconcat(img1, img2)
# cv2.hconcat(img1, img3)
# cv2.hconcat(img4, img5)
# cv2.hconcat(img4, img6)
# cv2.vconcat(img1, img4)

imgh = cv2.hconcat([img1, img2, img3])
imgh2 = cv2.hconcat([img4, img5, img6])

res = cv2.vconcat([imgh, imgh2])

cv2.imshow('img', res)
cv2.waitKey(0)
cv2.destroyAllWindows()