import sqlite3

conn = sqlite3.connect('../employee.db')

c = conn.cursor()

c.execute("""
INSERT INTO employees VALUES ('Markus', 'Lewandowski', '102000')
""")

# Commit to Database via the connection. Note that we are not using the cursor here!
conn.commit()

conn.close()