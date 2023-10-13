import tkinter as tk
import random
import re

def verify_gmail():
    gmail_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    gmail = entry_gmail.get()
    if re.match(gmail_pattern, gmail):
        return True
    else:
        result_label.config(text="Invalid Gmail ID. Please enter a valid one.")
        return False

def generate_password():
    if not verify_gmail():
        return

    password_length = 16

    letters_count = random.randint(1, 8)
    numbers_count = random.randint(1, 8)
    symbols_count = 16 - letters_count - numbers_count
    
    pswd_list = []
    for i in range(0, letters_count):
        pswd_list += random.choice(letters)
    for i in range(0, numbers_count):
        pswd_list += random.choice(numbers)
    for i in range(0, symbols_count):
        pswd_list += random.choice(symbols)    
    random.shuffle(pswd_list)
    password = "".join(pswd_list)
    result_label.config(text=f"New Password is {password}")

    gmail = entry_gmail.get()

    account_info = {gmail: password}

    file=open("C:/Users/nkgd2/OneDrive/Desktop/Python Course/Day3/account_info.txt", "a")
    file.write(str(account_info) + "\n")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
           'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

window = tk.Tk()
window.title("Password Manager")
window.geometry("500x250")

label_gmail = tk.Label(text="Enter your Gmail ID:")
label_gmail.grid(row=0, column=0, padx=10, pady=10)
entry_gmail = tk.Entry(window)
entry_gmail.grid(row=0, column=1, padx=10, pady=10)

generate_button = tk.Button(text="Generate Password", command=generate_password)
generate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(text="")
result_label.grid(row=3, column=0, columnspan=2, pady=(0,10))

window.mainloop()