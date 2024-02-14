from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("sandesh hero")

FRUITS = [
    ("Banana ", "Banana "),
    ("Apple ", " Apple"),
    ("Orange ", "Orange "),
    ("Onion ", "Onion"),
]


salad = StringVar()
salad.set("Banana")

for text, fruit in FRUITS:
    Radiobutton(root, text=text, variable=salad, value=fruit).pack(anchor=W)


def clicked(value):
    mylabel = Label(root, text = value)
    mylabel.pack()


# radio Buttons
# Radiobutton(root, text="Option One", variable=r, value=1, command=lambda : clicked(r.get())).pack()
# Radiobutton(root, text="Option Two", variable=r, value=2, command=lambda : clicked(r.get())).pack()


myButton = Button(root, text="Click me", command=lambda: clicked((salad.get())))
myButton.pack()

root.mainloop()
