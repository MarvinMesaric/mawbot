from flask import Flask, redirect, url_for, render_template, flash
from wtforms import FormField, SubmitField
from flask_sqlalchemy import SQLAlchemy 
from forms import LoginField, RegistrationField

app = Flask(__name__)

app.config['SECRET_KEY'] = '58b9f874c94eac1eefdaba2cdc757134'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    form = LoginField()
    return render_template("login.html", form=form)

@app.route("/registration")
def registration():
    form = RegistrationField()
    return render_template("register.html", title='Registrieren', form = form)
    


 
if __name__ == "__main__":
    app.run(debug = True)