import sqlite3
from Hub import open_account_page
import customtkinter
from CreateAccountPage import test

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

username = "a"
password = "a"

root = customtkinter.CTk()
root.geometry("500x500")
import sqlite3
filename = "carryover.txt"




def authenticate_user(username, password):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()


    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    stored_password = cursor.fetchone()

    if stored_password is not None:
        stored_password = stored_password[0]


        if password == stored_password:
            print("Authentication successful")
            try:
                with open(filename, 'x'):
                    pass
                print("Empty file created successfully")
            except FileExistsError:
                print("File already exists")
            with open(filename, 'w') as file:
                file.write(username)
            open_account_page()
        else:
            print("Authentication failed")
    else:
        print("User not found")

    conn.close()


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Shadow Banking")
label.pack(pady=12, padx=10)

uentry = customtkinter.CTkEntry(master=frame, placeholder_text="Login ID string")
uentry.pack(pady=12, padx=10)

pentry = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
pentry.pack(pady=12, padx=10)

lbutton = customtkinter.CTkButton(master=frame, fg_color="#00AA00", text="Login", command=lambda: authenticate_user(uentry.get(), pentry.get()))
lbutton.pack(pady=12, padx=10)

Nbutton = customtkinter.CTkButton(master=frame, fg_color="#00AA00", width=100, height=20, text="Create a account", command=lambda: test())
Nbutton.pack(pady=3, padx=10, )



written_uentry = uentry.get()
written_pentry = pentry.get()
username = written_uentry


def create_table():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Create the users table if it doesn't exist
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, id TEXT)")

    conn.close()


def print_all_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Retrieve all data from the database
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()

    # Print the retrieved data
    for row in data:
        print(row)

    conn.close()


create_table()

print_all_data()
root.mainloop()
