import tkinter as tk

def greet():
    print("Hello, user!")

root = tk.Tk()

button = tk.Button(root, text="Greet Me", command=greet)
button.pack()

root.mainloop()
