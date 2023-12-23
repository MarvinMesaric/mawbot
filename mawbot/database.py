from mawbot import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    profilePicture = db.Column(db.String(20), nullable=False, default='mawbot.png')
    dateOfCreation = db.Column(db.DateTime, nullable=False, default=datetime.utcnow )

class Temperature(db.Model):
    id = db.Column(db.Integer, primary=True)
    temperature = db.column(db.Float, unique=True, nullable=False)



