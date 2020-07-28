import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://///usr/local/aguapp/db/database2.db'
db = SQLAlchemy(app)


class Plantas(db.Model):
    __tablename__ = 'plantas'
    __table_args__ = (
        db.UniqueConstraint('nombre','rnc'),
        {'extend_existing': True}
    )

    idplanta = db.Column(db.Integer, primary_key=True)
    idusuario = db.Column(
        db.Integer(),
        db.ForeignKey(
            'usuarios.idusuario',
            ondelete='CASCADE'
        )
    )
    nombre = db.Column(db.String(255), nullable=False)
    rnc = db.Column(db.String(9),nullable=False)
    ubicacion = db.Column(db.String(255), nullable=False)
    owner = db.Column(db.String(50))

class Colmados(db.Model):
    __tablename__ = 'colmados'
    __table_args__ = {'extend_existing': True}

    idplanta = db.Column(db.Integer, primary_key=True)
    idusuario = db.Column(
        db.Integer(),
        db.ForeignKey(
            'usuarios.idusuario',
            ondelete='CASCADE'
        )
    )
    nombre = db.Column(db.String(255), nullable=False)
    rnc = db.Column(db.String(9),nullable=False)
    ubicacion = db.Column(db.String(255), nullable=False)
    owner = db.Column(db.String(50))

# Define the User data-model
class Users(db.Model):
    __tablename__ = 'usuarios'
    __table_args__ = (
        db.UniqueConstraint('username'),
        {'extend_existing': True}
    )

    idusuario = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100),nullable=False, unique=True)
    password = db.Column(db.String(255),nullable=False)
    status = db.Column(db.Boolean, nullable=False, default='1')
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    admin = db.Column(db.Boolean,nullable=True, default='0')
    colmado = db.Column(db.Boolean,nullable=True, default='0')
    cliente = db.Column(db.Boolean,nullable=True, default='0')

class Pedidos(db.Model):
    __tablename__ = 'pedidos'
    __table_args__ = {'extend_existing': True}

    idpedido = db.Column(db.Integer, primary_key=True)
    idusuario = db.Column(
        db.Integer(),
        db.ForeignKey(
            'usuarios.idusuario',
            ondelete='CASCADE'
        )
    )
    cantidad = db.Column(db.Integer, nullable=False)
    ubicacion = db.Column(db.String(255), nullable=False)
    water_brand = db.Column(db.String(255), nullable=False)

class Anuncios(db.Model):
    __tablename__ = 'anuncios'
    __table_args__ = {'extend_existing': True}

    idanuncio = db.Column(db.Integer, primary_key=True)
    idusuario = db.Column(
        db.Integer,
        db.ForeignKey(
            'usuarios.idusuario',
            ondelete='CASCADE'
        )
    )
    titulo = db.Column(db.String(255), nullable=False)
    info = db.Column(db.Text, nullable=False)
    precio = db.Column(db.Float, nullable=False)


db.create_all()
db.session.commit()
db.session.close()
