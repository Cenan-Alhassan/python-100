from tkinter import *
import csv
from tkinter import messagebox
import random
from tkinter.simpledialog import askstring


DEFAULT_EMAIL = "sinanhayer@gmail.com"
PASSWORD = "1234"

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    password_list += [random.choice(LETTERS) for _ in range(nr_letters)]
    password_list += [random.choice(SYMBOLS) for _ in range(nr_symbols)]
    password_list += [random.choice(NUMBERS) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

    window.clipboard_clear()
    window.clipboard_append(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

# we have three fields: website, username and password
# when pressing the add button, must extract csv text from entries into a dictionary, which is converted back to csv

FIELD_NAMES = ["website", "email", "password"]
# refer to https://www.geeksforgeeks.org/how-to-save-a-python-dictionary-to-a-csv-file/
# for formatting dict <-> csv conversions

with open("data.csv") as file:
    csv_dict = csv.DictReader(file)
    list_of_dictionaries = [row for row in csv_dict]

    for dict in list_of_dictionaries:
        print(dict)


# add takes entries and appends string to appropriate dictionary key
# the data file is in csv format. Translate it to dictionary and make appends. then convert it back to csv
def add_entries_to_csv():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()

    if website == "" or email == "" or password == "":
        messagebox.showerror(title="ERROR", message="Field empty.")
        return

    confirm_entry = messagebox.askokcancel(title="Confirm Entry", message=f"Website: {website}\nEmail: {email}"
                                                 f"\nPassword: {password}\n\nConfirm entry?")

    website_entry.delete(0, END)
    password_entry.delete(0, END)

    if not confirm_entry:
        return

    list_of_dictionaries.append(
        {"website": website, "email": email, "password": password}
    )

    with open("data.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames=FIELD_NAMES)
        writer.writeheader()
        writer.writerows(list_of_dictionaries)

# ---------------------------- DISPLAY PASSWORD ------------------------------- #


def password_is_correct():
    input = askstring(title="", prompt="Enter Password: ")

    if input == "" or input != PASSWORD:
        return False
    else:
        return True


def display_password():
    if not password_is_correct():
        return

    count = 1
    message = ""
    for dict in list_of_dictionaries:

        message += f"{count}- {dict['website']}, {dict['email']}, {dict['password']}\n\n"

        count += 1

    messagebox.showinfo(title="Passwords", message=message)
    window.clipboard_clear()
    window.clipboard_append(message)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
canvas.grid(column=2, row=1, columnspan=2, padx=(30, 100))

# label objects
website_text = Label(text="Website: ")
website_text.grid(column=1, row=2)

Username_text = Label(text="Email/Username: ")
Username_text.grid(column=1, row=3)

password_text = Label(text="Password: ")
password_text.grid(column=1, row=4)

# entry objects
website_entry = Entry()
website_entry.grid(column=2, row=2, columnspan=2, sticky="ew", padx=(5, 30), pady=3)
website_entry.focus()

username_entry = Entry()
username_entry.grid(column=2, row=3, columnspan=2, sticky="ew", padx=(5, 30), pady=3)
username_entry.insert(0, DEFAULT_EMAIL)

password_entry = Entry()
password_entry.grid(column=2, row=4, sticky="we", padx=5, pady=3)



# button
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=3, row=4, padx=(5, 30), pady=3)

add_button = Button(text="Add", command=add_entries_to_csv)
add_button.grid(column=2, row=5, columnspan=2, sticky="ew", padx=(5, 30), pady=3)

display_button = Button(text="Display Entries", command=display_password)
display_button.grid(column=2, row=6, columnspan=2, sticky="ew", padx=(5, 30), pady=(3, 50))

# canvas logo
my_pas_logo = PhotoImage(file="logo.png")
canvas.create_image((100, 100), image=my_pas_logo)


window.mainloop()