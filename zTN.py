import tkinter as tk

root = tk.Tk()
root.title("My Notes")

text = tk.Text(root)
text.pack(fill=tk.BOTH, expand=True)

def on_window_load():
    print('window loaded')
    try:
        with open('savefile.txt', 'r') as file:
            data = file.read()
            text.delete("1.0", tk.END)  # Clear the Text widget
            text.insert("1.0", data)
    except FileNotFoundError:
        print("No save file found.")

def on_window_close():
    datas = text.get("1.0", tk.END)
    with open('savefile.txt', 'w') as file:
        file.write(datas)
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_window_close)
root.after(100, on_window_load)  # Call after GUI setup
root.mainloop()
