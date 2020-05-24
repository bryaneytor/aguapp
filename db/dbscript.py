import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute("""CREATE TABLE pedidos
( 
    idpedido INTEGER PRIMARY KEY,
    cantidad INTEGER,
    ubicacion VARCHAR(255),
    cliente VARCHAR(50)
)
""")

c.execute("""CREATE TABLE planta 
(
    idplanta INTEGER PRIMARY KEY, 
    nombre VARCHAR(50), 
    RNC VARCHAR(9), 
    ubicacion VARCHAR(255), 
    dueno VARCHAR(50)
)
""")

c.execute("""CREATE TABLE roles
(
    idrole INTEGER PRIMARY KEY,
    
)
""")


conn.commit()
conn.close()
