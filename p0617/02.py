import cv2



capture = cv2.VideoCapture(0)
ret, frame = capture.read()
# ret : 정상적으로 읽었다면 True, 아니면 False / frame : 영상
print(frame.shape)
# (480, 640, 3)
cv2.imshow('b', frame)
cv2.imwrite('test1.jpg', 0)
cv2.waitKey(0)
cv2.destroyAllWindows()