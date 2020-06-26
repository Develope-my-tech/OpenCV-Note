import tkinter as tk
from tkinter import messagebox
import time, os

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry('200x400+300+300')#윈도우창 크기 1600*900, 위치:100,100
        self.master.resizable(True, True)
        self.pack()
        self.mode = tk.IntVar()
        self.fname = ''
        self.create_widgets()
        

    def create_widgets(self):
        self.mode_c = tk.Radiobutton(self, text='촬영모드', variable=self.mode, value=1)
        self.mode_c.pack()
        self.mode_c.invoke()
        
        self.mode_p = tk.Radiobutton(self, text='보기모드', variable=self.mode, value=2)
        self.mode_p.pack()
        
        self.btn1 = tk.Button(self, width=20, font=40, text='칼라모드촬영')
        self.btn1.pack()

        self.btn2 = tk.Button(self, width=20, font=40, text='흑백모드촬영')
        self.btn2.pack()

        self.btn3 = tk.Button(self, width=20, font=40, text='이전사진')
        self.btn3.pack()

        self.btn4 = tk.Button(self, width=20, font=40, text='다음사진')
        self.btn4.pack()

        self.btn5 = tk.Button(self, width=20, font=40, text='삭제')
        self.btn5.pack()

        self.file_l = tk.Label(self, width=20, font=40, text='파일명:')
        self.file_l.pack()
        self.file_e = tk.Entry(self, width=30)
        self.file_e.pack()


class Main:
    def __init__(self):
        self.app = Application(master=tk.Tk())

    def run(self):
        self.app.mainloop()

def main():
    m = Main()
    m.run()

main()



