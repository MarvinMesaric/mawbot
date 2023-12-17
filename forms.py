from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Email, DataRequired, Length, EqualTo


class RegistrationField(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    passswordCheck = PasswordField('Confirm Passsword', validators=[DataRequired(), EqualTo('password')])
    submit =  SubmitField('Registrieren')
    
    
    
class LoginField(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])   
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Eingeloggt bleiben')
    submit =  SubmitField('Login')
        
