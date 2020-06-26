import cv2, sys

image_file = 'test1.jpg'  # 얼굴 포함된 사진

# CascadeClassifier xml 파일의 경로
cascade_file = 'C:\\Users\\Playdata\\Desktop\\opencv-master\\opencv-master\data\\haarcascades\\haarcascade_frontalface_default.xml'
# haarcascade_frontalface_default.xml
# 판별할 이미지 읽음
image = cv2.imread(image_file)

# 이미지를 흑백처리
image_gs = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# opencv 머신러닝 CascadeClassifier 파일 로드. 학습 데이터 로드
cascade = cv2.CascadeClassifier(cascade_file)
print(cascade)

# 판별할 이미지를 학습 데이터를 기반으로 분석작업.
# param1:판별할 이미지 / param2:스케일값(보통 1~1.5 ) / param3:분석시 판별횟수 기준 / param4: 최소사이즈
# return 값: 결과로 판별된 좌표 리스트. [[x,y,w,h],[x,y,w,h],[x,y,w,h]...]
# x:판별된 부분의 좌측상단의 x좌표 / y:판별된 부분의 좌측상단의 y좌표.
# w:판별된 부분의 가로길이 / h:판별된 부분의 세로길이
face_list = cascade.detectMultiScale(image_gs, scaleFactor=1.1, minNeighbors=1, minSize=(150, 150))

if len(face_list) > 0:

    print(face_list)
    color = (0, 0, 255)
    for face in face_list:
        x, y, w, h = face
        cv2.rectangle(image, (x, y), (x + w, y + h), color, thickness=8)

    cv2.imwrite("res.png", image)

else:
    print("no face")
