import tkinter as tk

def show_text():
    user_input = entry.get()
    print("You typed:", user_input)

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Show Input", command=show_text)
button.pack()

root.mainloop()
