import tkinter as tk
from tkinter import ttk
from random import choice


window = tk.Tk()
window.title('Advanced Pack')
window.geometry('600x400')
window.iconbitmap('PrepareToSuffer.ico')

label1 = ttk.Label(window, text = 'label 1', background= 'red')
label2 = ttk.Label(window, text = 'label 2', background= 'blue')
label3 = ttk.Label(window, text = 'label 3', background= 'orange')

Button1 = ttk.Button(window, text = 'Raise lable one', command= lambda: label1.tkraise(aboveThis= label2))
Button2 = ttk.Button(window, text = 'Raise lable two', command= lambda: label2.tkraise())
Button3 = ttk.Button(window, text = 'Raise lable three', command= lambda: label3.tkraise())


label1.place(x = 50, y=100, width=200, height= 150)
label2.place(x = 150, y=60, width=140, height= 100)
label3.place(x = 130, y=70, width=140, height= 100)


Button1.place(rely = 1, relx = 0.6, anchor= 'se')
Button2.place(rely = 1, relx =0.8, anchor= 'se')
Button3.place(rely = 1, relx =1, anchor= 'se')











window.mainloop()