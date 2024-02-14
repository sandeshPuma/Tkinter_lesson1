from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("400x400")


def show():
    mylabel = Label(root, text=clicked.get()).pack()


option = [
    "sunday",
    "monday",
    "tuesday",
    "wednesday",
    "thursday",
    "friday",
    "saturday",
]

clicked = StringVar()
clicked.set(option[0])

drop = OptionMenu(root, clicked, *option).pack()


btn = Button(root, text="show selection", command= show).pack()


root.mainloop()
