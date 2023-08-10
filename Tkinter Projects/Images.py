import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry('600x400')
window.title('images')

#import images
image_og = Image.open('PrepareToSuffer.png')
image_tk = ImageTk.PhotoImage(image_og)

label = ttk.Label(window, text = 'shit', image = image_tk)
label.pack()



window.mainloop()
