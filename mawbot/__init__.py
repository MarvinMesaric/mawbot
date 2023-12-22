from flask import Flask, redirect, url_for, render_template, flash
from wtforms import FormField, SubmitField
from flask_sqlalchemy import SQLAlchemy 
from mawbot import routes


app = Flask(__name__)

app.config['SECRET_KEY'] = 'test'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)