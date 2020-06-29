import sqlite3
import json
from hashlib import md5, sha224
from .models import db, Pedidos, Plantas, Users, Colmados, Anuncios

class DBManager():

    def insertAd(user,title,info,price):
        anuncios = Anuncios(
            idusuario = user,
            titulo = title,
            info = info,
            precio = price
        )
        db.session.add(anuncios)
        db.session.commit()
        return

    def insertPlanta(user,nombre,rnc,ubicacion,dueno):
        planta = Plantas(
            idusuario=user,
            nombre=nombre, 
            rnc=rnc, 
            ubicacion=ubicacion, 
            owner=dueno
        )
        db.session.add(planta)
        db.session.commit()
        return
    
    def insertColmado(user,nombre,rnc,ubicacion,dueno):
        colm = Colmados(
            idusuario=user,
            nombre=nombre, 
            rnc=rnc, 
            ubicacion=ubicacion, 
            owner=dueno
        )
        db.session.add(colm)
        db.session.commit()
        return

    def insertPedido(client, qty, location,marca):
        pedido = Pedidos(
            idusuario=client, 
            cantidad=qty, 
            ubicacion=location,
            water_brand=marca
        )
        db.session.add(pedido)
        db.session.commit()
        return

    def insertUser(user, passwrd, status,admn,colm,clnt):
        user = Users(
            username=user, 
            password=passwrd,
            status=status,
            admin=admn,
            colmado=colm,
            cliente=clnt
        )
        db.session.add(user)
        db.session.commit()
        return 

###############################################################
#                       GET methods
###############################################################
    def verpedido(_id):
        with sqlite3.connect("db/database2.db") as conn:
            c = conn.cursor()
            c.execute(
                "SELECT * FROM pedidos WHERE idusuario = (?) ", 
                (str(_id),)
            )
            resultado = c.fetchall()
            print (resultado)
            return json.dumps(resultado)
        return

    def verPedidosClientes():
        with sqlite3.connect("db/database2.db") as conn:
            c = conn.cursor()
            c.execute(
                "SELECT * FROM pedidos where cliente = '1' ",
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

    def verplantas():
      with sqlite3.connect("db/database2.db") as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM plantas")
            resultado = c.fetchall()
            return json.dumps(resultado)

    def vercolmados():
        with sqlite3.connect("db/database2.db") as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM colmados")
            resultado = c.fetchall()
            return json.dumps(resultado)

    def verAds():
        with sqlite3.connect("db/database2.db") as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM anuncios")
            resultado = c.fetchall()
            return json.dumps(resultado)

####################################################################
#               Global USERS endpoints functions
####################################################################

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
        else:
            return True
       