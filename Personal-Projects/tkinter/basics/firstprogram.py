import tkinter as tk

# Create window
root = tk.Tk()
root.title("Canvas Test")

# Create and pack the canvas
C = tk.Canvas(root, bg="red", width=300, height=300)
C.pack()

# Draw a blue rectangle
C.create_rectangle(50, 50, 250, 250, fill="blue")

# Force an update to refresh the drawing on macOS
root.update_idletasks()

root.mainloop()
 