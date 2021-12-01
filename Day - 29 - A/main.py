from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    if input_password.index("end") == 0:
        input_password.insert(0, password)
        pyperclip.copy(password)
    else:
        input_password.delete(0, END)
        input_password.insert(0, password)
        pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = input_website.get()
    username = input_username.get()
    password = input_password.get()

    if input_website.index("end") == 0 or input_password.index("end") == 0:
        messagebox.showerror(title="Empty Entry", message="Please don't leave empty entries")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the entries you have entered: \nEmail:{username} \nPassword:{password} \nIs it ok to save?")

        if is_ok:
            with open("password.txt", "a+") as save_passwords:
                save_passwords.write(f"{website} | {username} | {password}\n")
            input_website.delete(0, END)
            input_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)
# Logo
canvas = Canvas(height=200, width=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# labels

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry (textbox)

input_website = Entry(width=35)
input_website.grid(column=1, row=1, columnspan=2, sticky="EW")
input_website.focus()

input_username = Entry(width=35)
input_username.grid(column=1, row=2, columnspan=2, sticky="EW")
input_username.insert(0, "romeoramosa@gmail.com")

input_password = Entry(width=21)
input_password.grid(column=1, row=3, sticky="EW")

# buttons

btn_generate = Button(text="Generate Password", command=generate_password)
btn_generate.grid(column=2, row=3, sticky="EW")

btn_add = Button(text="Add", width=36, command=save_password)
btn_add.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
