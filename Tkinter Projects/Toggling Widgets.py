import tkinter as tk
from tkinter import ttk
from random import choice
def toggle_label_place():
    global label_visibility

    if label_visibility:
        label.place_forget()
        label_visibility = False
    else:
        label_visibility = True
        label.place(relx=0.5, rely=0.5, anchor='center')



window = tk.Tk()
window.title('Advanced Pack')
window.geometry('600x400')
window.iconbitmap('PrepareToSuffer.ico')

#place method
button = ttk.Button(window, text='toggle label', command= toggle_label_place)
button.place(x = 10, y= 10)
label_visibility = True
label = ttk.Label(window, text= 'a label')
label.place(relx=0.5,rely=0.5,anchor= 'center')



window.mainloop()