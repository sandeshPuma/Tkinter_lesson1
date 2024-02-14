from tkinter import *

root = Tk()


# Creating a label widget
sandesh = Label(root, text="Hello to my world world!")
sandesh2 = Label(root, text="Hello to my world i am sandesh")
sandesh3 = Label(root, text="                        ")

# Shoving it in onto the screen


sandesh.grid(row=0, column=0)
sandesh2.grid(row=1, column=1)
sandesh3.grid(row=1, column=5)


# sandesh.pack()


root.mainloop()



