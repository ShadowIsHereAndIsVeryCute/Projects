import sqlite3
import random
import customtkinter
import string

def test():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    sub1 = customtkinter.CTk()
    sub1.geometry("500x500")

    frame = customtkinter.CTkFrame(master=sub1)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    label = customtkinter.CTkLabel(master=frame, text="Account Creation")
    label.pack(pady=12, padx=10)
    cuser = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
    cuser.pack(pady=12, padx=10)
    puser = customtkinter.CTkEntry(master=frame, placeholder_text="Password")
    puser.pack(pady=12, padx=10)

    def grn():
        digits = string.digits
        random_number = ''.join(random.choice(digits) for _ in range(16))
        return random_number

    def create_database():
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Create the users table if it doesn't exist
        cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, money REAL)")

        conn.commit()
        conn.close()

    def insert_user():
        written_cuser = cuser.get()
        written_puser = puser.get()
        random_numb = grn()

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()


        cursor.execute("SELECT username FROM users WHERE username = ?", (written_cuser,))
        existing_username = cursor.fetchone()

        if existing_username is not None:
            messagecube2 = customtkinter.CTkLabel(master=frame, text="Account name in use.")
            messagecube2.pack(pady=12, padx=10)
            conn.close()
            return


        cursor.execute("INSERT INTO users (id, username, password, money) VALUES (?, ?, ?, 0.0)",
                       (random_numb, written_cuser, written_puser))
        conn.commit()

        print("User inserted successfully")

        messagecube = customtkinter.CTkLabel(master=frame, text="Account Successfully Created.")
        messagecube.pack(pady=12, padx=10)

        conn.close()

    create_database()

    lbutton = customtkinter.CTkButton(master=frame, text="Create new account", command=insert_user)
    lbutton.pack(pady=12, padx=10)

    sub1.mainloop()

