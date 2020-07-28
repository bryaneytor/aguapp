# -*- coding: utf-8 -*-
import json
import sqlite3
from flask_cors import CORS
from flask import request
from db.models import db, app
from db.dbmanager import DBManager

CORS(app)

#POST Endpoints

@app.route('/agregar/planta', methods=['POST'])
def agregar_planta():
   if request.method == 'POST':
        data = request.get_json()
        print (data)
        DBManager.insertPlanta(
           data['idusuario'],
           data['nombre'],
           data['RNC'],
           data['ubicacion'],
           data['dueno']
        )
        return "true"

@app.route('/agregar/colmado', methods=['POST'])
def agregar_colmado():
   if request.method == 'POST':
       data = request.get_json()
       print (data)
       DBManager.insertColmado(
           data['idusuario'],
           data['nombre'],
           data['RNC'],
           data['ubicacion'],
           data['dueno']
        )
       return "true"

@app.route('/publicar/pedido', methods=['POST'])
def publicarPedido():
    if request.method == 'POST':
        data = request.get_json()
        print (data)
        DBManager.insertPedido(
            data['idcliente'],
            data['cantidad'],
            data['ubicacion'],
            data['marca']
        )
        return "true"

@app.route('/publicar/anuncio', methods=['POST'])
def ad():
    if request.method == 'POST':
        data = request.get_json()
        print (data)
        DBManager.insertAd(
            data['idusuario'],
            data['titulo'],
            data['info'],
            data['precio']
        )

    return "true"

@app.route('/publicar/pedido/anuncio')
def choseAd():

    return


#GET Endpoints

@app.route('/anuncios')
def verAds():
    return DBManager.verAds()

@app.route('/Q/<int:iduser>', methods=['GET'])
def verpedido(iduser):
    return DBManager.verpedido(iduser)

@app.route('/Q', methods=['GET'])
def pedidos():
    return DBManager.verpedidos()

@app.route('/Qclientes', methods=['GET'])
def pedidosClientes():
    return DBManager.verPedidosClientes()

@app.route('/plantas', methods=['GET'])
def plantas():
    return DBManager.verplantas()

@app.route('/colmados')
def colmados():
    return DBManager.vercolmados()

#USER Endpoints

@app.route('/users', methods=['GET'])
def veruser():
    return DBManager.veruser()

@app.route('/signup', methods=['POST'])
def signup():
    if request.method == "POST":
        data = request.get_json()
        print (data)

        #Validate if username exists before creating it
        with sqlite3.connect("db/database2.db") as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM usuarios where username = (?)", (data['username'],))
            resultado = c.fetchall()
            print (resultado)

            if not resultado:
                DBManager.insertUser(
                    data['username'],
                    data['password'],
                    int(data['status']),
                    int(data['admin']),
                    int(data['colmado']),
                    int(data['cliente'])
                )
                return "true"
            else:
                return "false"

@app.route('/login', methods=['POST'])
def login():
    if request.method == "POST":
        data = request.get_json()
        print(data)
        access = DBManager.login(
            data['username'],
            data['password']
        )

        if access == True:
            with sqlite3.connect("db/database2.db") as conn:
                c = conn.cursor()
                c.execute(
                    "SELECT idusuario,admin,colmado,cliente FROM usuarios where username = (?)",
                    (data['username'],)
                )
                user_data = c.fetchone()

                if user_data[3] == 1:
                    print("user type: cliente", user_data[3])
                    tipo = "cliente"
                elif user_data[2] == 1:
                    print ("user type: colmado", user_data[2])
                    tipo = "colmado"
                elif user_data [1] == 1:
                    print ("user type: admin", user_data[1])
                    tipo = "admin"
                else:
                    tipo = "cliente"

                return json.dumps({
                    "user_id": user_data[0],
                    "user_type": tipo
                })
        else:
            return "0"


if __name__ == "__main__":
      app.run(
        host='0.0.0.0',
        debug=True,
        ssl_context=(
            'certificate/cert.pem',
            'certificate/key.pem'
        )
      )
