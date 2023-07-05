import tkinter as tk

root = tk.Tk()
root.title("My Notes")

text = tk.Text(root)
text.pack(fill=tk.BOTH, expand=True)

root.mainloop()