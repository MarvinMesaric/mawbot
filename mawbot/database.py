from mawbot import db
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy


class User(db.Model):
    id = db.Column(db.Integer, primary=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    profilePicture = db.Column(db.String(20), nullable=False, default='mawbot.png')
    dateOfCreation = db.Column(db.DateTime, nullable=False, default=datetime.utcnow )

class Temperature(db.Model):
    id = db.Column(db.Integer, primary=True)
    temperature = db.Column(db.Float, unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Humidity(db.Model):
    id = db.Column(db.Integer, primary=True)
    humidity = db.Column(db.Float, unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class SoilMoisture(db.Model):
    id = db.Column(db.Integer, primary=True)
    soilMoisture = db.Column(db.Float, unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Rain(db.Model): # Mit Emanuel Abklären was alles hier übertragen wird.
    id = db.Column(db.Integer, primary=True)
    rain = db.Column(db.Boolean, unique=True, nullable=False) 
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Battery(db.Model):
    id = db.Column(db.Integer, primary=True)
    status = db.Column(db.Integer, unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Progress(db.Model):
    id = db.Column(db.Integer, primary=True)
    progress = db.Column(db.Integer, unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    