import flask

app = flask.Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='template')
app.config["DEBUG"] = True
from flask import render_template, redirect, url_for

@app.route("/")
def home():
    return render_template("home.html")

