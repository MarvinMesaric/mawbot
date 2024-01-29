import os
import secrets
from PIL import Image
from flask import url_for
from flask_mail import Message
from mawbot import app, mail

def save_picture(formPicture):
    randomHex = secrets.token_hex(8)
    _, fExt = os.path.splitext(formPicture.filename)
    pictureFn = randomHex + fExt
    picturePath = os.path.join(app.root_path, 'static/profilePictures', pictureFn)
    
    outputSize = (125, 125)
    i = Image.open(formPicture)
    i.thumbnail(outputSize)
    i.save(picturePath)
    return pictureFn

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Passwort Zurücksetzen', sender='mawbotnoreply@gmail.com', recipients=[user.email])
    msg.body = f'''Hallo {user.username},
Um ihr passwort zurück zu setzen, folgen sie dem folgenden Link:
{ url_for('users.reset_token', token=token, _external=True) }
Wenn diese Anfrage nicht von Ihnen kommt dann ignorieren Sie diese E-Mail und keine änderungen werden vor genommen.
'''
    mail.send(msg)