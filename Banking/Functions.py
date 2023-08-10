import customtkinter
import string
import random


def insert_user():
    written_cuser = cuser.get()
    written_puser = puser.get()
    random_numb = grn()

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Insert the username, password, and id into the users table
    cursor.execute("INSERT INTO users (username, password, id) VALUES (?, ?, ?)",
                   (written_cuser, written_puser, random_numb))
    conn.commit()

    print("User inserted successfully")

    messagecube = customtkinter.CTkLabel(master=frame, text="Account Successfully Created.")
    messagecube.pack(pady=12, padx=10)

    conn.close()