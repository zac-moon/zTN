import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("zTN Notes")

text = tk.Text(root)

def on_window_load():
    print('window loaded')
    try:
        with open('savefile.txt', 'r') as file:
            data = file.read()
            text.delete("1.0", tk.END)  
            text.insert("1.0", data)
    except FileNotFoundError:
        print("No save file found.")

def on_window_close():
    datas = text.get("1.0", tk.END)
    with open('savefile.txt', 'w') as file:
        file.write(datas)
    root.destroy()

notebook = ttk.Notebook()

text = tk.Text(root)

text.pack(fill=tk.BOTH, expand=True)

root.protocol("WM_DELETE_WINDOW", on_window_close)
root.protocol('')
root.after(100, on_window_load) 
root.mainloop()