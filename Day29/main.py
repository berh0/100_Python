from tkinter import *
# Actually messagebox is not a class.So we need to import it separately.
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# From Password Generator Project
def generate_password():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(6, 8))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

    # password = ""

    # for char in password_list:
    #   password += char


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure that you haven't left any fields empty.")
    
    else:
        try:
            with open("data.json", "r") as file:
                # Reading old data
                data = json.load(file)
                # Updating old data with new data
                data.update(new_data)
        
        except FileNotFoundError:
            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(new_data, file, indent=4)

        else:    
            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)

        finally:        
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- SEARCH ------------------------------- #

def search():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No Data File Found.")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=27)
website_entry.grid(column=1, row=1, columnspan=1)
website_entry.focus()
email_entry = Entry(width=27)
email_entry.grid(column=1, row=2, columnspan=1)
email_entry.insert(0, "berham@gmail.com")
password_entry = Entry(width=27)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Generate Password",width=14 ,command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add",width=23, command=save)
add_button.grid(column=1, row=4, columnspan=1)
search_button = Button(text="Search", width=14, command=search)
search_button.grid(column=2, row=1)


window.mainloop()