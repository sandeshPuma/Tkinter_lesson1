from tkinter import *
from PIL import Image, ImageTk
import sqlite3


root = Tk()
root.title("sandesh")
root.geometry("400x400")


# databases

# create a db or connect to one

conn = sqlite3.connect('address_book.db') # will create address_book for us

# create cursor
c = conn.cursor()

# Create table

c.execute("""  CREATE TABLE addresses(
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer)""")


# commit changes
conn.commit()

# close connection

conn.close()

root.mainloop()
