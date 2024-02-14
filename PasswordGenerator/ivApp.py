from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("sandesh Image app")
root.iconbitmap("D:/python/new Lesson/icon/apple.ico")


my_img = ImageTk.PhotoImage(Image.open("../icon/rocket.png"))
my_img1 = ImageTk.PhotoImage(Image.open("../icon/mern.png"))
my_img2 = ImageTk.PhotoImage(Image.open("../icon/innovative.png"))
my_img3 = ImageTk.PhotoImage(Image.open("../icon/hosting.png"))
my_img4 = ImageTk.PhotoImage(Image.open("../icon/wordpress.png"))

image_list = [my_img, my_img1, my_img2, my_img3, my_img4]


status = Label(root, text="Image 1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
status.grid(row=0, column=0)

my_label = Label(image=my_img)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global forward_button
    global back_button

    my_label.grid_forget()
    my_label = Label(image = image_list[image_number-1])
    forward_button = Button(root, text=">>", command=lambda: forward(image_number+1))
    back_button = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 5:
        forward_button = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    forward_button.grid(row=1, column=2)
    back_button.grid(row=1, column=0)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, columnspan=3, column=0, sticky=W + E)


def back(image_number, state=DISABLED):
    global my_label
    global forward_button
    global back_button

    my_label.grid_forget()
    my_label = Label(image = image_list[image_number-1])
    forward_button = Button(root, text=">>", command=lambda: forward(image_number+1))
    back_button = Button(root, text="<<", command=lambda: back(image_number-1))

    if image_number == 1:
        back_button = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    forward_button.grid(row=1, column=2)
    back_button.grid(row=1, column=0)

    status = Label(root, text="Image " + str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, columnspan=3, column=0, sticky=W + E)


back_button = Button(root, text="<<", command = back)
ext_button = Button(root, text="Exit", command=root.quit)
forward_button = Button(root, text=">>", command=lambda: forward(2))

ext_button.grid(row=1, column=1)
forward_button.grid(row=1, column=2, pady=10)
back_button.grid(row=1, column=0)
status.grid(row=2, columnspan=3, column=0, sticky=W+E)

root.mainloop()
