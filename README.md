# Accelerator Reading Sensory Equipment: Throttle Data Logger

#### Description:
This project's aim is to collect telemetry data on my sim racing setup using Arduino sensors, and then view it on an HTML web page.
  
I started by creating a SQLite3 database (telemetry.db) using a python code (dbmaker.py). I entered a dictionary with the years 2018 to 2021 as keys, and a list of all the tracks F1 raced on in those seasons for values. It would be better code if I used the more dynamic method of generating a list using the [fastf1](https://theoehrly.github.io/Fast-F1/index.html) library that I used for most of the rest of the project, however this code is meant to only be used once and takes a couple hours to finish running as it is. As you will see later, the library has to go through a lot of data just to come up with the information needed in this database. This is why it seemed better to just hard code the list of races into the code.
dbmaker.py eventually created the following database:
 ```
  CREATE TABLE f1 (
    id INTEGER NOT NULL 
    year NUMERIC NOT NULL 
    track TEXT NOT NULL 
    session TEXT NOT NULL 
    drivers TEXT NOT NULL 
    PRIMARY KEY(id)
);
  ```
This database is used by the HTML page, using flask (in app.py) and jinja, I create 2 pages, index.html and about.html. The main page (index.html) opens up with a drop down menu asking the user to choose a F1 season between 2018 and 2021, submitting the choice leads to the page refreshing with a new dropdown menu asking for a racetrack, which leads to asking for a session (which would be the free practice sessions, qualifying, sprint race, and the race, depending on whether the sessions were held or not), and finally leads to askign for a driver that took part in that session. As the user enters these inputs, another SQLite3 table is filled up:
  ```
  CREATE TABLE query (
    id INTEGER NOT NULL 
    year NUMERIC 
    track TEXT 
    session TEXT 
    driver TEXT 
    PRIMARY KEY(id)
);
  ```
Upon the submission of the name of the driver, the Arduino sketch (sketch.ino) is run. This is the part where the actual data logging happens, the user runs a lap on any racing game (ideally a game that runs f1 cars on f1 tracks, like the F1 Game series, since the whole point of the webpage is to compare the users' throttle input to that of a real F1 driver) using the Arduino setup (wokwi-project.txt). 
  
The system consists of an ultrasonic sensor, which is to be placed in front of the throttle pedal to measure the distance to said pedal (I would have used another ultrasonic sensor for the brakes, but I did not have one and the only way to get one was to go to a store that is a 40 minute drive away), and a potentiometer, to make sure that the sensor logs data only when the user wants to (ie: during the lap). sketch.ino reads the distance and prints it on the Serial Monitor, for app.py to read, convert to a percentage value indicating how far has the throttle pedal been pressed, and then plot it to a graph against time.
  
 ![ArduinoSchematic](https://user-images.githubusercontent.com/77352263/154856101-34c40ab9-28a6-4972-bb79-a69229c3b627.png)
  
Once this is done, app.py uses fastf1 to find the throttle data of the fastest lap that the chosen driver put in on the chosen session of the chosen track in the chosen season. Which is why it took so long to make the database, the library had to go through all kinds of data relevant to a race weekend (throttle, brake, DRS, gear shifts of every driver in every single weekend, along with the weather conditions for every minute of these weekends, and any other data that I have forgot to mention).
  
Finally, after all that is done, the telemetry data of the user and the F1 driver show up on index.html
  
And about.html is just to explain the website to anyone who would access it but is not reading this README.
