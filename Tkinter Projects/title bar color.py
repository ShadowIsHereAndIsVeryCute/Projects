import customtkinter as ctk
from ctypes import windll, byref, sizeof, c_int

app = ctk.CTk()
app.geometry('300x200')

HWND = windll.user32.GetParent(app.winfo_id())
tb = 0x000000FF
windll.dwmapi.DwmSetWindowAttribute(HWND,
                                    35,
                                    byref(c_int(tb)), sizeof(c_int))


app.mainloop()