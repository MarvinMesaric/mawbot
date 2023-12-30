from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FormField
from wtforms.validators import Email, DataRequired, Length, EqualTo, ValidationError
from mawbot.database import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    passwordCheck = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit =  SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Dieser Nutzername wird bereits genutzt.')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Diese E-Mail wird bereits genutzt.')
    
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(min=2, max=20), Email()])   
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Eingeloggt bleiben')
    submit =  SubmitField('Login')