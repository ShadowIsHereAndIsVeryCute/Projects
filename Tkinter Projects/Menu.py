import tkinter as tk
from tkinter import ttk
from random import choice


window = tk.Tk()
window.title('ComboBox and SpinBox')
window.geometry('600x400')
# main menu
menu = tk.Menu(window)

#sub menu
file_menu = tk.Menu(menu, tearoff= False)
file_menu.add_command(label= 'New', command = lambda: print("new file"))
file_menu.add_command(label= 'Open', command = lambda: print("new file"))
#sub sub menu
help_menu = tk.Menu(menu, tearoff= False)
menu.add_cascade(label= 'Help', menu= help_menu)
menu.add_cascade(label= 'Files', menu = file_menu)
e_menu = tk.Menu(menu, tearoff= False)
menu.add_cascade(label= 'E Menu', menu = e_menu)
e_menu2 = tk.Menu(e_menu, tearoff= False)
e_menu.add_cascade(label= 'cool', menu = e_menu2)
e_menu3 = tk.Menu(e_menu2, tearoff= False)
e_menu2.add_cascade(label= 'yes', menu= e_menu3)
help_menu.add_command(label= 'Help', command = lambda: print("Help"))
help_check_string = tk.StringVar()
help_menu.add_checkbutton(label = 'check', onvalue= 'on', offvalue= 'off', variable=help_check_string)
# menu button
mb = ttk.Menubutton(window, text= 'Menu button')
mb.pack()
bsm = tk.Menu(mb, tearoff= False)
bsm.add_command(label = 'entry 1', command= lambda: print("value 1"))
mb.configure(menu = bsm)
window.configure(menu = menu)


window.mainloop()