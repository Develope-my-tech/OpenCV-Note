import tkinter as tk
from functools import partial

def btn1_clicked(app, service, event):
    print(event)
    flag = service.face_detect()
    if flag:
        app.change_img(service.res)

def btn2_clicked(app, service, event):
    print(event)
    flag = service.eyes_detect()
    if flag:
        app.change_img(service.res)

def btn3_clicked(app, service, event):
    print(event)
    flag = service.smile_detect()
    if flag:
        app.change_img(service.res)

def btn4_clicked(service, event):
    print(event)
    flag = service.smile_detect()
    service.face_recog_train()

def btn5_clicked(app, service, event):
    print(event)
    flag, name = service.face_recog()
    if flag:
        app.ent.insert(0, name)

def make(app, service):
    app.ent = tk.Entry(app.sub_fr, width=60)

    app.btn1 = tk.Button(app.sub_fr, width=10, font=60, text='face detect')
    app.btn2 = tk.Button(app.sub_fr, width=10, font=60, text='eyes detect')
    app.btn3 = tk.Button(app.sub_fr, width=10, font=60, text='smile detect')
    app.btn4 = tk.Button(app.sub_fr, width=10, font=60, text='face train')
    app.btn5 = tk.Button(app.sub_fr, width=10, font=60, text='face recognize')

    app.ent.grid(row=0, column=0, columnspan=5)
    app.btn1.grid(row=1, column=0)
    app.btn2.grid(row=1, column=1)
    app.btn3.grid(row=1, column=2)
    app.btn4.grid(row=1, column=3)
    app.btn5.grid(row=1, column=4)

    app.btn1.bind('<Button-1>', partial(btn1_clicked, app, service))
    app.btn2.bind('<Button-1>', partial(btn2_clicked, app, service))
    app.btn3.bind('<Button-1>', partial(btn3_clicked, app, service))
    app.btn4.bind('<Button-1>', partial(btn4_clicked, service))
    app.btn5.bind('<Button-1>', partial(btn5_clicked, app, service))
