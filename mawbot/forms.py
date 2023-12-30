from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms import FormField, SubmitField
from wtforms.validators import Email, DataRequired, Length, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    passwordCheck = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit =  SubmitField('Sign Up')
    
    
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])   
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Eingeloggt bleiben')
    submit =  SubmitField('Login')