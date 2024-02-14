from tkinter import *

root = Tk()


def clickone():
    sandesh = Label(root, text="Look! I clicked a button!!!")
    sandesh.pack()


myButton = Button(root, text ="Click Me!", padx=50, pady = 50, command= clickone, fg="yellow", bg="black")
myButton.pack()
root.mainloop()



