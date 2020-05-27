# -*- coding: utf-8 -*-

from flask_cors import CORS
from flask import request
from db.backupold import DBManage
from db.dbmanager import db, app
from db.connect import DBManager
from hashlib import sha224
CORS(app)

@app.route('/agregar/planta', methods=['POST'])
def agregar_planta():
   if request.method == 'POST':
       data = request.get_json()
       print (data)
       DBManage.insertPlanta(
           data['nombre'],
           data['RNC'],
           data['ubicacion'],
           data['dueno']
        )
       return ""

@app.route('/publicar/pedido', methods=['GET','POST'])
def publicarPedido():
    if request.method == 'POST':
        data = request.get_json()
        print (data)
        DBManager.insertPedido(
            data['cliente'],
            data['cantidad'],
            data['ubicacion']
        )
        return ""

@app.route('/publicar/pedido/cliente', methods=['GET','POST'])
def publicarPedidoCliente():
    if request.method == 'POST':
        data = request.get_json()
        print (data)
        DBManager.insertPedidoCliente(
            data['idcliente'],
            data['cantidad'],
            data['ubicacion'],
            data['marca']
        )
        return ""

@app.route('/verpedido/cliente/<int:cliente>', methods=['GET'])
def ClientePedido(cliente):
   return DBManager.verClientePedido(cliente)

@app.route('/verpedido/<int:numeropedido>', methods=['GET'])
def verpedido(numeropedido):
    return DBManager.verpedido(numeropedido)

@app.route('/verpedidos', methods=['GET'])
def pedidos():
    return DBManager.verpedidos()

@app.route('/verpedidosClientes', methods=['GET'])
def pedidosClientes():
    return DBManager.verpedidosclientes()

@app.route('/verplantas', methods=['GET'])
def plantas():
    return DBManager.verplantas()

@app.route('/verusuarios', methods=['GET'])
def veruser():
    return DBManager.veruser()

@app.route('/signup', methods=['POST'])
def signup():
    if request.method == "POST":
        data = request.get_json()
        print (data)
        DBManager.insertUser(
            data['username'], 
            data['password'], 
            data['rol'], 
            int(data['status'])
            )
        return ""

@app.route('/login', methods=['GET'])
def login():
    if request.method == "GET":
        data = request.get_json()
          
if __name__ == "__main__":  
    app.run(
        host='0.0.0.0', 
        debug=True, 
        ssl_context=(
            'cert.pem', 
            'key.pem'
        )
    )
