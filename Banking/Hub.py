import sqlite3

import customtkinter


def open_account_page():
    def get_id_from_username(username):
        conn = sqlite3.connect('database                                    .db')
        cursor = conn.cursor()

        # Retrieve the ID from the database
        cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()

        # Check if the account exists
        if row is None:
            print("Account not found")
            conn.close()
            return None

        # Extract the ID value from the row
        id = row[0]

        conn.close()
        return id
    def read_username_from_file(filename):
        try:
            with open(filename, 'r') as file:
                username = file.read().strip()
            return username
        except FileNotFoundError:
            print("File not found")
            return None

    def get_account_balance(username):
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()


        cursor.execute("SELECT money FROM users WHERE username = ?", (username, ))
        row = cursor.fetchone()


        if row is None:
            print("Account not found")
            conn.close()
            return None


        balance = row[0]

        conn.close()
        return balance

    def read_file(filename):
        try:
            with open(filename, 'r') as file:
                content = file.read()
            print("File content:")
            print(content)
        except FileNotFoundError:
            print("File not found")


    username = read_username_from_file("carryover.txt")
    balance = get_account_balance(username)
    id = get_id_from_username(username)
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    sub2 = customtkinter.CTk()
    sub2.geometry("450x100")
    frame = customtkinter.CTkFrame(master=sub2)
    frame.pack(pady=20, padx=60, fill="both", expand=True)
    optionmenu_1 = customtkinter.CTkOptionMenu(fg_color="#13020C",button_color="#13020C", button_hover_color="#24131D",master=frame, dropdown_fg_color= "#13020C", values=["Transaction ID", str(id), "Balance", str(balance)])
    optionmenu_1.pack(pady=12, padx=10)
    optionmenu_1.set("Welcome to Shadow's Banking home page " + username)
    
    sub2.mainloop()





