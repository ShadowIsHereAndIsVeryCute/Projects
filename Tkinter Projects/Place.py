import tkinter as tk
from tkinter import ttk
from random import choice


window = tk.Tk()
window.title('Advanced Pack')
window.geometry('600x400')
window.iconbitmap('PrepareToSuffer.ico')


label1 = ttk.Label(window, text = 'First label', background= 'red')
label2 = ttk.Label(window, text = 'Label 2', background= 'blue')
label3 = ttk.Label(window, text = 'third label', background= 'orange')
button1 = ttk.Button(window, text='button 1')

label1.place(x = 0, y= 0)

window.mainloop()