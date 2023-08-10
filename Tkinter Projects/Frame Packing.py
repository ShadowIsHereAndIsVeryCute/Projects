import tkinter as tk
from tkinter import ttk
from random import choice


window = tk.Tk()
window.title('Advanced Pack')
window.geometry('600x400')
window.iconbitmap('PrepareToSuffer.ico')
#Top Frame
top_frame = ttk.Frame(window)
label1 = ttk.Label(top_frame, text = 'First label', background= 'red')
label2 = ttk.Label(top_frame, text = 'Label 2', background= 'blue')
#Middle
label3 = ttk.Label(window, text = 'Another label', background= 'green')
# Bottom frame
buttom_frame = ttk.Frame(window)
label4 = ttk.Label(window, text = 'Last label', background= 'orange')
button = ttk.Button(window, text = 'a button')
button2 = ttk.Button(window, text = 'Another button')
#Bottom right frame
bottom_right_frame = ttk.Frame(buttom_frame)
button3 = ttk.Button(bottom_right_frame, text = 'Button3')
button4 = ttk.Button(bottom_right_frame, text = 'Button4')
button5 = ttk.Button(bottom_right_frame, text = 'a Button5')




# top layout
label1.pack(side = 'left',fill= 'both', expand= True)
label2.pack(side = 'left',fill= 'both', expand= True)
top_frame.pack(fill = 'both', expand= True)
#Middle Layout
label3.pack(expand= True)
#Bottom Layout
button.pack(side = 'left', expand=True, fill= 'both')
label4.pack(side = 'left', expand=True, fill= 'both')
button2.pack(side = 'left', expand=True, fill= 'both')
buttom_frame.pack(expand= True, padx= 20, pady = 20)
button3.pack(expand=True, fill='both')
button4.pack(expand=True, fill='both')
button5.pack(expand=True, fill='both')
bottom_right_frame.pack(fill='both', side= 'left')
window.mainloop()