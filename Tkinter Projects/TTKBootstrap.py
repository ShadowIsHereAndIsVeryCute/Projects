import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk
from PIL import Image
Image.CUBIC = Image.BICUBIC
from ttkbootstrap.scrolled import ScrolledFrame
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.tooltip import ToolTip
from ttkbootstrap.widgets import DateEntry
from ttkbootstrap.widgets import Floodgauge
from ttkbootstrap.widgets import Meter

# window
window = ttk.Window(themename= 'darkly')
window.title('ttk bootstrap intro')
window.geometry('400x300')
window.minsize(700,700)

#scroll frame
scroll_frame = ScrolledFrame(window)
scroll_frame.pack(expand= True, fill= 'both')

#Toaster
toast = ToastNotification(title = 'WEre contacting u about ur extended car payments',
                          message= 'coolio',
                          duration = 5000,
                          bootstyle= 'dark',
                          position= (5,5,'ne'))
ttk.Button(window, text = 'show toast', command= toast.show_toast).pack(pady=10)

#tool tip
button = ttk.Button(window, text='tooltip button', bootstyle = 'warning')
button.pack(pady=10)
ToolTip(button, text= 'Heheheha', bootstyle= 'light')
#Calender

calendar = DateEntry(window)
calendar.pack(pady = 10)

ttk.Button(window, text= 'get callander date', command = lambda: print(calendar.entry.get())).pack()

#progress bar/floodgage
progress_int = tk.IntVar(value=0)
progress = ttk.Floodgauge(window, text='progress', variable = progress_int, bootstyle='darkly', mask= 'mask {}%')
progress.pack(pady = 10, fill= 'x')
ttk.Scale(window, from_= 0, to= 100, variable= progress_int).pack()

#Meter
meter = ttk.Meter(window,
                  amounttotal=100,
                  amountused=0,
                  interactive=True,
                  metertype= 'semi',
                  subtext= 'somme text',
                  bootstyle= 'danger')
meter.pack()

for i in range (100):
    frame = ttk.Frame(scroll_frame)
    ttk.Label(frame, text = f'{i}').pack(fill = 'x', side = 'left')
    ttk.Button(frame, text = f'{i}').pack(fill = 'x', side = 'left')
    frame.pack(fill= 'x', expand= True)
#label = ttk.Label(window, text = 'Label')
#label.pack(pady = 10)
#
#button1 = ttk.Button(window, text = 'Red', bootstyle = 'danger-outline')
#button1.pack(pady = 10)
#
#button2 = ttk.Button(window, text = 'Warning', bootstyle = 'warning')
#button2.pack(pady = 10)
#
#button3 = ttk.Button(window, text = 'Green', bootstyle = 'success')
#button3.pack(pady = 10)

# run
window.mainloop()