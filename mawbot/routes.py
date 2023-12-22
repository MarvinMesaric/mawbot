from flask import redirect, url_for, render_template, flash
from mawbot.forms import LoginForm, RegistrationForm
from mawbot import app

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", form=form, title='Login')

@app.route("/registration")
def registration():
    form = RegistrationForm()
    return render_template("register.html", form = form, title='Registrieren')
    
 