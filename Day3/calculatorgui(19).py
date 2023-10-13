import tkinter as tk
from tkinter import ttk

def add():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result.set(num1 + num2)

def subtract():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result.set(num1 - num2)

def multiply():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result.set(num1 * num2)

def divide():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result.set(num1 / num2)

window = tk.Tk()
window.title("Calculator")
window.geometry("500x250")


entry1 = ttk.Entry(window)
entry2 = ttk.Entry(window)

result = tk.StringVar()

result_label = ttk.Label(textvariable=result)

add_button = ttk.Button(text="+", command=add)
subtract_button = ttk.Button(text="-", command=subtract)
multiply_button = ttk.Button(text="*", command=multiply)
divide_button = ttk.Button(text="/", command=divide)

entry1.grid(row=1, column=0, padx=10, pady=10)
entry2.grid(row=1, column=2, padx=10, pady=10)
result_label.grid(row=2, column=0, columnspan=2, pady=10)
add_button.grid(row=3, column=0, padx=5, pady=5)
subtract_button.grid(row=3, column=1, padx=5, pady=5)
multiply_button.grid(row=4, column=0, padx=5, pady=5)
divide_button.grid(row=4, column=1, padx=5, pady=5)

window.mainloop()