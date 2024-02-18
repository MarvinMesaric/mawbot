from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from mawbot import db, login_manager, app
from flask_login import UserMixin
import pytz

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    profilePicture = db.Column(db.String(20), nullable=False, default='default.jpg')
    uuid = db.Column(db.Integer, nullable=False)
    dateOfCreation = db.Column(db.String(19), nullable=False, default=datetime.now(pytz.timezone('Europe/Berlin')).strftime("%Y-%m-%d %H:%M:%S"))

    def get_reset_token(self, expiresSec=1800):
        s = Serializer(app.config['SECRET_KEY'], expiresSec)
        return s.dumps({'user_id': self.id}).decode('utf-8')
    
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.profilePicture}')"

class Temperature(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Integer, nullable=False)
    temperature = db.Column(db.Float, unique=True, nullable=False)
    date = db.Column(db.String(19), nullable=False, default=datetime.now(pytz.timezone('Europe/Berlin')).strftime("%Y-%m-%d %H:%M:%S"))

class Humidity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Integer, nullable=False)
    humidity = db.Column(db.Float, unique=True, nullable=False)
    date = db.Column(db.String(19), nullable=False, default=datetime.now(pytz.timezone('Europe/Berlin')).strftime("%Y-%m-%d %H:%M:%S"))

class SoilMoisture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Integer, nullable=False)
    soilMoisture = db.Column(db.Float, unique=True, nullable=False)
    date = db.Column(db.String(19), nullable=False, default=datetime.now(pytz.timezone('Europe/Berlin')).strftime("%Y-%m-%d %H:%M:%S"))

class Rain(db.Model): # Mit Emanuel Abklären was alles hier übertragen wird.
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Integer, nullable=False)
    rain = db.Column(db.Boolean, unique=True, nullable=False) 
    date = db.Column(db.String(19), nullable=False, default=datetime.now(pytz.timezone('Europe/Berlin')).strftime("%Y-%m-%d %H:%M:%S"))

class Battery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, unique=True, nullable=False)
    date = db.Column(db.String(19), nullable=False, default=datetime.now(pytz.timezone('Europe/Berlin')).strftime("%Y-%m-%d %H:%M:%S"))

class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Integer, nullable=False)
    progress = db.Column(db.Integer, unique=True, nullable=False)
    date = db.Column(db.String(19), nullable=False, default=datetime.now(pytz.timezone('Europe/Berlin')).strftime("%Y-%m-%d %H:%M:%S"))

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Integer, nullable=False)
    lastMawDate = db.Column(db.String(19), nullable=False)
    nextMawDate = db.Column(db.String(19), nullable=True)
    date = db.Column(db.String(19), nullable=False, default=datetime.now(pytz.timezone('Europe/Berlin')).strftime("%Y-%m-%d %H:%M:%S"))
    
class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Integer, nullable=False)
    PosX = db.Column(db.Float, nullable=False)
    PosY = db.Column(db.Float, nullable=False)
    date = db.Column(db.String(19), nullable=False, default=datetime.now(pytz.timezone('Europe/Berlin')).strftime("%Y-%m-%d %H:%M:%S"))
    
# class Activity(db.Model):
    # id = db.Column(db.Integer, primary=True)
    # uuid = db.Column(db.Integer, nullable=False)
    # driving = db.Column(db.Boolean, nullable=False)
    # date = db.Column(db.DateTime, defautl=datetime.utcnow)