from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Learn Sandesh Learn")
root.iconbitmap('D:/python/new Lesson/icon/apple.ico')


image_1 = ImageTk.PhotoImage(Image.open("D:/python/new Lesson/icon/domain.png"))
my_label = Label(image = image_1)
my_label.pack()


button_quit = Button(root, text="Exit", padx=200, pady=10, command=root.quit)
button_quit.pack()


root.mainloop()
