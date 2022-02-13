"""Will act as backend to the html pages"""
import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from datetime import datetime

from matplotlib import pyplot as plt
import fastf1 as ff1
from fastf1 import plotting
from fastf1 import Cache
import pandas as pd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

db = SQL("sqlite:///telemetry.db")



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


@app.route("/", methods=["GET", "POST"])
def index():
    """Allow user to select  driver"""


    # Figure out a way to get all tracks of a season, then all sessions of a track, and then all drivers of a session.
    if request.method =="POST":
        

        lst = db.execute("SELECT DISTINCT(year) FROM f1;")
        years=[]
        for i in lst:
            years.append(i['year'])

        season = request.form.get("season")
        print(season)
        track = request.form.get("track")
        print(track)
        driver = request.form.get("driver")
        print(driver) 

        return redirect("/")

    #TODO: Create appropriate table in database for storing year, track, and driver and see if that is any easier.
    
    else:
        return render_template("index.html") 

@app.route("/about")
def about():
    return render_template("about.html")

# if __name__ == "__main__":
#     from waitress import serve
#     serve(app, host="0.0.0.0", port=8080)