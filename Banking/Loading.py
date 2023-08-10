import customtkinter
import time


def create_progressbar():
    sub1 = customtkinter.CTk()
    sub1.geometry("500x350")

    frame = customtkinter.CTkFrame(master=sub1)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    sub1.progressbar_1 = customtkinter.CTkProgressBar(sub1.slider_progressbar_frame)
    sub1.progressbar_1.pack(pady=20, padx=20)

create_progressbar()