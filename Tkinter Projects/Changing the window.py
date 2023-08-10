import tkinter as tk
from tkinter import ttk
from random import choice


window = tk.Tk()
window.title('More on the window')

window.iconbitmap('PrepareToSuffer.ico')

x = window.winfo_screenwidth()/2
y = window.winfo_screenheight()/2
window.geometry()
#window sizes
window.minsize(200, 100)
window.resizable(True, True)

#Screen Atrributes
print(window.winfo_screenwidth())
print(window.winfo_screenheight())

#Window Atrributes
window.attributes('-alpha', 1)
window.bind('<Escape>', lambda event: window.quit())
#window.attributes('-fullscreen', True)
window.overrideredirect(True)
size = ttk.Sizegrip(window)
size.place(relx = 1.0, rely = 1.0, anchor = 'se')



window.mainloop()