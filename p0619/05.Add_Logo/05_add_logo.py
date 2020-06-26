import cv2

img = cv2.imread('05_test.jpg')
logo = cv2.imread('05_opencvlogo.png')

row, cols, channels = logo.shape

# 이미지가 삽입될 위치에 있는 배경을 뽑기위해 크기를 지정
roi = img[200:200+row, 0:cols]

imggray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)

cv2.imshow("imggray", imggray)
cv2.waitKey(0)

ret, mask = cv2.threshold(imggray, 10, 255, cv2.THRESH_BINARY)
# threshold : 임계처리
# 참고 https://opencv-python.readthedocs.io/en/latest/doc/09.imageThresholding/imageThresholding.html

mask_inv = cv2.bitwise_not(mask)

cv2.imshow('mask', mask)
# 검정 바탕에 색이 있는 픽셀은 하얀색
cv2.imshow('mask_inv', mask_inv)
# 하얀 바탕에 색이 있는 픽셀은 검정색

cv2.waitKey(0)

logo_fg = cv2.bitwise_and(logo, logo, mask=mask)
img_fg = cv2.bitwise_and(roi, roi, mask=mask_inv)

cv2.imshow('logo_fg', logo_fg)
cv2.imshow('img_fg', img_fg)
cv2.waitKey(0)

dst = cv2.add(logo_fg, img_fg)

img[200:200+row, 0:cols] = dst

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()