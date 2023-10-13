import tkinter as tk

def display_label():
    label.config(text="Hello World!")

window = tk.Tk()
window.title("Console")
window.geometry("200x300")

label = tk.Label(font=('Arial', 24))
label.pack(pady=20)

button = tk.Button(text="Click Me", command=display_label)
button.pack()

window.mainloop()
