import sqlite3

connection = sqlite3.connect("users-sqlite.db")

cursor = connection.cursor()

cursor.execute(
    """CREATE TABLE IF NOT EXISTS Users
(user_id INTEGER PRIMARY KEY, AUTO, INCREMENT, first_name TEXT, last_name TEXT, email_address TEXT)"""
)


usersToInsert = [
    ("Tina", "Mccoy", "tmccoy@gmail.com"),
    ("Joan", "Ruiz", "jruiz@gmail.com"),
    ("Sara", "Cox", "scox@gmail.com"),
    ("Jessica", "Alvarez", "jalvarez@gmail.com"),
    ("Amanda", "Butler", "abutler@gmail.com"),
]

# cursor.executemany(
#     '''INSERT INTO Users(first_name, last_name, email_address) VALUES (?,?,?)''', usersToInsert)

# cursor.execute("SELECT email_address FROM Users")
# print(cursor.fetchall())

cursor.execute(
    """UPDATE Users
               SET first_name = "A Manda" 
               WHERE user_id=10"""
)

cursor.execute("SELECT * FROM Users")
print(cursor.fetchall())

connection.commit()
connection.close
