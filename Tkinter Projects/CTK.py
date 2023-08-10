import customtkinter as ctk

window = ctk.CTk()
window.title('ctk app')
window.geometry('600x400')
tk
label = ctk.CTkLabel(window, text = 'a ctk label')
label.pack()

window.mainloop()