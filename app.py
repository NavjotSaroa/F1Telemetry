"""Will act as backend to the html pages"""
import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
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


    # Figure out a way to get all tracks of a season, then all sessions of a track, and then all drivers of a session.
    years = [i for i in range(2018,2022)]

    print(request.args.get("year"))

    # Yes this is not pretty code, but it takes a while to run so this way the user doesn't have to wait for long for the next bit to show up.
    if request.form.get("year") != None:
        if int(request.args.get("year")) == 2018:
            tracks=['Australian Grand Prix', 'Bahrain Grand Prix', 'Chinese Grand Prix', 'Azerbaijan Grand Prix', 
            'Spanish Grand Prix', 'Monaco Grand Prix', 'Canadian Grand Prix', 'French Grand Prix', 
            'Austrian Grand Prix', 'British Grand Prix', 'German Grand Prix', 'Hungarian Grand Prix', 
            'Belgian Grand Prix', 'Italian Grand Prix', 'Singapore Grand Prix', 'Russian Grand Prix', 
            'Japanese Grand Prix', 'United States Grand Prix', 'Mexican Grand Prix', 'Brazilian Grand Prix', 
            'Abu Dhabi Grand Prix']

        elif int(request.args.get("year")) == 2019:
            tracks=['Australian Grand Prix', 'Bahrain Grand Prix', 'Chinese Grand Prix', 'Azerbaijan Grand Prix', 
            'Spanish Grand Prix', 'Monaco Grand Prix', 'Canadian Grand Prix', 'French Grand Prix', 'Austrian Grand Prix', 
            'British Grand Prix', 'German Grand Prix', 'Hungarian Grand Prix', 'Belgian Grand Prix', 'Italian Grand Prix', 
            'Singapore Grand Prix', 'Russian Grand Prix', 'Japanese Grand Prix', 'Mexican Grand Prix', 'United States Grand Prix', 
            'Brazilian Grand Prix', 'Abu Dhabi Grand Prix']

        elif int(request.args.get("year")) == 2020:
            tracks=['Austrian Grand Prix', 'Styrian Grand Prix', 'Hungarian Grand Prix', 'British Grand Prix', 
            '70th Anniversary Grand Prix', 'Spanish Grand Prix', 'Belgian Grand Prix', 'Italian Grand Prix', 
            'Tuscan Grand Prix', 'Russian Grand Prix', 'Eifel Grand Prix', 'Portuguese Grand Prix', 'Emilia Romagna Grand Prix', 
            'Turkish Grand Prix', 'Bahrain Grand Prix', 'Sakhir Grand Prix', 'Abu Dhabi Grand Prix']
        else:
            tracks=['Bahrain Grand Prix', 'Emilia Romagna Grand Prix', 'Portuguese Grand Prix', 
            'Spanish Grand Prix', 'Monaco Grand Prix', 'Azerbaijan Grand Prix', 'French Grand Prix', 
            'Styrian Grand Prix', 'Austrian Grand Prix', 'British Grand Prix', 'Hungarian Grand Prix', 
            'Belgian Grand Prix', 'Dutch Grand Prix', 'Italian Grand Prix', 'Russian Grand Prix', 
            'Turkish Grand Prix', 'United States Grand Prix', 'Mexico City Grand Prix', 'São Paulo Grand Prix', 
            'Qatar Grand Prix', 'Saudi Arabian Grand Prix', 'Abu Dhabi Grand Prix']
        return render_template("index.html", years=years, tracks=tracks)

    return render_template("index.html", years=years)

@app.route("/about")
def about():
    return render_template("about.html")

# if __name__ == "__main__":
#     from waitress import serve
#     serve(app, host="0.0.0.0", port=8080)