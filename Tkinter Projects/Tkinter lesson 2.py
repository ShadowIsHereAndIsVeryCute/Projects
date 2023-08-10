import tkinter as tk
from tkinter import ttk
def reset_text():
    label['text'] = 'some text'
    entry['state'] = 'enabled'
def button_function():
    entry_text = entry.get()
    label['text'] = entry_text
    entry['state'] = 'disabled'
window = tk.Tk()
window.title('Getting and Settings widgets')

label = ttk.Label(master = window, text = 'Some Text')
label.pack()

entry = ttk.Entry(master= window)
entry.pack()
button = ttk.Button(master= window, text = "button", command= button_function)
button.pack()
button2 = ttk.Button(master= window, text = "button 2", command= reset_text)
button2.pack()

window.mainloop()
