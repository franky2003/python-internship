import tkinter as tk

def lol_label():
    content = float(input_element.get())
    sq = content*2
    label2.config(text=f"Converted value is {sq}kms", font=d_font)

window = tk.Tk()
window.title("Square Calc")
window.geometry("400x200")

c_font = ("algerian", 20)
d_font = ("Lucida Sans", 10)

label1 = tk.Label(text="Enter(Miles)", font=d_font)
label1.grid(row=0, column=0, pady=(10,0), padx=10)

label2 = tk.Label(text="Equal to", font=d_font)
label2.grid(row=1, column=0, pady=(0,10), padx=10)

input_element = tk.Entry()
input_element.grid(row=0, column=1, pady=(10,0), padx=10)

button = tk.Button(window, text="Submit", font=d_font, command=lol_label)
button.grid(row=1, column=1, pady=(0,20), padx=20)

window.mainloop()
