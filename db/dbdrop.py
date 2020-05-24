import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute("DROP TABLE planta")
c.execute("DROP TABLE pedidos")