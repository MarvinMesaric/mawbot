from flask import render_template, url_for, flash, redirect
from mawbot import app, db, bcrypt
from mawbot.forms import RegistrationForm, LoginForm
from mawbot.database import User 

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
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Ihr Account wurde erstellt, Sie können sich jetzt einloggen')
        return render_template(url_for('login'))
    return render_template("register.html", form = form, title='Registrieren')
    
 