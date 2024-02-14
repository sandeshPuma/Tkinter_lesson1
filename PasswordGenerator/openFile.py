from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog


root = Tk()

# get image location
# my_label = Label(root, text=root.filename).pack()
# filedialog is only opening location

def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir="D:/python/new Lesson/icon",
                                               title="Select A file",
                                               filetypes=(("jpeg files", "*.jpeg"), ("all files", "*.*")))
    # open images using folder
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()


my_button = Button(root, text="Open file", command=open).pack()
exit_button = Button(root, text="Exit file", command=root.quit).pack()

root.mainloop()


