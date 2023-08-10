import tkinter as tk
from tkinter import ttk
from random import choice

window = tk.Tk()
window.title('ComboBox and SpinBox')
window.geometry('600x400')
first_names = ["John", "Jane", "Michael", "Emily", "David", "Sarah", "Daniel", "Olivia", "Matthew", "Emma", "Andrew", "Sophia", "Christopher", "Isabella", "Joseph", "Ava", "William", "Mia", "Alexander", "Charlotte"]

last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Robinson"]

table = ttk.Treeview(window, columns= ('First', 'Last', 'Collums'), show= 'headings')
table.heading('First', text= "First Name")
table.heading('Last', text= "Last Name")
table.heading('Collums', text= "Email")
table.pack(fill = 'both', expand= True)
for i in range(100):
    first = choice(first_names)
    last = choice(last_names)
    email = f'{first}{last}@gmail.com'
    data = (first, last, email)
    table.insert(parent = '', index= 0, values=data)
def item_select(_):
    print(table.selection())
    for i in table.selection():
        print(table.item(i)['values'])



table.bind('<<TreeviewSelect>>', item_select)


window.mainloop()