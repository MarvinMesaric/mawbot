from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from mawbot import db
from mawbot.database import *

sensordata = Blueprint('sensordata', __name__)

@sensordata.route("/controls")
def controls():
    return render_template("controls.html")

@sensordata.route("/sensordatas")
@login_required
def sensordatas():
    tempValue = Temperature.query.order_by(Temperature.id.desc()).filter_by(uuid=current_user.uuid).first()
    humValue = Humidity.query.order_by(Humidity.id.desc()).filter_by(uuid=current_user.uuid).first()
    soilMValue = SoilMoisture.query.order_by(SoilMoisture.id.desc()).filter_by(uuid=current_user.uuid).first()
    rainValue = Rain.query.order_by(Rain.id.desc()).filter_by(uuid=current_user.uuid).first()
    batValue = Battery.query.order_by(Battery.id.desc()).filter_by(uuid=current_user.uuid).first()
    progValue = Progress.query.order_by(Progress.id.desc()).filter_by(uuid=current_user.uuid).first()
    return render_template("sensordatas.html", temperatureValue=tempValue.temperature, humidityValue=humValue.humidity, soilMoistureValue=soilMValue.soilMoisture, rainValue=rainValue.rain,  batteryValue=batValue.status, progressValue=progValue.progress)

# @sensordata.route("/recievedata")
# def recievedata():
     