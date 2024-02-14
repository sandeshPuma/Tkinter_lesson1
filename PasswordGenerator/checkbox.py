from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("sandesh box")
root.geometry("1920x1080")


def show():
    mylabel = Label(root, text = var_one.get()).pack()


# using int var to make sure checkbox gets to a number
# var_one = IntVar()
var_one = StringVar()

box_one = Checkbutton(root, text="this is checkbox", variable=var_one, onvalue="sandesh", offvalue="sachin")
box_one.deselect()
box_one.pack()

# command to show the var
myButton = Button(root, text="show selection", command=show).pack()

root.mainloop()
