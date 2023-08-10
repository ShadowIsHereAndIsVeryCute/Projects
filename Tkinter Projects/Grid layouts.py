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
label4 = ttk.Label(window, text = 'Label 4', background= 'green')
button1 = ttk.Button(window, text='button 1')
button2 = ttk.Button(window, text='button 2')
entry = ttk.Entry(window)

#grid definition

window.columnconfigure((0,1,2), weight= 1, uniform='a')

window.columnconfigure(3, weight= 2)
window.rowconfigure((0,1,2), weight= 1)

label1.grid(row= 0, column= 1, sticky= 'nesw', columnspan=2)
label2.grid(row= 0, column= 0, sticky= 'nesw')
window.mainloop()


