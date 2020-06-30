import tkinter as tk
import Opencv_Note.p0625.hw.car.main_ui as win
import Opencv_Note.p0625.hw.car.make_widgets as mkw
import Opencv_Note.p0625.hw.car.car_member as car
def main():
    img_path = '../img/c3.jpg'
    root = tk.Tk()
    app = win.AppWindow(root, '800x650+100+100', img_path)
    dao = car.CarMemberDao()
    mkw.make(app, dao)
    app.mainloop()

main()