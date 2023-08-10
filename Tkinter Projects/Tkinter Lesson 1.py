import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
def convert():
    km_input = entryInt.get()
    mile_output= km_input * 0.61
    output_label['text'] = mile_output

#Window Creator
window = ttk.Window(themename = 'darkly')
window.title("This Is the title name")
#Size
window.geometry('300x150')
#Title
title_label = ttk.Label(master = window, text= 'Unit Convertor', font= 'Calibri 24 bold')
title_label.pack()
#Input Fields
input_frame = ttk.Frame(master = window)
entryInt = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable= entryInt)
button = ttk.Button(master = input_frame, text= 'Convert', command= convert)
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 15)
#Output Frame

output_label = ttk.Label(
    master = window,
    font= 'Calibri 18',
    text = "Output")
output_label.pack()

# Run the mainloop
window.mainloop()