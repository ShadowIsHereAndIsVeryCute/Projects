import tkinter as tk
from tkinter import ttk
from random import choice
from tkinter import scrolledtext

window = tk.Tk()
window.title('ComboBox and SpinBox')
window.geometry('600x400')
#Slider
scale_float = tk.DoubleVar(value= 15)
scale = ttk.Scale(window,
                  command = lambda value: print(scale_float.get()),
                  from_= 0,
                  to= 50,
                  length= 300,
                  orient= 'horizontal',
                  variable= scale_float)
scale.pack()

# progress bar
progress = ttk.Progressbar(window,
                           variable = scale_float,
                           maximum=50,
                           orient= 'horizontal',
                           mode = 'determinate',
                           length=100)
progress.pack()

#scrolled text
scrolled_text = scrolledtext.ScrolledText(window)
scrolled_text.pack()

window.mainloop()