from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("sandesh windows")


def openme():
    global my_image
    top = Toplevel()
    top.title("my second window")
    top.iconbitmap("D:/python/new Lesson/icon/apple.ico")
    my_image = ImageTk.PhotoImage(Image.open("D:/python/new Lesson/icon/apple.ico"))
    lbl_One = Label(top, text="sandesh", image=my_image).pack()
    btn2 = Button(top, text= "close window", command=top.quit).pack()


btn = Button(root, text="open second window", command=openme, pady=5, padx=10).pack()
root.mainloop()
