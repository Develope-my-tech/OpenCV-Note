import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 240)

while (1):
    ret, frame = cap.read()

    if ret:

        # BGR -> HSV로 변환
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # blue 영역을 low_blue ~ upper_blue 로 지정
        low_blue = np.array([110, 50, 50])
        up_blue = np.array([130, 255, 255])

        # blue 영역의 값을 지정
        mask = cv2.inRange(hsv, low_blue, up_blue)

        # blue 영역만 남김
        res = cv2.bitwise_and(frame, frame, mask=mask)

        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        cv2.imshow('res', res)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
