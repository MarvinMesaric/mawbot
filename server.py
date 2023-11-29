from flask import Flask, redirect, url_for, render_template
from wtforms import FormField, SubmitField,

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    



if __name__ == "__main__":
    app.run()