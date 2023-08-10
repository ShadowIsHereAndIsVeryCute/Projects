import sqlite3
def print_all_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Retrieve all rows from the users table
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    # Print the contents of the table
    for row in rows:
        print(row)
def update_money(username, id, new_money):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Check if the username exists in the database
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    if row is None:
        print("Username not found")
        conn.close()
        return

    # Check if the id exists in the database
    cursor.execute("SELECT * FROM users WHERE id = ?", (id,))
    row = cursor.fetchone()
    if row is None:
        print("ID not found")
        conn.close()
        return

    # Update the money column for the specified username and id
    cursor.execute("UPDATE users SET money = money + ? WHERE username = ? AND id = ?", (new_money, username, id))
    conn.commit()

    print("Money updated successfully")

    conn.close()

# Usage example
new_money = float(input("Magic Money Input: "))
username = input("name: ")
id = input("id: ")
print_all_data()
update_money(username, id, new_money)
print_all_data()
