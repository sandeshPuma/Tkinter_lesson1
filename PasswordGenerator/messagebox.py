from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("sandesh msg box")

# showinfo showwarning yesno askquestion askokcancel askyesno askyesnocancel


# def popup():
#     response = messagebox.askyesno("This is my popup", "Hello World")
#     if response == 1:
#         Label(root, text="you've clicked yes!!").pack()
#     else:
#         Label(root, text="You've clicked no!!!").pack()


# def popup():
#     response = messagebox.askokcancel("This is my popup", "Hello World")
#     if response == 1:
#         Label(root, text="you've clicked yes!!").pack()
#     else:
#         Label(root, text="You've clicked no!!!").pack()


def popup():
    response = messagebox.showinfo("This is my popup", "Hello World")
    if response == 1:
        Label(root, text="you've clicked yes!!").pack()
    else:
        Label(root, text="You've clicked no!!!").pack()


Button(root, text="popupBox", command=popup).pack()


root.mainloop()
