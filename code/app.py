from flask import Flask,render_template,flash,redirect,url_for,session,logging,request
from flask_login import login_user
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from models import *
from functools import wraps
from wtforms.validators import DataRequired
import os
import wtforms_fields

app= Flask(__name__)
app.secret_key=os.environ.get('SECRET')

#database
app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URL')

db=SQLAlchemy(app)



@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/home')
def home():
    return render_template('home.html')




# User Register
@app.route('/register', methods=['GET', 'POST','UPDATE'])
def register():
    form = wtforms_fields.RegisterForm()
    if form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = form.password.data
        user1 = User(username=username, password=password,name=name,email=email)
        db.session.add(user1)
        db.session.commit()
        return render_template('login.html',form=login_form)

    return render_template("register.html", form=form)



# User login


@app.route("/login", methods=['GET', 'POST'])
def login():
    login_form = wtforms_fields.LoginForm()

    if login_form.validate_on_submit():
        user_object = User.query.filter_by(username=login_form.username.data).all()
        flash('Bienvenido ')
        return redirect(url_for('home'))
    return render_template("login.html", form=login_form)




@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out')
    return redirect(url_for('home'))

@app.route('/pedido', methods=['GET', 'POST','UPDATE'])
def pedido():
    form = wtforms_fields.ValidarPedido()
    if form.validate_on_submit():
        nombre_cliente = form.nombre_cliente.data
        cantidad=form.cantidad.data
        tipo=form.tipo.data
        fecha_entrega=form.fecha_entrega.data
        pedido1 = Pedido(nombre_cliente=nombre_cliente,cantidad=cantidad,tipo=tipo,fecha_entrega=fecha_entrega)
        db.session.add(pedido1)
        db.session.commit()
        return render_template('pedido_registrado.html')

    return render_template("pedido.html", form=form)

@app.route('/pedido_registrado')
def pedido_registrado():
    return render_template('pedido_registrado.html')

if __name__=="__main__":
    app.run()
