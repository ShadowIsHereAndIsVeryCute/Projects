import tkinter as tk
from tkinter import ttk
import customtkinter as ctk

class app(ctk.CTk):
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0],size[1])

        self.menu = Menu(self)
        self.main = Main(self)

        self.mainloop()
class Menu(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(x = 0, y = 0, relwidth = 0.3, relheight=1)
        self.create_widgets()
    def create_widgets(self):


        menu_button1 = ctk.CTkButton(self, text='Button1')
        menu_button2 = ctk.CTkButton(self, text='Button2')
        menu_button3 = ctk.CTkButton(self, text='Button3')

        menu_slider = ctk.CTkSlider(self, orientation='vertical')
        menu_slider1 = ctk.CTkSlider(self, orientation='vertical')

        toggle_frame = ctk.CTkFrame(self)
        menu_toggle1 = ctk.CTkCheckBox(toggle_frame, text='check 1')
        menu_toggle2 = ctk.CTkCheckBox(toggle_frame, text='check 2')
        entry = ctk.CTkEntry(self)
        self.columnconfigure((0, 1, 2), weight=1, uniform='a')
        self.rowconfigure((0, 1, 2, 3, 4), weight=1, uniform='a')
        menu_button1.grid(row=0, column=0, sticky='nesw', columnspan=2)
        menu_button2.grid(row=0, column=2, sticky='nesw')
        menu_button3.grid(row=1, column=0, sticky='nesw', columnspan=3)
        menu_slider.grid(row=2, column=0, sticky='nesw', rowspan=2, pady=20)
        menu_slider1.grid(row=2, column=2, sticky='nesw', rowspan=2, pady=20)
        toggle_frame.grid(row=4, column=0, columnspan=3, sticky='nesw')

class Main(ctk.CTkFrame):
    def  __init__(self, parent):
        super().__init__(parent)
        self.place(relx=0.3, y=0, relwidth=0.7, relheight=1)
        Entry(self, 'yeah','yess','red')
        Entry(self, 'woohoo', 'woopie', 'orange')
class Entry(ctk.CTkFrame):
    def __init__(self, parent, label_text, button_text, label_bg):
        super().__init__(parent)
        label = ctk.CTkLabel(self, text = label_text, bg_color= label_bg)
        button = ctk.CTkButton(self, text = button_text)
        label.pack(expand= True, fill= 'both')
        button.pack(expand= True, fill= 'both', pady = 10)
        self.pack(side = 'left', expand= True, fill = 'both', padx= 20, pady=20)
app('class based app', (600,600))
