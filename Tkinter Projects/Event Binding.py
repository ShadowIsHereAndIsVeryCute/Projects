import tkinter as tk
from tkinter import ttk
def getpos(event):
    print(f'x{event.x} y{event.y}')
window = tk.Tk()
window.title('Event Binding')
window.geometry('600x500')

text = tk.Text(window)
text.pack()

entry = ttk.Entry(window)
entry.pack()

btn = ttk.Button(window,
                 text = 'a button')
btn.pack()

#event
btn.bind('<Alt-KeyPress-a>', lambda event: print('an event'))
window.bind('<Motion>', getpos)
window.bind('<KeyPress>', lambda event: print("A key was pressed" + (f' ({event.char})')))
entry.bind('<FocusIn>', lambda event: print("entry field was selected"))
text.bind('<Shift-MouseWheel>', lambda event: print("fields were met"))
window.mainloop()