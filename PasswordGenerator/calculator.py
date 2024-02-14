from tkinter import *

root = Tk()
root.title("Simple Calculator")

a = Entry(root, width=35, borderwidth=5)
a.grid(column=0, row=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    # a.delete(0, END)
    current = a.get()
    a.delete(0, END)
    a.insert(0, str(current) + str(number))


def button_clear():
    a.delete(0, END)


def button_add():
    global f_num
    global math
    math = "addition"
    f_num = int(a.get())
    a.delete(0, END)


def button_sub():
    global f_num
    global math
    math = "subtraction"
    f_num = int(a.get())
    a.delete(0, END)


def button_div():
    global f_num
    global math
    math = "division"
    f_num = int(a.get())
    a.delete(0, END)


def button_mul():
    global f_num
    global math
    math = "multiply"
    f_num = int(a.get())
    a.delete(0, END)


def button_equal():
    second_number = a.get()
    a.delete(0, END)
    if math == "addition":
        a.insert(0, f_num + int(second_number))
    if math == "subtraction":
        a.insert(0, f_num - int(second_number))
    if math == "multiply":
        a.insert(0, f_num * int(second_number))
    if math == "division":
        a.insert(0, f_num / int(second_number))


button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_equal = Button(root, text="=", padx=86.5, pady=20, command= button_equal)
button_clear = Button(root, text="clear", padx=78, pady=20, command = button_clear)

button_add = Button(root, text="+", padx=39, pady=20, command=button_add)
button_sub = Button(root, text="-", padx=41, pady=20, command=button_sub)
button_div = Button(root, text="/", padx=41, pady=20, command=button_div)
button_mul = Button(root, text="x", padx=40, pady=20, command=button_mul)

button_1.grid(column=0, row=3)
button_2.grid(column=1, row=3)
button_3.grid(column=2, row=3)

button_4.grid(column=0, row=2)
button_5.grid(column=1, row=2)
button_6.grid(column=2, row=2)

button_7.grid(column=0, row=1)
button_8.grid(column=1, row=1)
button_9.grid(column=2, row=1)

button_0.grid(column=0, row=4)
button_add.grid(column=0, row=5)
button_sub.grid(column=0, row=6)
button_div.grid(column=1, row=6)
button_mul.grid(column=2, row=6)
button_clear.grid(column=1, row=4, columnspan=2)
button_equal.grid(column=1, row=5, columnspan=2)


root.mainloop()
