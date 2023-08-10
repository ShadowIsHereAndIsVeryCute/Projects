import tkinter as tk
from tkinter import ttk
from random import choice


window = tk.Tk()
window.title('ComboBox and SpinBox')
window.geometry('600x400')

#tab
notebook = ttk.Notebook(window)
tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1, text = 'yes')
label1.pack()
tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2, text = 'yese')
label2.pack()
tab3 = ttk.Frame(notebook)
b1 = ttk.Button(tab3, text= '2')
b2 = ttk.Button(tab3, text= '3')
l1 = ttk.Label(tab3, text= 'Coolie')
l1.pack()
b1.pack()
b2.pack()

notebook.add(tab1, text= 'tab1')
notebook.add(tab2, text= 'tab2')
notebook.add(tab3, text= 'tab3')
notebook.pack()

window.mainloop()
