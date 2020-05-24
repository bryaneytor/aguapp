import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/bryan/bryan/aguapp/db/database2.db'
db = SQLAlchemy(app)

class pedidos(db.Model):
    __tablename__ = 'pedidos'
    idpedido = db.Column(db.Integer, primary_key=True)
    cliente = db.Column(db.String(50))
    cantidad = db.Column(db.Integer, nullable=False)
    ubicacion = db.Column(db.String(255), nullable=False)

class plantas(db.Model):
    __tablename__ = 'plantas'
    idplanta = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    rnc = db.Column(db.String(9),nullable=False)
    ubicacion = db.Column(db.String(255), nullable=False)
    owner = db.Column(db.String(50))

# Define the User data-model
class usuario(db.Model):
    __tablename__ = 'usuarios'
    idusuario = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(255),nullable=False)
    status = db.Column(db.String(1), nullable=False)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    rol = db.Column(db.String(50), nullable=False, default="Cliente")

# Define the Role data-model
#class Role(db.Model):
# Roles : Admin, Planta, Colmado, Cliente
#    __tablename__ = 'roles'
#    idrol = db.Column(db.Integer(), primary_key=True)
#    rol = db.Column(db.String(50), unique=True)

# Define the UserRoles association table
#class UserRoles(db.Model):
#    __tablename__ = 'user_roles'
#    _id = db.Column(db.Integer(), primary_key=True)
#    user_id = db.Column(db.Integer(), db.ForeignKey('usuario.idusuario', ondelete='CASCADE'))
#    role_id = db.Column(db.Integer(), db.ForeignKey('roles.idrol', ondelete='CASCADE'))

db.create_all()
db.session.commit()
db.session.close()