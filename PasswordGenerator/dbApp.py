from tkinter import *
# from PIL import Image, ImageTk
import sqlite3

root = Tk()

conn = sqlite3.connect("address_book.db")

c = conn.cursor()


# Create table

# c.execute("""  CREATE TABLE addresses(
#         first_name text,
#         last_name text,
#         address text,
#         city text,
#         state text,
#         zipcode integer)""")

def update():
    # Create a db or connect to one
    conn = sqlite3.connect("address_book.db")
    # create a cursor
    c = conn.cursor()


    record_id = delete_box.get()

    c.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode
        
        WHERE oid = :oid""",

              {
                  'first': f_name_editor.get(),
                  'last': l_name_editor.get(),
                  'address': address_editor.get(),
                  'city': city_editor.get(),
                  'state': state_editor.get(),
                  'zipcode': zipcode_editor.get(),

                  'oid': record_id
              })
    # commit changes
    conn.commit()
    # close connection
    conn.close()
    editor.destroy()

# create a edit function to update


def edit():
    global editor
    editor = Tk()
    editor.title("update")
    editor.geometry("400x400")

    # Create a db or connect to one
    conn = sqlite3.connect("address_book.db")
    # create a cursor
    c = conn.cursor()

    record_id = delete_box.get()

    # Query the db
    c.execute("SELECT * FROM addresses where oid =" + record_id)
    records = c.fetchall()

    # print(records)

    # Loop through results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[5]) + " " + "\n"
    # create global var for text box
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor

    # crete text box
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    zipcode_editor = Entry(editor, width=30)
    zipcode_editor.grid(row=5, column=1)

    # create text box labels

    f_name_label = Label(editor, text="First name")
    f_name_label.grid(row=0, column=0, pady=(10, 0))
    l_name_label = Label(editor, text="last name")
    l_name_label.grid(row=1, column=0)
    address_label = Label(editor, text="address")
    address_label.grid(row=2, column=0)
    city_label = Label(editor, text="city")
    city_label.grid(row=3, column=0)
    state_label = Label(editor, text="state name")
    state_label.grid(row=4, column=0)
    zipcode_label = Label(editor, text="zipcode ")
    zipcode_label.grid(row=5, column=0)

    # loop through results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])

    # create an save button
    save_button = Button(editor, text="save records", command=update)
    save_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=132)


# create function to delete a record

def delete():
    # Create a db or connect to one
    conn = sqlite3.connect("address_book.db")
    # create a cursor
    c = conn.cursor()

    c.execute("DELETE from addresses WHERE oid = " + delete_box.get())

    # commit changes
    conn.commit()
    # close connection
    conn.close()


# create submit function for db


def query():
    # Create a db or connect to one
    conn = sqlite3.connect("address_book.db")
    # create a cursor
    c = conn.cursor()

    # Query the db
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    # print(records)

    # Loop through results
    print_records = ''
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + " " + "\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)

    # commit changes
    conn.commit()
    # close connection
    conn.close()


def submit():
    # Create a db or connect to one
    conn = sqlite3.connect("address_book.db")
    # create a cursor
    c = conn.cursor()

    # Insert into Tabel
    c.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                  'f_name': f_name.get(),
                  'l_name': l_name.get(),
                  'address': address.get(),
                  'city': city.get(),
                  'state': state.get(),
                  'zipcode': zipcode.get()
              })

    # commit changes
    conn.commit()
    # close connection
    conn.close()

    # clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)


# crete text box
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)
delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

# create text box labels

f_name_label = Label(root, text="First name")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(root, text="last name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="city")
city_label.grid(row=3, column=0)
state_label = Label(root, text="state name")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="zipcode ")
zipcode_label.grid(row=5, column=0)
delete_box_label = Label(root, text="SELECT ID")
delete_box_label.grid(row=9, column=0, pady=5)

# create submit function

submit_btn = Button(root, text="Add tp the record", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=125)

# Create a Query Button

query_btn = Button(root, text="show records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=137)

# create a delete Button
delete_btn = Button(root, text="Delete records", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=135)

# create an update button
up_button = Button(root, text="Update records", command=edit)
up_button.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=132)

conn.commit()

conn.close()

root.mainloop()
