import tkinter as tk

root = tk.Tk()
root.title("zTN Notes")
root.geometry('600x400')

text = tk.Text(root,font=('Arial',45))

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

text.pack(fill=tk.BOTH, expand=True)

root.protocol("WM_DELETE_WINDOW", on_window_close)
root.after(100, on_window_load) 
root.mainloop()