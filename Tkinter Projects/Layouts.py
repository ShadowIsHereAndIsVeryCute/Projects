import tkinter as tk
from tkinter import ttk
from random import choice


window = tk.Tk()
window.title('Pack, Grid and Place')
window.geometry('600x400')
window.iconbitmap('PrepareToSuffer.ico')

#widgets
label1 = ttk.Label(window, text= 'label1', background='red')
label2 = ttk.Label(window, text= 'labe2', background='blue')

#label2.pack(sid='left', expand= True, fill = 'both')
window.columnconfigure(0,weight= 1)
window.columnconfigure(1,weight= 1)
window.columnconfigure(2,weight= 2)
window.rowconfigure(0, weight= 1)
window.rowconfigure(1, weight= 1)

#label1.grid(row = 0, column= 1, sticky= 'nsew')
#label2.grid(row = 1, column= 1,columnspan=2, sticky= 'nsew')
label1.place(x= 0, y=0)
window.mainloop()