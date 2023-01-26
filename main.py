from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = password_numbers + password_symbols + password_letters

    random.shuffle(password_list)

    password = "".join(password_list)
    password_en.insert(END, string=password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    new_data = {
        website_en.get(): {
            "email": username_en.get(),
            "password": password_en.get()
        }
    }

    if website_en.get() == "" or password_en.get() == "":
        messagebox.showwarning(message="Fill up everything!", title="ERROR")
        return
    try:
        with open("passwords.json", "r") as passwords:
            data_d = json.load(passwords)
    except:
        with open("passwords.json", "w") as passwords:
            json.dump(new_data, passwords, indent=4)
    else:
        data_d.update(new_data)
        with open("passwords.json", "w") as passwords:
            json.dump(data_d, passwords, indent=4)
    finally:
        website_en.delete(0, END)
        password_en.delete(0, END)
# ---------------------------- SEARCH ------------------------------- #

def search():
    with open("passwords.json") as data_file:
        data = json.load(data_file)
        if website_en.get() in data:
            email = data[website_en.get()]["email"]
            password = data[website_en.get()]["password"]
            messagebox.showinfo(title=website_en.get(), message=f"Email: {email}\nPassword: {password}")



# ---------------------------- GUI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=10, pady=10)

canvas = Canvas(width=200, height=200)
lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(column=2, row=1)

#Buttons
generate_bt = Button(text="Generate Password", command=generate_password)
generate_bt.grid(column=3, row=4)

search_bt = Button(text="Search", command=search)
search_bt.grid(column=3, row=2)

add_bt = Button(text="Add", width=36, command=save)
add_bt.grid(column=2, row=5, columnspan=2)

#Labels
website_label = Label(text="Website:", font=("Arial", 10, "normal"))
website_label.grid(column=1, row=2)

username_label = Label(text="Email/Username:", font=("Arial", 10, "normal"))
username_label.grid(column=1, row=3)

password_label = Label(text="Password:", font=("Arial", 10, "normal"))
password_label.grid(column=1, row=4)

#Entries
website_en = Entry(width=22)
website_en.grid(column=2, row=2)
website_en.focus()

username_en = Entry(width=40)
username_en.insert(0, "theuscosta76@hotmail.com")
username_en.grid(column=2, row=3, columnspan=2)

password_en = Entry(width=22)
password_en.grid(column=2, row=4)

window.mainloop()