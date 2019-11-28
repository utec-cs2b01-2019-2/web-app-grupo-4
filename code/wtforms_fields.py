from flask import g
from flask_wtf import FlaskForm
from passlib.handlers.pbkdf2 import pbkdf2_sha256
from wtforms import StringField,PasswordField,IntegerField,DateField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
import models




class RegisterForm(FlaskForm):
    
    name = StringField('Nombre', validators=[InputRequired(message="Nombre requerido"), Length(min=4, max=25, message="El usuario debe tener entre 4 y 25 caracteres")])
    username = StringField('Usuario', validators=[InputRequired(message="Usuario requerido"), Length(min=4, max=25, message="El usuario debe tener entre 4 y 25 caracteres")])
    email = StringField('Email', validators=[InputRequired(message="Email requerido"), Length(min=4, max=100,message="Ingrese su correo electronico")])
    password = PasswordField('Contrasena', validators=[InputRequired(message="Contrasena requerida"), Length(min=4, max=25, message="La contrasena debe tener entre 4 y 25 caracteres")])
    confirm = PasswordField('Confirmar contrasena', validators=[InputRequired(message="Coonfirmar contrasena"), EqualTo('password', message="Las contrasenas deben ser iguales")])

def invalid_credentials(form, field):
    

    username = form.username.data
    password = field.data

    user= models.User.query.filter_by(username=username).first()
    if user is None:
        raise ValidationError("Usuario o contrasena incorrectos")

    elif password != user.password:
        raise ValidationError("Usuario o contrasena incorrectos")

class ValidarPedido(FlaskForm):
    """ Registration form"""
    nombre_cliente = StringField('Nombre del local', validators=[InputRequired(message="Nombre requerido"), Length(min=2, max=100, message="")])
    cantidad = IntegerField('Cantidad de bolsas', validators=[InputRequired(message="Ingrese la cantidad de bolsas")])
    tipo = StringField('Tipo de bolsa 3kg o 5kg', validators=[InputRequired(message="Ingrese el tipo de bolsa")])
    fecha_entrega = DateField('Fecha de entrega', validators=[InputRequired(message="Escoga una fecha de entrega")])

class LoginForm(FlaskForm):
    """ Login form """

    username = StringField('username', validators=[InputRequired(message="Usuario requerido")])
    password = PasswordField('password', validators=[InputRequired(message="Contrasena requerida"), invalid_credentials])

