from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- CONSTANTS ------------------------------- #
PAD_XY = 50
PASSWORD_FILE = "data.json"
LOGO_FILE = "logo.png"
DEF_EMAIL = "name@email.com"
LETTERS = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+', ' ']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    rand_letters = ''.join(random.choices(LETTERS, k=nr_letters))
    rand_symbols = ''.join(random.choices(SYMBOLS, k=nr_symbols))
    rand_numbers = ''.join(random.choices(NUMBERS, k=nr_numbers))

    all_chars_gen = rand_letters + rand_symbols + rand_numbers
    generated_password = ''.join(random.sample(all_chars_gen, len(all_chars_gen)))

    password_entry.delete(0, END)
    password_entry.insert(0, generated_password)

    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()
    email_user = email_user_entry.get()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email_user,
            "password": password,
        },
    }

    if (len(website) == 0) or (len(email_user) == 0) or (len(password) == 0):
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open(PASSWORD_FILE, "r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            data = new_data
        finally:
            with open(PASSWORD_FILE, "w") as file:
                json.dump(data, file, indent=4)

            messagebox.showinfo(title="Saved Password", message="Successfully saved password")
            website_entry.delete(0, END)
            email_user_entry.delete(0, END)
            email_user_entry.insert(0, DEF_EMAIL)
            password_entry.delete(0, END)


# ---------------------------- SEARCH ------------------------------- #
def search():
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showwarning(title="Input Needed", message="Please enter a website to look for!")
    else:
        try:
            with open(PASSWORD_FILE, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showerror(title="Error",
                                 message=f"No data found.")
        else:
            if website in data:
                messagebox.showinfo(title=f"{website}",
                                    message=f"Password will be copied to clipboard.\n"
                                            f"Email: {data[website]['email']}\n"
                                            f"Password: {data[website]['password']}")
                pyperclip.copy(data[website]['password'])
            else:
                messagebox.showerror(title="No Password Found",
                                     message=f"No password details found for the website '{website}'")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=PAD_XY, pady=PAD_XY)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file=LOGO_FILE)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)

email_user_label = Label(text="Email/Username: ")
email_user_label.grid(column=0, row=2)

password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

# Entries
website_text = StringVar()
website_entry = Entry(textvariable=website_text)
website_entry.grid(column=1, row=1, sticky="EW")

email_user_text = StringVar()
email_user_entry = Entry(textvariable=email_user_text)
email_user_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_user_entry.insert(0, DEF_EMAIL)

password_text = StringVar()
password_entry = Entry(textvariable=password_text)
password_entry.grid(column=1, row=3, sticky="EW")

# Buttons
search_button = Button(text="Search", command=search)
search_button.grid(column=2, row=1, sticky="EW")

gen_pass_button = Button(text="Generate Password", command=generate_password)
gen_pass_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", command=add_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

# Loop
window.mainloop()
