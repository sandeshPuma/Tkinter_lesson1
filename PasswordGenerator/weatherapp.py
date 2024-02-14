from tkinter import *
from PIL import Image, ImageTk
import requests
import json


root = Tk()
root.geometry("600x100")


def countrylookup():
    try:
        response = requests.get("https://api.openaq.org/v1/measurements")
        data = json.loads(response.content)

    except Exception as e:
        params = "error occurred "



country = Entry(root)
country.grid(row=0, column=0, stick= W+E+N+S)

zip_btn = Button(root, text="Lookup country", command= countrylookup)
zip_btn.grid(row=0, column=1, stick= W+E+N+S)

root.mainloop()