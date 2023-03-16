import sqlite3

conn = sqlite3.connect('../employee.db')

c = conn.cursor()
c.execute(" SELECT * FROM employees WHERE last='Lewandowski' ")

print(c.rowcount)
print(c.fetchall())
print(c.fetchone())
print(c.fetchmany(3))

# result = c.execute(" SELECT * FROM employees WHERE last='Lewandowski' ")

# {} placeholder for .format sting are bad practice! SQL API can use ? placeholders for exactly that and mititgat
# SQL injections



# print(result)

# Commit to Database via the connection. Note that we are not using the cursor here!
conn.commit()

conn.close()
