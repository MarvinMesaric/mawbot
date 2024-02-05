from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FormField
from wtforms.validators import Email, DataRequired, Length, EqualTo, ValidationError
from mawbot.database import User 

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    passwordCheck = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    uuid = StringField('UU-ID', validators=[DataRequired()])
    submit =  SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Dieser Nutzername wird bereits genutzt.')
        
    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Diese E-Mail wird bereits genutzt.')
    
    def validate_uuid(self, uuid):
        if uuid.data != current_user.uuid:
            uuid = User.query.filter_by(uuid=uuid.data).first()
            if uuid:
                raise ValidationError('Diese UU-ID ist bereits vergeben.')     
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])   
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Eingeloggt bleiben') 
    submit =  SubmitField('Login')

class UpdateCurrentUserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Profilbild Aktualisieren', validators=[FileAllowed(['jpg', 'png'])])
    submit =  SubmitField('Aktualisieren')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Dieser Nutzername wird bereits genutzt.')
        
    def validate_email(self, email):
        if email.data != current_user.email:
            email = User.query.filter_by(email=email.data).first()
            if email:
                raise ValidationError('Diese E-Mail wird bereits genutzt.')
            
       
            

class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit =  SubmitField('Abschicken')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError('Es existiert kein Account mit dieser E-Mail. Bitte Registrieren sie sich erst.')
        

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    passwordCheck = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit =  SubmitField('Passwort ändern')
