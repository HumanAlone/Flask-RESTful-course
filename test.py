import sqlite3

connection = sqlite3.connect("data.db")

cursor = connection.cursor()

# create_table = "CREATE TABLE users (id int, username text, password text)"
# cursor.execute(create_table)

user = (1, "Sergey", "123")
insert_query = "INSERT INTO users VALUES (?, ?, ?)"


users = [
    (2, "Anna", "345"),
    (3, "Gena", "567")
]
cursor.executemany(insert_query, users)

connection.commit()

connection.close()
