from tkinter import *
from tkinter import messagebox
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def password_generator():
    # Pre-setting all letters, symbols, and numbers that can be used.
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Setting the required number of letters, symbols, and numbers that can be used for the password.

    password_list = []

    [password_list.append(random.choice(letters)) for _ in range(random.randint(8, 10))]
    [password_list.append(random.choice(symbols)) for _ in range(random.randint(2, 4))]
    [password_list.append(random.choice(numbers)) for _ in range(random.randint(2, 4))]

    random.shuffle(password_list)

    # Join all object sof the list into one string
    password = "".join(password_list)

    # Overwrite old generated password with new one if user doesnt like the old one
    password_input.delete(0, END)
    # Input generate password into password input box
    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_input.get()
    user = user_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "user": user,
            "password": password,
        }
    }

    if len(password) == 0:
        messagebox.showinfo(
            title="Oops, Something's Wrong",
            message="Password field is empty, please include the password")
    elif len(website) == 0:
        messagebox.showinfo(
            title="Oops, Something's Wrong",
            message="Website field is empty, please include the website")
    else:
        try:
            with open("saved_data.json", "r") as saved_data_file:
                # Reading old data
                data = json.load(saved_data_file)
        except FileNotFoundError:
            with open("saved_data.json", "w") as saved_data_file:
                # Saving updated data to json file
                json.dump(new_data, saved_data_file, indent=4)
        else:
            # Update old data with new data
            data.update(new_data)
            with open("saved_data.json", "w") as saved_data_file:
                # Saving updated data to json file
                json.dump(new_data, saved_data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

    messagebox.showinfo(title="Success!", message=f"Added {website} to the data storage")


# ---------------------------- UI SETUP ------------------------------- #

# The Window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Setting the Background image
logo_image = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# TEXT LABELS
#
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)
#
user_label = Label(text="Email/Username: ")
user_label.grid(column=0, row=2)
#
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

# INPUT BOXES
#
website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()
#
user_input = Entry(width=38)
user_input.grid(column=1, row=2, columnspan=2)
user_input.insert(0, "example@gmail.com")
#
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# BUTTONS
#
generate_pw_button = Button(text="Generate Password", command=password_generator)
generate_pw_button.grid(column=2, row=3)
#
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)
#
search_button = Button(text="Search", width=13)
search_button.grid(column=2, row=1)

window.mainloop()
