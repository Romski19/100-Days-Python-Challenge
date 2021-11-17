from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = input_website.get()
    username = input_username.get()
    password = input_password.get()
    with open("password.txt", "a+") as save_passwords:
        # save_passwords.seek(0)
        # data = save_passwords.read(2000)
        # if len(data) > 0:
        #     save_passwords.write("\n")
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

btn_generate = Button(text="Generate Password")
btn_generate.grid(column=2, row=3, sticky="EW")

btn_add = Button(text="Add", width=36, command=save_password)
btn_add.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
