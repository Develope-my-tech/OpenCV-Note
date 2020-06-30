import cv2
import copy
import os
import numpy as np

class DetectService:
    def __init__(self, src):
        self.classifier = []
        self.src = src
        self.img = None
        self.gray = None
        self.res = None
        self.face = None
        self.trainer_path = 'dataset/trainer.yml'

    def face_detect(self):
        self.classifier.clear()
        self.classifier.append(cv2.CascadeClassifier('classifier/haarcascade_frontalface_default.xml'))
        self.img = cv2.imread(self.src)
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.face = self.classifier[0].detectMultiScale(
            self.gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(20, 20)
        )
        img = copy.deepcopy(self.img)
        for (x, y, w, h) in self.face:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            self.res = img

        if len(self.face)==0:
            print('no face')
            return False

        return True

    def eyes_detect(self):
        flag = self.face_detect()
        if not flag:
            print('no face, no eyes')
            return False

        self.classifier.append(cv2.CascadeClassifier('classifier/haarcascade_eye.xml'))

        img = copy.deepcopy(self.img)
        for (x, y, w, h) in self.face:
            roi_gray = self.gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

        eyes = self.classifier[1].detectMultiScale(
                roi_gray,
                scaleFactor=1.5,
                minNeighbors=10,
                minSize=(5, 5),
            )

        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            self.res = img

        return True

    def smile_detect(self):
        flag = self.face_detect()
        if not flag:
            print('no face, no smile')
            return False

        self.classifier.append(cv2.CascadeClassifier('classifier/haarcascade_smile.xml'))

        img = copy.deepcopy(self.img)
        for (x, y, w, h) in self.face:
            roi_gray = self.gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]

        smile = self.classifier[1].detectMultiScale(
                roi_gray,
                scaleFactor=1.5,
                minNeighbors=15,
                minSize=(25, 25),
            )

        for (xx, yy, ww, hh) in smile:
            cv2.rectangle(roi_color, (xx, yy), (xx + ww, yy + hh), (0, 0, 255), 2)

            self.res = img

        return True

    def face_recog_train(self):
        dataset_path = 'dataset/'
        li = os.listdir(dataset_path)
        persons = [os.listdir(dataset_path+li[0]),os.listdir(dataset_path+li[1])]
        self.classifier.clear()
        self.classifier.append(cv2.CascadeClassifier('classifier/haarcascade_frontalface_default.xml'))

        #pip install opencv-contrib-python
        recognizer = cv2.face.LBPHFaceRecognizer_create()

        samples=[]
        ids=[]
        for id, row in enumerate(persons):
            for p in row:
                img = cv2.imread(dataset_path+li[id]+'/'+p)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                face = self.classifier[0].detectMultiScale(
                    gray,
                    scaleFactor=1.2,
                    minNeighbors=5,
                    minSize=(20, 20)
                )
                for (x, y, w, h) in face:
                    samples.append(gray[y:y+h,x:x+w])
                    ids.append(id)

        recognizer.train(samples, np.array(ids))

        recognizer.write(self.trainer_path)
        print('얼굴 학습 완료')

    def face_recog(self):
        self.classifier.clear()
        self.classifier.append(cv2.CascadeClassifier('classifier/haarcascade_frontalface_default.xml'))

        #pip install opencv-contrib-python
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(self.trainer_path)

        names = ['김태리', '김태희']
        self.img = cv2.imread(self.src)
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.face = self.classifier[0].detectMultiScale(
            self.gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(20, 20)
        )
        res = False
        name = 'no face'
        for (x, y, w, h) in self.face:
            id, confidence = recognizer.predict(self.gray[y:y + h, x:x + w])
            # Check if confidence is less them 100 ==> "0" is perfect match
            if (confidence < 100):
                name = names[id]
                print(name, '/ confidence:', confidence)
                res = True
            else:
                name = "unknown"
                res = False

        print(res,'/',name)
        return res, name


