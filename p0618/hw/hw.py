import tkinter
from tkinter import *
import cv2
import PIL.Image, PIL.ImageTk
import time
import os

file_idx = 0
fnum = 0

active_fname = ""

def graybtn_clicked():
    global img
    cap = cv2.VideoCapture(0)
    ret, img = cap.read()
    filename = "./image/"+time.strftime("%Y%m%d_%H%M%S")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(filename + ".jpg", img)
    img = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(img))
    w.create_image(0, 0, image=img, anchor=tkinter.NW)
    global active_fname
    active_fname = filename


def colorbtn_clicked():
    global img
    cap = cv2.VideoCapture(0)
    ret, img = cap.read()
    filename = "./image/"+time.strftime("%Y%m%d_%H%M%S")
    cv2.imwrite(filename+".jpg", img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(img))
    w.create_image(0, 0, image=img, anchor=tkinter.NW)
    global active_fname
    active_fname = filename

def get_files():
    global fnum
    global file_idx
    path = "./image"
    file_list = os.listdir(path)
    fnum = len(file_list)
    return file_list

def prebtn_clicked():
    flist = get_files()
    global file_idx
    global fnum
    if fnum==0:
        return
    file_idx-=1
    if file_idx < 0:
        file_idx = fnum-1
    elif file_idx >= fnum:
        file_idx = 0

    global img
    img = cv2.imread("./image/"+flist[file_idx])
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    img = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(img))
    w.create_image(0, 0, image=img, anchor=tkinter.NW)
    global active_fname
    active_fname = "./image/"+flist[file_idx]

def nextbtn_clicked():
    flist = get_files()
    global file_idx
    global fnum
    if fnum == 0:
        return
    file_idx += 1
    if file_idx >= fnum:
        file_idx = 0

    global img
    print(file_idx)
    img = cv2.imread("./image/"+flist[file_idx])
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    img = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(img))
    w.create_image(0, 0, image=img, anchor=tkinter.NW)
    global active_fname
    active_fname = "./image/" + flist[file_idx]

def delbtn_clicked():
    global active_fname
    global img
    os.remove(active_fname)
    flist = get_files()
    img = cv2.imread("./image/" + flist[0])
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    img = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(img))
    w.create_image(0, 0, image=img, anchor=tkinter.NW)
    active_fname = "./image/" + flist[file_idx]


root = Tk()
w = Canvas(root, width=500, height=500, bd=10, bg='white')
w.grid(row=0, column=0, columnspan=5)

cap_gray = Button(width=10, height=2, text="흑백 촬영", command=graybtn_clicked)
cap_gray.grid(row=1, column=0)

cap_color = Button(width=10, height=2, text="컬러 촬영", command=colorbtn_clicked)
cap_color.grid(row=1, column=1)

pre_img = Button(width=10, height=2, text="이전 사진", command=prebtn_clicked)
pre_img.grid(row=1, column=2)

next_img = Button(width=10, height=2, text="다음 사진", command=nextbtn_clicked)
next_img.grid(row=1, column=3)

del_img = Button(width=10, height=2, text="삭제", command=delbtn_clicked)
del_img.grid(row=1, column=4)


root.mainloop()
