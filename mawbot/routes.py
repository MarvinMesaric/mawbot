import secrets
import os
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from mawbot import app, db, bcrypt, mail
from mawbot.forms import RegistrationForm, LoginForm, UpdateCurrentUserForm, ResetPasswordForm, RequestResetForm
from mawbot.database import User 
from flask_login import current_user, login_user, logout_user, login_required
from flask_mail import Message

#pip install flask-mail

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/controls")
def controls():
    return render_template("controls.html")

@app.route("/sensordata")
def sensordata():
    return render_template("sensordata.html")

def SavePicture(formPicture):
    randomHex = secrets.token_hex(8)
    _, fExt = os.path.splitext(formPicture.filename)
    pictureFn = randomHex + fExt
    picturePath = os.path.join(app.root_path, 'static/profilePictures', pictureFn)
    
    outputSize = (125, 125)
    i = Image.open(formPicture)
    i.thumbnail(outputSize)
    i.save(picturePath)
    return pictureFn

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateCurrentUserForm()
    if form.validate_on_submit():
        if form.picture.data:
            pictureFile = SavePicture(form.picture.data)
            current_user.profilePicture = pictureFile
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Ihr Account wurde Aktualisiert.', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username 
        form.email.data = current_user.email
    profilePicture = url_for('static', filename='profilePictures/' + current_user.profilePicture)
    return render_template("account.html", form=form, title="Account", profilePicture=profilePicture)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Ihr Nutzername / Passwort stimmen nicht überein. Bitte versuchen sie es erneut.', 'danger')
    return render_template("login.html", form=form, title='Login')

@app.route("/registration", methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Ihr Account wurde erstellt, Sie können sich jetzt einloggen')
        return redirect(url_for('login'))
    return render_template("registration.html", form = form, title='Registrieren')
    
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Passwort Zurücksetzen', sender='mawbotnoreply@gmail.com', recipients=[user.email])
    msg.body = f'''Hallo {user.username},
Um ihr passwort zurück zu setzen, folgen sie dem folgenden Link:
{ url_for('reset_token', token=token, _external=True) }
Wenn diese Anfrage nicht von Ihnen kommt dann ignorieren Sie diese E-Mail und keine änderungen werden vor genommen.
'''
    mail.send(msg)

@app.route("/reset_password", methods=['GET', 'POST'])
def reset_password():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('Sie haben eine E-Mail zum zurücksetzen Ihres Passwortes erhalten', 'info')
        return redirect(url_for('login'))
    return render_template('resetRequest.html', title='Passwort Zurücksetzen', form=form)

@app.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('Dieser Token ist nicht mehr gültig.', 'warning')
        return redirect(url_for('resetRequest'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Ihr Passwort wurde geändert! Sie können sich nun einloggen.')
        return redirect(url_for('login'))
    return render_template('resetToken.html', title='Passwort Zurücksetzen', form=form)

