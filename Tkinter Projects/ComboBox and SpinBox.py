import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('ComboBox and SpinBox')
window.geometry('600x400')

#combobox
items = ('IceCream', 'Pizza', 'Lunch')
food_string = tk.StringVar(value = items[0])
combo = ttk.Combobox(window, textvariable= food_string)
combo.configure(values = items)
combo.pack()

combo.bind('<<ComboboxSelected>>', lambda event: combo_label.configure(text = f'Selected value: {food_string.get()}'))
combo_label = ttk.Label(window, text= "Selected value: " + items[0])
combo_label.pack()

#spinbox
list = ('a', 'b', 'c', 'd', 'e')
spin = ttk.Spinbox(window, from_ = 0, to= 20, increment=2, command= lambda: print("a button was pressed"))
spin.bind('<<Increment>>', lambda event: print("up"))
spin.bind('<<Decrement>>', lambda event: print("down"))
#spin.configure(values = "list")
spin.pack()
e_string = tk.StringVar(value= list[0])
espin = ttk.Spinbox(window, values= list, textvariable=e_string)
espin.bind('<<Decrement>>', lambda event: print(e_string.get()))
espin_value = espin.get()
espin.pack()

window.mainloop()