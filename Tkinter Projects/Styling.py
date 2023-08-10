import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Styling')
window.geometry('300x400')

style = ttk.Style()
style.configure('new.TButton', background = 'green')
style.map('new.TButton',
	foreground = [('pressed', 'red'),('disabled', 'yellow')])

label = ttk.Label(window, text = 'balballa')
label.pack()

Button = ttk.Button(window, text = 'balballa',style = 'new.TButton')
Button.pack()

window.mainloop()

