import sqlite3

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

cursor.execute("CREATE TABLE user(first_name, last_name)")
cursor.execute("INSERT INTO user VALUES('marcin', 'developer')")

connection.commit()

result = cursor.execute("SELECT * FROM user")
rows = result.fetchall()

print(rows)