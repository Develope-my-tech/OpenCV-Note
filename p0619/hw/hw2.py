import cv2

crown = cv2.imread('./hw2/crown.PNG')
bo = cv2.imread('./hw2/jo.jpg')

cascade_file = 'C:\\Users\\Playdata\\Desktop\\opencv-master\\opencv-master\data\\haarcascades\\haarcascade_frontalface_default.xml'
cascade = cv2.CascadeClassifier(cascade_file)
face_list = cascade.detectMultiScale(bo, scaleFactor=1.1, minNeighbors=1, minSize=(150, 150))

if len(face_list) > 0:
    color = (0, 0, 255)
    for face in face_list:
        x, y, w, h = face
        print(x, y, w, h)
        # cv2.rectangle(bo, (x, y), (x + w, y + h), color, thickness=8)

        cw = w //2
        ch = h // 3
        crown = cv2.resize(crown, dsize=(cw, ch), interpolation=cv2.INTER_AREA)

        roix = x + (cw // 2)
        roiy = y - ch
        roi = bo[roiy:roiy + ch, roix:roix + cw]
        # roi : 왕관을 놓을 위치의 박보검 사진

        imgray = cv2.cvtColor(crown, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(imgray, 10, 255, cv2.THRESH_BINARY)
        # 왕관 : 흰색 , 배경 : 검정

        mask_inv = cv2.bitwise_not(mask)
        # cv2.imshow('mask_inv', mask_inv)
        # 왕관 : 검정, 배경 : 흰색

        crown_fg = cv2.bitwise_and(crown, crown, mask=mask)
        img_fg = cv2.bitwise_and(roi, roi, mask_inv)

        dst = cv2.add(crown_fg, img_fg)
        bo[roiy:roiy + ch, roix:roix + cw] = dst

else:
    print("no face")

cv2.imshow('image', bo)
cv2.waitKey(0)
cv2.destroyAllWindows()
