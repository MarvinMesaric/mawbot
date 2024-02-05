from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_user, current_user, logout_user, login_required
from mawbot import db, bcrypt
from mawbot.database import User
from mawbot.users.forms import RegistrationForm, LoginForm, UpdateCurrentUserForm, RequestResetForm, ResetPasswordForm
from mawbot.users.utils import save_picture, send_reset_email

users = Blueprint('users', __name__)

@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Ihr Nutzername / Passwort stimmen nicht überein. Bitte versuchen sie es erneut.', 'danger')
    return render_template("login.html", form=form, title='Login')

@users.route("/registration", methods=['GET', 'POST']) 
def registration():
    form = RegistrationForm()
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password, uuid = form.email.uuid)
        db.session.add(user)
        db.session.commit()
        flash('Ihr Account wurde erstellt, Sie können sich jetzt einloggen')
        return redirect(url_for('users.login'))
    return render_template("registration.html", form = form, title='Registrieren')

@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateCurrentUserForm()
    if form.validate_on_submit():
        if form.picture.data:
            pictureFile = save_picture(form.picture.data)
            current_user.profilePicture = pictureFile
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Ihr Account wurde Aktualisiert.', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username 
        form.email.data = current_user.email
    profilePicture = url_for('static', filename='profilePictures/' + current_user.profilePicture)
    return render_template("account.html", form=form, title="Account", profilePicture=profilePicture)

@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@users.route("/reset_password", methods=['GET', 'POST'])
def reset_password():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('Sie haben eine E-Mail zum zurücksetzen Ihres Passwortes erhalten', 'info')
        return redirect(url_for('users.login'))
    return render_template('resetRequest.html', title='Passwort Zurücksetzen', form=form)

@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('Dieser Token ist nicht mehr gültig.', 'warning')
        return redirect(url_for('users.resetRequest'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Ihr Passwort wurde geändert! Sie können sich nun einloggen.', 'success')
        return redirect(url_for('users.login'))
    return render_template('resetToken.html', title='Passwort Zurücksetzen', form=form)

