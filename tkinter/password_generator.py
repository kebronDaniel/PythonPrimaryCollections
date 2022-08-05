import random
from tkinter import *
from tkinter import messagebox
from string import ascii_letters, digits
import pyperclip

all_symbols = ['!', '@', '#', '$', '%', '^',
               '&', '*', '(', ')', '_' '-', '+', '*']
all_letters = list(ascii_letters)
all_digits = list(digits)

window = Tk()

window.config(padx=50, pady=50)
window.title("Password Manager")

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

website_text = Label(text="Website:")
website_text.grid(row=1, column=0)

website = Entry(width=35)
website.focus()
website.grid(row=1, column=1, columnspan=2)

email_text = Label(text="Email/Username:")
email_text.grid(row=2, column=0)

email = Entry(width=35)
email.insert(0, "kebronjrdaniel@gmail.com")
email.grid(row=2, column=1, columnspan=2)

password_text = Label(text="Password:")
password_text.grid(row=3, column=0)

password = Entry(width=19)
password.grid(row=3, column=1)


def save_password():
    website_data = website.get()
    email_data = email.get()
    password_data = password.get()

    if len(website_data) == 0 or len(password_data) == 0 or len(email_data) == 0:
        messagebox.showerror(title="Empty Fields", message="You have got empty fields, Please fill them out!")
    else:
        is_ok = messagebox.askokcancel(title="Save Password", message=f"Website:{website_data} \n"
                                                                      f"Email:{email_data}\n"
                                                                      f"Password:{password_data}\n"
                                                                      f"Do You want to Save?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website_data}    |   {email_data}   |   {password_data} \n")
                website.delete(0, END)
                password.delete(0, END)

                reset_spans = StringVar(window)
                reset_spans.set("0")

                string_span.config(textvariable=reset_spans)
                number_span.config(textvariable=reset_spans)
                symbol_span.config(textvariable=reset_spans)


string_password_label = Label(text="Number of letters ")
string_password_label.grid(row=4, column=1)

string_span = Spinbox(from_=0, to_=10, width=5)
string_span.grid(row=4, column=2)

number_password_label = Label(text="Number of numerics ")
number_password_label.grid(row=5, column=1)

number_span = Spinbox(from_=0, to_=5, width=5)
number_span.grid(row=5, column=2)

symbol_password_label = Label(text="Number of Symbols ")
symbol_password_label.grid(row=6, column=1)

symbol_span = Spinbox(from_=0, to_=5, width=5)
symbol_span.grid(row=6, column=2)


def custom_password_generator():
    number_of_letters = int(string_span.get())
    number_of_symbols = int(number_span.get())
    number_of_numerics = int(symbol_span.get())

    letters = random.choices(all_letters, k=number_of_letters)
    numbers = random.choices(all_digits, k=number_of_numerics)
    symbols = random.choices(all_symbols, k=number_of_symbols)
    new_password = letters + numbers + symbols

    new_password = "".join(new_password)
    password.insert(0,new_password)
    pyperclip.copy(new_password)


password_generator_button = Button(text="Generate Password", width=12, command=custom_password_generator)
password_generator_button.grid(row=7, column=2)

add_button = Button(text="Add", width=33, command=save_password)
add_button.grid(row=8, column=1, columnspan=2)

def show_help():
    messagebox.showinfo("Help", message="You can either type any password you want in the password field or generate "
                                        "one.\n "
                                        "Once you generate a password, it's automatically copied to the clip board")


help_button = Button(text="Help", command=show_help)
help_button.grid(row=9, column=3)

window.mainloop()
