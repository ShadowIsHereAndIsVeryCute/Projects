import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('buttons')
window.geometry('600x400')

#Default button
def buttonformula():
    print("abasicbutton")
    print(radiovar.get())


button = ttk.Button(window, text = 'A simple button', command= buttonformula)
button.pack()

#checkbutton
checkvar = tk.IntVar()
check = ttk.Checkbutton(window,
                        text='checkbutton',
                        command= lambda: print(checkvar.get()),
                        variable= checkvar,
                        onvalue= 1,
                        offvalue= 0)
#Radio button
radiovar = tk.StringVar()
radio1 = ttk.Radiobutton(window,
                         text= 'radio 1',
                         value = 1,
                         variable= radiovar,
                         command= lambda: print(radiovar.get()))
radio1.pack()
radio2 = ttk.Radiobutton(window, text= 'radio 2', value = 2, variable= radiovar)
radio2.pack()
check.pack()

#excersise
echeckvar = tk.BooleanVar()
eradiovar = tk.IntVar()
eradio1 = ttk.Radiobutton(window,
                          text = 'radio 1',
                          value = 1,
                          variable= eradiovar,
                          command = lambda: print(echeckvar.get()))
eradio1.pack()
eradio2 = ttk.Radiobutton(window,
                          text = 'radio1',
                          value = 2,
                          variable= eradiovar,
                          command = lambda: print(echeckvar.get()))
eradio2.pack()
echeck = ttk.Checkbutton (window,
                          text = 'checkboxe',
                          variable= echeckvar,
                          onvalue=1,
                          offvalue=0,
                          command = lambda: print(eradiovar.get()))
echeck.pack()


window.mainloop()