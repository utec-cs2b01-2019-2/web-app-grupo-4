from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,IntegerField
from wtforms.validators import InputRequired, Length, EqualTo, ValidationError
from models import *

class RegisterForm(FlaskForm):
    """ Registration form"""
    name = StringField('Nombre', validators=[InputRequired(message="Username required"), Length(min=4, max=25, message="El usuario debe tener entre 4 y 25 caracteres")])
    username = StringField('Usuario', validators=[InputRequired(message="Username required"), Length(min=4, max=25, message="El usuario debe tener entre 4 y 25 caracteres")])
    email = StringField('Email', validators=[InputRequired(message="Username required"), Length(min=4, max=100,message="Ingrese su correo electronico")])
    password = PasswordField('Contrasena', validators=[InputRequired(message="Password required"), Length(min=4, max=25, message="La contrasena debe tener entre 4 y 25 caracteres")])
    confirm = PasswordField('Confirmar contrasena', validators=[InputRequired(message="Password required"), EqualTo('password', message="Las contrasenas deben ser iguales")])

