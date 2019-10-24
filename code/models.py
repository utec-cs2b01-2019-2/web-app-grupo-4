from flask_sqlalchemy import SQLAlchemy
import datetime
from flask_login import UserMixin

db = SQLAlchemy()


class User(UserMixin, db.Model):
    """ User model """

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(25),unique=True, nullable=False)
    email = db.Column(db.String(25), unique=True, nullable=False)
    username = db.Column(db.String(25), unique=True, nullable=False)
    hashed_pswd = db.Column(db.String(), nullable=False)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
