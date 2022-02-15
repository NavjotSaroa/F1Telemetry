"""Will act as backend to the html pages"""
import os
from teleplot import userplot

from cs50 import SQL
from flask import Flask, render_template, request, session
from flask_session import Session
# from tempfile import mkdtemp
# from datetime import datetime

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


# Everything above this is pretty much all taken from CS50's Flask problem set, apart from lines 10 to 14

@app.route("/")
def index():
    """Allow user to select  driver"""

    year = request.args.get("year")
    track = request.args.get("track")
    event = request.args.get("event")
    driver = request.args.get("driver") # Point of these is just to initialise the variables really

    if (not year) and (not track) and (not event) and (not driver): # Selecting year here
        db.execute("INSERT INTO query(year, track, session, driver) VALUES('','','','');")
        # id = db.execute("SELECT id FROM ")
        
        """I realised that calling session that here was not a smart idea, just that I realised that way too late and the rest of the
        code just works with this, any mention of session in this function refers to an F1 session rather than the flask_session import 
        though. 'session' comes from the html, the equivalent in this python code is 'event'."""

        lst = db.execute("SELECT DISTINCT(year) FROM f1;")
        years=[]
        for i in lst:
            years.append(i['year']) # Generates a list of years between 2018 and 2021, the years where fastf1 data is apparently good.

        return render_template("index.html", years=years) 

    elif year: # Selecting track here
        db.execute("UPDATE query SET year = ? WHERE id = (SELECT MAX(id) FROM query);", year)
        lst = db.execute("SELECT DISTINCT(track) FROM f1 WHERE year = ?;", year)
        tracks = []
        for i in lst:
            tracks.append(i['track']) # Generates a list of tracks that were raced on in the selected year

        return render_template("index.html", year=year, tracks=tracks)

    elif track: # Selecting event here
        print(track)
        db.execute("UPDATE query SET track = ? WHERE id = (SELECT MAX(id) FROM query);", track)
        year = db.execute("SELECT year FROM query WHERE id = (SELECT MAX(id) FROM query);")
        year = year[-1]["year"]

        lst = db.execute("SELECT DISTINCT(session) FROM f1 WHERE year=? AND track=?;", year, track)
        events = []
        for i in lst:
            events.append(i['session']) # Generates a list of sessions/events
            # Should almost always be ["FP1", "FP2", "FP3", "Q", "R"] or ["FP1", "FP2", "Q", "SQ", "R"] unless a session was abandoned.

        return render_template("index.html", year=year, track=track, events=events)

    elif event: # Selecting driver here
        db.execute("UPDATE query SET session = ? WHERE id = (SELECT MAX(id) FROM query);", event)
        year = db.execute("SELECT year FROM query WHERE id = (SELECT MAX(id) FROM query);")
        year = year[-1]["year"]

        track = db.execute("SELECT track FROM query WHERE id = (SELECT MAX(id) FROM query);")
        track = track[-1]["track"]

        lst = db.execute("SELECT DISTINCT(drivers) FROM f1 WHERE year=? AND track=? AND session=?;", year, track, event)
        drivers = []
        for i in lst:
            drivers.append(i['drivers']) # Generates a list of all drivers that participated in the session.

        return render_template("index.html", year=year, track=track, event=event, drivers=drivers)

    elif driver: # Just shows the choices at the end
        db.execute("UPDATE query SET driver = ? WHERE id = (SELECT MAX(id) FROM query);", driver)
        year = db.execute("SELECT year FROM query WHERE id = (SELECT MAX(id) FROM query);")
        year = year[-1]["year"]

        track = db.execute("SELECT track FROM query WHERE id = (SELECT MAX(id) FROM query);")
        track = track[-1]["track"]

        event = db.execute("SELECT session FROM query WHERE id = (SELECT MAX(id) FROM query);")
        event = event[-1]["session"]

        status1 = False#userplot() # Will get your race data

        plotting.setup_mpl() # Everything below here gets f1 driver data.

        weekend = ff1.get_session(year, track, event)

        laps = weekend.load_laps(with_telemetry=True)
        fastestlap = laps.pick_driver(driver).pick_fastest()
        data = fastestlap.get_car_data()
        t = data['Time']
        throttle = data['Throttle']

        # The rest is just plotting
        fig, ax = plt.subplots()
        ax.plot(t, throttle)
        ax.set_xlabel('Time')
        ax.set_ylabel('Throttle (%)')
        plt.savefig("static\\racertelemetry.jpg")

        return render_template("index.html", year=year, track=track, event=event, driver=driver, status1=status1)



@app.route("/about")
def about():
    return render_template("about.html")