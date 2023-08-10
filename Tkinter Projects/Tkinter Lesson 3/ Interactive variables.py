import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title('Tkinter Variables')
def button():
    print(stringvar.get())
#tk variable
stringvar = tk.StringVar(value= 'start value')


label = ttk.Label(master = window, textvariable= stringvar)
label.pack()
entry = ttk.Entry(master = window, textvariable= stringvar)
entry.pack()
buttonn = ttk.Button(master= window, text = 'button', command= button)

exstringvar = tk.StringVar(value= 'start')
label = ttk.Label(master = window, textvariable= exstringvar)
label.pack()
entry = ttk.Entry(master = window, textvariable= exstringvar)
entry.pack()
entry2 = ttk.Entry(master = window, textvariable= exstringvar)
entry2.pack()
window.mainloop()