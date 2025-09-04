import sqlite3

# Database connection
conn = sqlite3.connect('internship.db')
cursor = conn.cursor()

# Table create
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
)
''')

# Insert data
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Aryan", 17))
conn.commit()

# Read data
print("Reading data from database:")
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

# Update data
cursor.execute("UPDATE users SET age=? WHERE name=?", (19, "Aryan"))
conn.commit()
print("\nData after update:")
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

# Delete data
cursor.execute("DELETE FROM users WHERE name=?", ("Aryan",))
conn.commit()
print("\nData after delete:")
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

conn.close()