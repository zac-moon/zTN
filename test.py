import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Examples')

# ttk.Notebook widget with tabs
notebook = ttk.Notebook(root)
tab1 = tk.Frame(notebook)
tab2 = tk.Frame(notebook)
tab3 = tk.Frame(notebook)
notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")
notebook.add(tab3,text='Tab 3')
notebook.pack()

lab1 = tk.Label(tab1,text='L1')
lab2 = tk.Label(tab2,text='L2')
lab3 = tk.Label(tab3, text='L3')

labs = ['lab1','lab2','lab3']
for lab in labs:
    globals()[lab].pack()
root.mainloop()
