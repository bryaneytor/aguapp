import sqlite3
import json

class DBManage():

    def insertPlanta(nombre,rnc,ubicacion,dueno):
        with sqlite3.connect("database.db") as conn:
            c = conn.cursor()
            c.execute(
                "INSERT INTO planta(nombre,RNC,ubicacion, dueno) VALUES (?, ?, ?, ?)", 
                (nombre,rnc,ubicacion,dueno)
            )
            conn.commit()
            return
        return
    
    def insertPedido(client, qty, location):
        with sqlite3.connect("database.db") as conn:
            c = conn.cursor()
            c.execute("INSERT INTO pedidos(cliente,cantidad,ubicacion) VALUES (?, ?, ?)", (client, qty, location))
            conn.commit()
            return
        return
    
    def verpedido(idpedido):
        with sqlite3.connect("database.db") as conn:
            c = conn.cursor()
            c.execute("SELECT ubicacion, cliente, cantidad FROM pedidos WHERE idpedido = (?) ", (str(idpedido),))
            resultado = c.fetchone()
            print (resultado)
            return json.dumps(resultado)
        return
    
    def verpedidos():
        with sqlite3.connect("database.db") as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM pedidos")
            resultado = c.fetchall()
            return json.dumps(resultado)
        return

    def verplantas():
        with sqlite3.connect("database.db") as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM planta")
            resultado = c.fetchall()
            return json.dumps(resultado)