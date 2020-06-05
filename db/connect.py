import sqlite3
import json
from hashlib import md5
from .dbmanager import db, pedidos, plantas, usuario, pedidoCliente

class DBManager():

    def insertPlanta(nombre,rnc,ubicacion,dueno):
        planta = plantas(
            nombre=nombre, 
            rnc=rnc, 
            ubicacion=ubicacion, 
            owner=dueno
        )
        db.session.add(planta)
        db.session.commit()
        return
    
    def insertPedido(client, qty, location):
        pedido = pedidos(
            cliente=client, 
            cantidad=qty, 
            ubicacion=location
        )
        db.session.add(pedido)
        db.session.commit()
        return

    def insertPedidoCliente(idclient, qty, location,botellon):
        pedido = pedidoCliente(
            id_cliente=idclient, 
            cantidad=qty, 
            ubicacion=location,
            water_brand=botellon
        )
        db.session.add(pedido)
        db.session.commit()
        return

    def insertUser(user, passwrd, rol, status):
        #passw = passwrd.encode("utf-8")
        #m = md5()
        #m.update(passw)
        #contra = m.digest()
        #print(contra)
        user = usuario(
            username=user, 
            password=passwrd, 
            rol=rol, 
            status=status
        )
        db.session.add(user)
        db.session.commit()
        return ""
    
    def verpedido(_id):
        with sqlite3.connect("db/database2.db") as conn:
            c = conn.cursor()
            c.execute(
                "SELECT ubicacion, cliente, cantidad FROM pedidos WHERE idpedido = (?) ", 
                (str(_id),)
            )
            resultado = c.fetchone()
            print (resultado)
            return json.dumps(resultado)
        return
    def verClientePedido(cliente):
        with sqlite3.connect("db/database2.db") as conn:
            c = conn.cursor()
            c.execute(
                "SELECT * FROM pedidoCliente where id_cliente = (?) ", (cliente,)
            )
            resultado = c.fetchall()
            return json.dumps(resultado)
        return
    
    def verpedidos():
        with sqlite3.connect("db/database2.db") as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM pedidos")
            resultado = c.fetchall()
            return json.dumps(resultado)
        return
    def verpedidosclientes():
        with sqlite3.connect("db/database2.db") as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM pedidoCliente")
            resultado = c.fetchall()
            return json.dumps(resultado)
        return

    def verplantas():
      with sqlite3.connect("db/database2.db") as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM planta")
            resultado = c.fetchall()
            return json.dumps(resultado)

    def veruser():
        with sqlite3.connect("db/database2.db") as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM usuarios")
            resultado = c.fetchall()
            return json.dumps(resultado)

    def login(user,contra):
        with sqlite3.connect("db/database2.db") as conn:
            c = conn.cursor()
            c.execute("SELECT username,password FROM usuarios where username = (?) and password = (?)", (user,contra))
            resultado = c.fetchall()
            print (json.dumps(resultado))
        
        if not resultado:
            return False
            #json.dumps({
            #     "err_code": 400,
            #     "err_mesg": "Wrong username or password",
            #     "data": None
            # })

        else:
            return True
            # json.dumps({
            #     "err_code": 200,
            #     "err_mesg": "Login Succesfull",
            #     "data": json.dumps(resultado)
            # })

    #c.execute("SELECT * FROM pedidos")
    #rows = c.fetchall()

    #with open("json_tables/planta.json", "w") as write_file:
    #    json.dump(rows, write_file)

    #for row in rows: 
    #    json.dumps(row)
    #    print(row)

    #conn.close()
