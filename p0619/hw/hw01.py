import tkinter
from tkinter import *
import time
from tkinter import ttk

import cv2
import os

def captureFace(img):
    cascade_file = 'C:\\Users\\Playdata\\Desktop\\opencv-master\\opencv-master\data\\haarcascades\\haarcascade_frontalface_default.xml'
    cascade = cv2.CascadeClassifier(cascade_file)
    face_list = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=1, minSize=(150, 150))

    if len(face_list) > 0:
        color = (0, 0, 255)
        for face in face_list:
            x, y, w, h = face
            cv2.rectangle(img, (x, y), (x + w, y + h), color, thickness=8)
            cv2.imwrite("./face/"+time.strftime("%Y%m%d_%H%M%S")+".jpg", img)
    else:
        print("no face")


def capture():
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    filename = "./video/" + time.strftime("%Y%m%d_%H%M%S") + ".avi"
    out = cv2.VideoWriter(filename, fourcc, 50, (640, 480))

    while cap.isOpened():
        ret, img = cap.read()

        if ret:
            img = cv2.flip(img, 1)  # 1: 좌우 반전
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = cv2.merge([img, img, img])
            captureFace(img)

            out.write(img)
            cv2.imshow('recording..', img)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                out.release()
                break
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()


def rbtn_clicked(idx):
    cap = cv2.VideoCapture('./video/' + flist[idx])
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv2.imshow('output', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            cap.release()
            cv2.destroyAllWindows()


def play():
    def click():
        form.destroy()
        rbtn_clicked(rVar.get())

    global flist
    flist = os.listdir("./video")

    form = tkinter.Toplevel()
    # 응용 프로그램의 창, 창을 닫으면 하위 위젯이 삭제되지만 프로그램은 종료되지 않습니다.
    rVar = tkinter.IntVar()
    rbutton = []

    for i in range(len(flist)):
        rbutton.append(ttk.Radiobutton(form, text=flist[i], variable=rVar, value=i, command=click))
        rbutton[i].grid(row=i, column=0)

    form.mainloop()


root = Tk()
# 응용 프로그램의 절대 루트, gui는 파기될 때 종료
flist = os.listdir("./video")

cap_btn = Button(width=10, height=2, text="흑백 촬영", command=capture)
cap_btn.grid(row=1, column=0)

play_btn = Button(width=10, height=2, text="보기", command=play)
play_btn.grid(row=1, column=1)

root.mainloop()
