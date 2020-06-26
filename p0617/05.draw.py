# np.uint8 : unsigned int 8 bits --> 0 ~ 255 까지
import numpy as np
import cv2

#모두 0으로 되어 있는 빈 Canvas(검정색)
img = np.zeros((512, 512, 3), np.uint8)
# 512 * 512 크기의 3채널의 그림판

# 선
# img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
# 시작점 : (0, 0), 끝점 : (511, 511), 색깔 : (255, 0, 0), 두께 : 5

# 원
# img = cv2.circle(img, (447,63), 63, (0,0,255), -1)

# 타원
img = cv2.ellipse(img, (256,256), (100,50), 0, 0, 180, 255, -1)

# polygon
# pts = np.array([[10,5], [20,30], [70,20], [50,10]], np.int32) # 각 꼭지점은 2차원 행렬로 선언
# # 이미지에 표현하기 위해 3차원 행렬로 변환. 변환이전과 이후의 행렬 갯수는 동일해야함.
# # -1은 원본에 해당하는 값을 그대로 유지.
# pts = pts.reshape((-1, 1, 2))
# img = cv2.polylines(img, [pts], True, (0,255,255))

# text
# cv2.putText(img, 'OpenCV', (10,500), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 2)


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
