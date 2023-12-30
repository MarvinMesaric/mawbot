from datetime import datetime
from mawbot import db



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    profilePicture = db.Column(db.String(20), nullable=False, default='mawbot.png')
    dateOfCreation = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.profilePicture}')"

class Temperature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float, unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Humidity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    humidity = db.Column(db.Float, unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class SoilMoisture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    soilMoisture = db.Column(db.Float, unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Rain(db.Model): # Mit Emanuel Abklären was alles hier übertragen wird.
    id = db.Column(db.Integer, primary_key=True)
    rain = db.Column(db.Boolean, unique=True, nullable=False) 
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Battery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer, unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    progress = db.Column(db.Integer, unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Session(db.Model):
    id = db.Column(db.Integer, primary=True)
    lastMawDate = db.Column(db.DateTime, nullable=False)
    nextMawDate = db.Column(db.datetime, nullable=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
class Location(db.Model):
    id = db.Column(db.Integer, primary=True)
    PosX = db.Column(db.Float, nullable=False)
    PosY = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
# class Activity(db.Model):
    # id = db.Column(db.Integer, primary=True)
    # driving = db.Column(db.Boolean, nullable=False)
    # date = db.Column(db.DateTime, defautl=datetime.utcnow)