import tkinter as tk
import Opencv_Note.p0625.hw.car.car_member as mem
from functools import partial

def remove_ent(app):
    app.id_e.delete(0, 'end')
    app.pwd_e.delete(0, 'end')
    app.name_e.delete(0, 'end')
    app.tel_e.delete(0, 'end')
    app.car_e.delete(0, 'end')

def btn1_clicked(app, service, event):
    id = app.id_e.get()
    pwd = app.pwd_e.get()
    name = app.name_e.get()
    tel = app.tel_e.get()
    car_num = app.car_e.get()

    c = mem.CarMember(id, pwd, name, tel, car_num)
    service.insert(c)

    remove_ent(app)

def btn2_clicked(app, service, event):
    if mem.CarMember.login_id != None:
        print('이미 로그인 상태')
        return
    id = app.id_e.get()
    pwd = app.pwd_e.get()
    m = service.select(id)
    if m==None:
        print('없는 아이디')
        return
    if pwd==m.pwd:
        print('로그인 성공')
        mem.CarMember.login_id = id
        app.login_t['text']='login id:'+id
    else:
        print('pwd 불일치')

    remove_ent(app)

def btn3_clicked(app, service, event):
    if mem.CarMember.login_id == None:
        print('먼저 로그인 하시오')
        return
    m = service.select(mem.CarMember.login_id)
    app.id_e.insert(0, m.id)
    app.pwd_e.insert(0, m.pwd)
    app.name_e.insert(0, m.name)
    app.tel_e.insert(0, m.tel)
    app.car_e.insert(0, m.car_num)

def btn4_clicked(app, service, event):
    if mem.CarMember.login_id == None:
        print('먼저 로그인 하시오')
        return

    pwd = app.pwd_e.get()
    tel = app.tel_e.get()
    car_num = app.car_e.get()

    if pwd==None or tel==None or car_num==None:
        print('필수 입력을 모두 입력하시오')
        return
    service.update(mem.CarMember(mem.CarMember.login_id, pwd, '', tel, car_num))
    remove_ent(app)

def logout(app):
    mem.CarMember.login_id = None
    app.login_t['text'] = 'login id:'

def btn5_clicked(app, event):
    if mem.CarMember.login_id == None:
        print('먼저 로그인 하시오')
        return
    logout(app)

def btn6_clicked(app, service, event):
    if mem.CarMember.login_id == None:
        print('먼저 로그인 하시오')
        return
    service.delete(mem.CarMember.login_id)
    logout(app)

def btn7_clicked(app, event):
    remove_ent(app)

def make(app, service=None):
    app.title = tk.Label(app.sub_fr, text='회원정보', font=60)
    app.id_t = tk.Label(app.sub_fr, text='id:', font=60)
    app.id_e = tk.Entry(app.sub_fr, width=60)
    app.pwd_t = tk.Label(app.sub_fr, text='pwd:', font=60)
    app.pwd_e = tk.Entry(app.sub_fr, width=60)
    app.name_t = tk.Label(app.sub_fr, text='name:', font=60)
    app.name_e = tk.Entry(app.sub_fr, width=60)
    app.tel_t = tk.Label(app.sub_fr, text='tel:', font=60)
    app.tel_e = tk.Entry(app.sub_fr, width=60)
    app.car_t = tk.Label(app.sub_fr, text='car number:', font=60)
    app.car_e = tk.Entry(app.sub_fr, width=60)

    app.btn1 = tk.Button(app.sub_fr, width=10, font=60, text='join')
    app.btn2 = tk.Button(app.sub_fr, width=10, font=60, text='login')
    app.btn3 = tk.Button(app.sub_fr, width=10, font=60, text='내정보')
    app.btn4 = tk.Button(app.sub_fr, width=10, font=60, text='수정')
    app.btn5 = tk.Button(app.sub_fr, width=10, font=60, text='logout')
    app.btn6 = tk.Button(app.sub_fr, width=10, font=60, text='탈퇴')
    app.btn7 = tk.Button(app.sub_fr, width=10, font=60, text='clear')
    app.login_t = tk.Label(app.sub_fr, text='login id:', font=60)

    app.title.grid(row=0, column=0, columnspan=3)
    app.id_t.grid(row=1, column=0)
    app.id_e.grid(row=1, column=1, columnspan=2)
    app.pwd_t.grid(row=2, column=0)
    app.pwd_e.grid(row=2, column=1, columnspan=2)
    app.name_t.grid(row=3, column=0)
    app.name_e.grid(row=3, column=1, columnspan=2)
    app.tel_t.grid(row=4, column=0)
    app.tel_e.grid(row=4, column=1, columnspan=2)
    app.car_t.grid(row=5, column=0)
    app.car_e.grid(row=5, column=1, columnspan=2)

    app.btn1.grid(row=6, column=0)
    app.btn2.grid(row=6, column=1)
    app.btn3.grid(row=6, column=2)
    app.btn4.grid(row=7, column=0)
    app.btn5.grid(row=7, column=1)
    app.btn6.grid(row=7, column=2)
    app.login_t.grid(row=8, column=0, columnspan=2)
    app.btn7.grid(row=8, column=2)

    app.btn1.bind('<Button-1>', partial(btn1_clicked, app, service))
    app.btn2.bind('<Button-1>', partial(btn2_clicked, app, service))
    app.btn3.bind('<Button-1>', partial(btn3_clicked, app, service))
    app.btn4.bind('<Button-1>', partial(btn4_clicked, app, service))
    app.btn5.bind('<Button-1>', partial(btn5_clicked, app))
    app.btn6.bind('<Button-1>', partial(btn6_clicked, app, service))
    app.btn7.bind('<Button-1>', partial(btn7_clicked, app))
    # lambda 대신 partial을 사용하는 이유 (https://wikidocs.net/13973)
