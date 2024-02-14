from tkinter import *

root = Tk()

e = Entry(root, width=20, bg="white", fg="dark blue", borderwidth=15)
e.pack()
e.insert(0, "Enter Your Name: ")
# e.get()

def clickone():
    hello = "Hello " + e.get()
    sandesh = Label(root, text=hello)
    sandesh.pack()


myButton = Button(root, text ="Enter your Stck Quote", command= clickone, fg="black", bg="white")
myButton.pack()
root.mainloop()



