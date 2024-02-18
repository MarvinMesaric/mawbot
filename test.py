from mawbot.database import *
from datetime import datetime
from mawbot import app, db
import pytz

nmd = datetime.now(pytz.timezone('Europe/Berlin')).strftime("%Y-%m-%d %H:%M:%S")


temperature = Temperature(uuid=1, temperature=25)
humidity = Humidity(uuid=1, humidity=100)
soilMoisture = SoilMoisture(uuid=1, soilMoisture=100)
rain = Rain(uuid=1, rain=True)
battery = Battery(uuid=1, status=3)
progress = Progress(uuid=1, progress=2)
session = Session(uuid=1, lastMawDate=nmd, nextMawDate=nmd)
location = Location(uuid=1, PosX=10.0, PosY=10.0)





with app.app_context():
    db.session.add(temperature)
    db.session.add(humidity)
    db.session.add(soilMoisture)
    db.session.add(rain)
    db.session.add(battery)
    db.session.add(progress)
    db.session.add(session)
    db.session.add(location)
    db.session.commit()