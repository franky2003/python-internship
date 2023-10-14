import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def remove_task():
        index = listbox.curselection()
        listbox.delete(index)

def mark_completed():
        index = listbox.curselection()
        if index:
            listbox.itemconfig(index, {'bg':'light green'})

window = tk.Tk()
window.title("To-Do List")

listbox = tk.Listbox(window, width=50, height=10)
listbox.pack(pady=10)

entry = tk.Entry(window, width=50)
entry.pack(pady=10)

add_button = tk.Button(text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=5)
remove_button = tk.Button(text="Remove Task", command=remove_task)
remove_button.pack(side=tk.LEFT, padx=5)
complete_button = tk.Button(text="Mark Completed", command=mark_completed)
complete_button.pack(side=tk.LEFT, padx=5)

window.mainloop()