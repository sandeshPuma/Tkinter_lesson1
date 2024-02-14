from tkinter import *
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt
import random

root = Tk()
root.geometry("400x400")


def graph():
    house_prices = np.random.normal(200000, 25000, 5000)
    plt.polar(house_prices)
    plt.show()


btn_one = Button(root, text="Graph It!", command=graph)
btn_one.pack()
root.mainloop()
