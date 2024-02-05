from flask import render_template, Blueprint

sensordata = Blueprint('sensordata', __name__)

@sensordata.route("/controls")
def controls():
    return render_template("controls.html")

@sensordata.route("/sensordatas")
def sensordatas():
    return render_template("sensordatas.html")

@sensordata.route("/recievedata")
def recievedata():
    