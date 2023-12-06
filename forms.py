from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationField(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20, )])
    email = StringField('Email', validators=[DataRequired, Email])
    password = PasswordField('Password', validators=[DataRequired])
    passswordCheck = PasswordField('Confirm Passsword', validators=[DataRequired, EqualTo('password')])
    submit =  SubmitField('Sign Up')
    
    
    
class RegistrationField(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20, )])   
    password = PasswordField('Password', validators=[DataRequired])
    submit =  SubmitField('Sign Up')
        