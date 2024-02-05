from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from mawbot import db, login_manager, app
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    profilePicture = db.Column(db.String(20), nullable=False, default='default.jpg')
    dateOfCreation = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

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
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Humidity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Integer, nullable=False)
    humidity = db.Column(db.Float, unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class SoilMoisture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Integer, nullable=False)
    soilMoisture = db.Column(db.Float, unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Rain(db.Model): # Mit Emanuel Abklären was alles hier übertragen wird.
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Integer, nullable=False)
    rain = db.Column(db.Boolean, unique=True, nullable=False) 
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Battery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Progress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Integer, nullable=False)
    progress = db.Column(db.Integer, unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Integer, nullable=False)
    lastMawDate = db.Column(db.DateTime, nullable=False)
    nextMawDate = db.Column(db.DateTime, nullable=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
class Location(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Integer, nullable=False)
    PosX = db.Column(db.Float, nullable=False)
    PosY = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
# class Activity(db.Model):
    # id = db.Column(db.Integer, primary=True)
    # uuid = db.Column(db.Integer, nullable=False)
    # driving = db.Column(db.Boolean, nullable=False)
    # date = db.Column(db.DateTime, defautl=datetime.utcnow)