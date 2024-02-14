from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("sandesh")
root.iconbitmap('')

frame = LabelFrame(root, pady=50, padx=50)
frame.pack(padx=20, pady=80)

b = Button(frame, text="dont click here!!!")
b2 = Button(frame, text=">>>>> or here!!!")
b.grid(column=5, row=5)
b2.grid(column=10, row=10)

root.mainloop()
