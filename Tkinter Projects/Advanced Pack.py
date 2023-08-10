import tkinter as tk
from tkinter import ttk
from random import choice


window = tk.Tk()
window.title('Advanced Pack')
window.geometry('600x400')
window.iconbitmap('PrepareToSuffer.ico')

label1 = ttk.Label(window, text= 'eeeeeeeee', background= 'black')
label2 = ttk.Label(window, text= 'eeeeeeeee', background= 'green')
label3 = ttk.Label(window, text= 'eeeeeeeee', background= 'blue')
label4 = ttk.Label(window, text= 'eeeeeeeee', background= 'red')

#Pack payout
label1.pack(side= 'left', expand= True, fill= 'both')
label2.pack(side= 'top', expand= True, fill= 'both')
label3.pack(side= 'top', expand= True, fill= 'both')
label4.pack(side= 'top', expand= True, fill= 'both')
window.mainloop()