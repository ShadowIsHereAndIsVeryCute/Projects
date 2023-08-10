import tkinter as tk
from tkinter import ttk
from random import choice
from tkinter import scrolledtext

window = tk.Tk()
window.title('ComboBox and SpinBox')
window.geometry('600x400')


#frame
frame = ttk.Frame(window, width=100, height=200, borderwidth= 10, relief= tk.RIDGE)
frame.pack(side= 'left')

#Master setting
label = ttk.Label(frame, text = 'label in frame')
frame.pack_propagate(False)
label.pack()

window.mainloop()