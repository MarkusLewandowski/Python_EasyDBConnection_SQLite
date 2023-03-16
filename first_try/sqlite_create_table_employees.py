import sqlite3

conn = sqlite3.connect('../employee.db')

c = conn.cursor()
c.execute("""CREATE TABLE employees (
first text,
last text,
pay real
)""")

# Commit to Database via the connection. Note that we are not using the cursor here!
conn.commit()

conn.close()
