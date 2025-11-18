import tkinter as tk

root = tk.Tk()

root.geometry("300x300")

root.title("Widgets Example")

# Create a label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()  # Adds it to the window

# Create a button
button = tk.Button(root, text="Click Me")
button.pack()

root.mainloop()
