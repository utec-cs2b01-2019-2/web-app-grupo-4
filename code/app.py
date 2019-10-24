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
app.secret_key='secreto'

#database
app.config['SQLALCHEMY_DATABASE_URI']='postgres://tkmqionogakzdx:a80c41f6bf582ea300d0d70470ca51e7c5706f5857fa3b6af16c80b67760dadd@ec2-107-20-155-148.compute-1.amazonaws.com:5432/dfa2lqmmmvka0j'

db=SQLAlchemy(app)



@app.route('/')
def index():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')





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
        return render_template('pedido_registrado.html')

    return render_template("register.html", form=form)



# User login


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']

        # Create cursor
        cur = db.cursor()

        # Get user by username
        result = cur.execute("SELECT * FROM users WHERE username = %s", [username])

        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            password = data['password']

            # Compare Passwords
            if sha256_crypt.verify(password_candidate, password):
                # Passed
                session['logged_in'] = True
                session['username'] = username

                flash('You are now logged in', 'success')
                return redirect(url_for('dashboard'))
            else:
                error = 'Invalid login'
                return render_template('login.html', error=error)
            # Close connection
            cur.close()
        else:
            error = 'Username not found'
            return render_template('login.html', error=error)

    return render_template('login.html')

# Check if user logged in

def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap

# Logout

@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))

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
    app.run(debug=True)


