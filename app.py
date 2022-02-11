"""Will act as backend to the html pages"""
import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

# from matplotlib import pyplot as plt
# import fastf1 as ff1
# from fastf1 import plotting
# from fastf1 import Cache
# import pandas as pd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True



# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    """Allow user to select  driver"""

    #Figure out a way to get all tracks of a season, then all sessions of a track, and then all drivers of a session.
    # tracks=[]

    # for i in range(1,23):
    #     tracks.append(ff1.get_session(2021, i, "R").weekend.name)



    # track = request.form.get("track")
    # session = request.form.get("session")
    # driver = request.form.get("driver")

    
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

# if __name__ == "__main__":
#     from waitress import serve
#     serve(app, host="0.0.0.0", port=8080)