from tkinter import *
from tkinter import messagebox
import random
from tkinter.simpledialog import askstring
import json


DEFAULT_EMAIL = "sinanhayer@gmail.com"
PASSWORD = "1234"

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

try:
    with open("data.json", 'r'):
        pass
except FileNotFoundError:
    with open("data.json", "w"):
        pass
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

# add takes entries and appends string to appropriate dictionary key
# the data file is in csv format. Translate it to dictionary and make appends. then convert it back to csv
def add_entries_to_json():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()

    json_entry = {
        website: {
            "email": email,
            "password": password
        }
    }

    if website == "" or email == "" or password == "":
        messagebox.showerror(title="ERROR", message="Field empty.")
        return

    try:
        with open("data.json", 'r') as file:
            # open json as dictionary
            json_dict = json.load(file)
            # update the dictionary
            json_dict.update(json_entry)

    except json.decoder.JSONDecodeError:  # if the json file is empty
        with open("data.json", 'w') as file:
            # dump the dictionary
            json.dump(json_entry, file, indent=4)
        add_entries_to_json()

    else:
        with open("data.json", 'w') as file:
            # dump the dictionary
            json.dump(json_dict, file, indent=4)

        confirm_entry = messagebox.askokcancel(title="Confirm Entry", message=f"Website: {website}\nEmail: {email}"
                                                                              f"\nPassword: {password}\n\nConfirm entry?")

        if not confirm_entry:
            return

        website_entry.delete(0, END)
        password_entry.delete(0, END)

# only asking for confirmation when error is not called
# if error happens, must create file and call function now that file exists
# ---------------------------- DISPLAY PASSWORD ------------------------------- #


def password_is_correct():
    input = askstring(title="", prompt="Enter Password: ")

    if input == "" or input != PASSWORD:
        return False
    else:
        return True


def search_entry():
    if not password_is_correct():
        return

    with open("data.json") as file:
        json_dicts = json.load(file)

    search_input = website_entry.get()
    password = ""

    try:
        password = json_dicts[search_input]['password']
        message = f"Password for {search_input} is {password}"
    except KeyError:
        message = "Entry not found."

    messagebox.showinfo(message=message, title="Searched entry")
    window.clipboard_clear()
    window.clipboard_append(password)


def display_passwords():
    if not password_is_correct():
        return

    count = 1
    message = ""

    try:
        with open("data.json", 'r') as file:
            json_dicts = json.load(file)
    except:
        return

    for name, dict in json_dicts.items():

        message += f"{count}- {name}, {dict['email']}, {dict['password']}\n\n"

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
website_entry.grid(column=2, row=2, sticky="we", padx=5, pady=3)
website_entry.focus()

username_entry = Entry()
username_entry.grid(column=2, row=3, columnspan=2, sticky="ew", padx=(5, 30), pady=3)
username_entry.insert(0, DEFAULT_EMAIL)

password_entry = Entry()
password_entry.grid(column=2, row=4, sticky="we", padx=5, pady=3)



# buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=3, row=4, padx=(5, 30), sticky="ew", pady=3)

search_button = Button(text="Search Password", command=search_entry)
search_button.grid(column=3, row=2, padx=(5, 30), sticky="ew", pady=3)

add_button = Button(text="Add", command=add_entries_to_json)
add_button.grid(column=2, row=5, columnspan=2, sticky="ew", padx=(5, 30), pady=3)

display_button = Button(text="Display Entries", command=display_passwords)
display_button.grid(column=2, row=6, columnspan=2, sticky="ew", padx=(5, 30), pady=(3, 35))

# canvas logo
my_pas_logo = PhotoImage(file="logo.png")
canvas.create_image((100, 100), image=my_pas_logo)


window.mainloop()
