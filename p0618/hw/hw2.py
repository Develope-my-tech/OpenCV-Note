import tkinter
from tkinter import *
import time
from tkinter import ttk

import cv2
import os


def capture():
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    filename = "./video/" + time.strftime("%Y%m%d_%H%M%S") + ".avi"
    out = cv2.VideoWriter(filename, fourcc, 20, (640, 480))

    while cap.isOpened():
        ret, img = cap.read()

        if ret:
            img = cv2.flip(img, 1)  # 1: 좌우 반전
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # img : r, g, b 3채널이 아닌 밝기를 나타내는 값 0 ~ 255 만 가짐
            img = cv2.merge([img, img, img])
            # r, g, b 를 똑같은 밝기 [b, b, b]로 설정해서 3개의 채널로 설정
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
