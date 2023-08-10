import customtkinter as ctk
import time

class sidepanel(ctk.CTkFrame):
    def __init__(self,parent, start_c, end_c):
        super().__init__(parent)

        self.start_c = start_c + 0.02
        self.end_c = end_c
        self.width = abs(start_c - end_c)

        self.pos = self.start_c
        self.in_start_pos = True

        self.place(relx = self.start_c, rely = 0.05, relwidth = self.width, relheight = 0.9)
    def animate(self):
        if self.in_start_pos:
            self.animate_forward()
        else:
            self.animate_backward()

    def animate_forward(self):
        if self.pos > self.end_c:
            self.pos -= 0.002
            self.place(relx = self.pos, rely = 0.05, relwidth = self.width, relheight = 0.9)
            self.after(2, self.animate_forward)
        else:
            self.in_start_pos = False
    def animate_backward(self):
        if self.pos < self.start_c:
            self.pos += 0.002
            self.place(relx=self.pos, rely=0.05, relwidth=self.width, relheight=0.9)
            self.after(2, self.animate_backward)
        else:
            self.in_start_pos = True

def move_btn():
    global button_x
    button_x += 0.001
    button.place(relx=button_x, rely=0.5, anchor='center')

    if button_x < 0.9:
        window.after(10, move_btn   )

def inf_print():
    global button_x
    print("infinite")
    button_x += 0.5
    if button_x > 10:
        window.after(1, inf_print)

window = ctk.CTk()
window.geometry('600x400')
button_x = 0.5
animpanel = sidepanel(window,0, -0.3)
ctk.CTkLabel(animpanel, text = 'label').pack(fill= 'both', expand = True, pady = 10)
ctk.CTkLabel(animpanel, text = 'label').pack(fill= 'both', expand = True, pady = 10)
ctk.CTkButton(animpanel, text = 'label', corner_radius= 5).pack(fill= 'both', expand = True, pady = 10)

button = ctk.CTkButton(window, text = 'animation', command = animpanel.animate)
button.place(relx=button_x, rely= 0.5,anchor = 'center')

window.mainloop()