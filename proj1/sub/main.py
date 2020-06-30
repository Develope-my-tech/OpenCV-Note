import tkinter as tk
import Opencv_Note.proj1.sub.main_ui as ui
import Opencv_Note.proj1.sub.make_widgets as mkw
import Opencv_Note.proj1.sub.obj_detect_service as ds

def main(service):
    img_path = 'imgs/a.jpg'
    root = tk.Tk()
    app = ui.Application(master=root,size='650x500+100+100', img_path=img_path)
    d_service = ds.DetectService(img_path)
    mkw.make(app, d_service)
    service()
    app.mainloop()

