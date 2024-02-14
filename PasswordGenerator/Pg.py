# prompt: to do applications
import string
# Create a random password generator application using the functions defined above.

import tkinter as tk
import secrets

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")

# Create a label to display the generated password
password_label = tk.Label(root, text="Generated Password:")
password_label.pack()

alphabet = string.ascii_letters + string.digits

# Create a function to generate a new password and update the label


def generate_password():
    password_length = 8
    password = ''.join(secrets.choice(alphabet) for i in range(password_length))
    password_label.config(text="Generated Password: " + password)


# Create a button to generate a new password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# Start the main event loop
root.mainloop()
