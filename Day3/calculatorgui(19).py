import tkinter as tk
from tkinter import ttk

def click_button(value):
    current = str(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

window = tk.Tk()
window.title("Calculator")

frame = ttk.Frame(window, padding=10)
frame.grid(row=0, column=0)

entry = ttk.Entry(frame, font=('Arial', 24))
entry.grid(row=0, column=0, columnspan=4, pady=(0, 10), ipady=5)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    action = lambda x=button: click_button(x)

    if button == '=':
        action = calculate
    elif button == 'C':
        action = clear

    ttk.Button(frame, text=button, width=5, command=action).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

frame.grid_columnconfigure((0, 1, 2, 3), weight=1)
frame.grid_rowconfigure((1, 2, 3, 4), weight=1)

window.mainloop()

