import tkinter as tk
import random

def generate_password():
    letters_count = int(entry.get())
    numbers_count=int(entry1.get())
    symbols_count=int(entry2.get())
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

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

window = tk.Tk()
window.title("Password Generator")
window.geometry("500x250")
label = tk.Label(window, text="How many letters would you like in your password?")
label.grid(row=0, column=0, padx=10, pady=10)
label = tk.Label(window, text="How many numbers would you like in your password?")
label.grid(row=1, column=0, padx=10, pady=10)
label = tk.Label(window, text="How many symbols would you like in your password?")
label.grid(row=2, column=0, padx=10, pady=10)

entry = tk.Entry(window)
entry.grid(row=0, column=1, padx=10, pady=10)
entry1 = tk.Entry(window)
entry1.grid(row=1, column=1, padx=10, pady=10)
entry2 = tk.Entry(window)
entry2.grid(row=2, column=1, padx=10, pady=10)

generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(window, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=(0,10))

window.mainloop()


