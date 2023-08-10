import tkinter as tk
from tkinter import ttk


def create_segment(parent, label_text, button_text):
    frame = ttk.Frame(parent)
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure((0, 1, 2), weight=1, uniform='a')
    ttk.Label(frame, text=label_text).grid(row=0, column=0, sticky='news', padx=10, pady=10)
    ttk.Button(frame, text=button_text).grid(row=0, column=1, sticky='nesw', padx=10, pady=10)

    return frame
class Segment(ttk.Frame):
    def __init__(self, parent, label_text, button_text, exercise_text):
        super().__init__(parent)

        self.rowconfigure(0, weight = 1)
        self.columnconfigure((0,1,2), weight=1, uniform= 'a')
        ttk.Label(self, text = label_text).grid(row= 0, column = 0, sticky='news', padx = 10, pady = 10)
        ttk.Button(self, text = button_text).grid(row = 0, column = 1, sticky = 'nesw', padx = 10, pady = 10)
        self.create_p2(exercise_text).grid(row = 0, column = '2', sticky = 'nesw')
        self.pack(expand = True, fill= 'both')
    def create_p2(self, button_info):
        frame2 = ttk.Frame(self)
        ttk.Entry(frame2).pack(expand = True, fill= 'both')
        ttk.Button(frame2, text = button_info).pack(expand = True, fill= 'both')
        return frame2



window = tk.Tk()
window.title('widgets and return')
window.geometry('400x600')
#create_segment(window, 'label', 'button').pack(expand= True, fill= 'both', padx =10, pady=10)
#create_segment(window, 'label', 'button').pack(expand= True, fill= 'both', padx =10, pady=10)
#create_segment(window, 'label', 'button').pack(expand= True, fill= 'both', padx =10, pady=10)
#create_segment(window, 'label', 'button').pack(expand= True, fill= 'both', padx =10, pady=10)
#create_segment(window, 'label', 'button').pack(expand= True, fill= 'both', padx =10, pady=10)
Segment(window, 'label', 'button', 'coolio')
Segment(window, 'label', 'button', 'coolio')
Segment(window, 'label', 'button', 'coolio')
Segment(window, 'label', 'button', 'coolio')
Segment(window, 'label', 'button', 'coolio')

window.mainloop()