from tkinter import *
from PIL import Image, ImageTk
import mysql.connector


root = Tk()

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "password123",
)
print(mydb)

root.mainloop()
