from flask import Flask,render_template, request, session, Response, redirect
from database import connector
from model import entities
import datetime
import json
import time


db = connector.Manager()
engine = db.createEngine()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login' , methods =['POST']) 
def login():
    username = request.form['user'] 
    password = request.form['password']

    db_session = db.getSession(engine)

    user = db_session.query(entities.User).filter(
        entities.User.username == username
    ).filter(
    entities.User.password == password
    ).first()

    if user != None:
        session['usuario'] = username
        return render_template('pedido.html')
    else:
        return "Sorry "+username+" no esta en la base de datos"