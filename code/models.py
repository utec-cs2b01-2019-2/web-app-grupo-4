from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_login import UserMixin
from wtforms import *
import wtforms_fields

db = SQLAlchemy()



class User(db.Model):
    """ User model """
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(25),unique=True, nullable=False)
    email = db.Column(db.String(25), unique=True, nullable=False)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    register_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

class Pedido(db.Model):
    __tablename__ = "pedidos"
    id = db.Column(db.Integer, primary_key=True)
    nombre_cliente = db.Column(db.String(36), unique=False, nullable=True)
    cantidad = db.Column(db.Integer, unique=False, nullable=False)
    tipo = db.Column(db.Integer, nullable=False)
    fecha_entrega = db.Column(db.DateTime(25), unique=False, nullable=False)
    cancelada = db.Column(db.String(3), nullable=True)
    fecha_pedido = db.Column(db.DateTime, default=datetime.datetime.utcnow)


