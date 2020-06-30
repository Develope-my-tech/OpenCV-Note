import tkinter as tk
from PIL import Image
from PIL import ImageTk
import cv2

class Application(tk.Frame):
    def __init__(self, master=None, size=None, img_path=None):
        super().__init__(master)
        self.master = master
        self.master.geometry(size)
        self.master.resizable(True, True)
        self.pack()
        self.src = None
        self.fr = None
        self.sub_fr = None
        self.create_widgets(img_path)

    def make_img(self, path):
        src = cv2.imread(path)
        src = cv2.resize(src, (640, 400))
        img = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        self.src = ImageTk.PhotoImage(image=img)

    def create_widgets(self, img_path):
        self.make_img(img_path)
        self.fr = tk.Label(self.master, image=self.src)
        self.fr.pack()
        self.sub_fr = tk.Frame(self.master)
        self.sub_fr.pack()

    def change_img(self, res):
        res = cv2.resize(res, (640, 400))
        img = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        self.src = ImageTk.PhotoImage(image=img)
        self.fr['image'] = self.src

