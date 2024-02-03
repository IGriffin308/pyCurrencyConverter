from flask import Flask, flash, request, render_template, session, redirect
from flask_debugtoolbar import DebugToolbarExtension
from converter import Convert
import requests 

app = Flask(__name__)
app.config["SECRET_KEY"] = "invest19"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

@app.route("/")
def show_homepage():
    """Start application"""
    return render_template("form.html")

@app.route("/result", methods=['POST', 'GET'])
def show_result():
    """Display the result"""
    return Convert.convert()
