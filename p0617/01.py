import cv2

fn = 'b.gif'
img = cv2.imread(fn, cv2.IMREAD_COLOR)
# imread : 이미지 파일 읽어오기 , flag = cv2.IMREAD_COLOR
print(img.shape)
# (188, 360, 3)
cv2.imshow('b', img)
# 함수를 사이즈에 맞게 보여줌
cv2.waitKey(0)
# 키가 입력될때까지 wait
cv2.destroyAllWindows()