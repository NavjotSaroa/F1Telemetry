"""This bit is only meant to be used once to create the database.
Ran for a couple hours on my laptop so you better treat the database
carefully or else you will have to run it for that long too!"""


from cs50 import SQL
import fastf1 as ff1
from fastf1 import plotting
from fastf1 import Cache
import pandas as pd

db = SQL("sqlite:///telemetry.db")


# dictionary = {2018:['Australian Grand Prix', 'Bahrain Grand Prix', 'Chinese Grand Prix', 'Azerbaijan Grand Prix', 
#         'Spanish Grand Prix', 'Monaco Grand Prix', 'Canadian Grand Prix', 'French Grand Prix', 
#         'Austrian Grand Prix', 'British Grand Prix', 'German Grand Prix', 'Hungarian Grand Prix', 
#         'Belgian Grand Prix', 'Italian Grand Prix', 'Singapore Grand Prix', 'Russian Grand Prix', 
#         'Japanese Grand Prix', 'United States Grand Prix', 'Mexican Grand Prix', 'Brazilian Grand Prix', 
#         'Abu Dhabi Grand Prix'],
#         2019:['Australian Grand Prix', 'Bahrain Grand Prix', 'Chinese Grand Prix', 'Azerbaijan Grand Prix', 
#         'Spanish Grand Prix', 'Monaco Grand Prix', 'Canadian Grand Prix', 'French Grand Prix', 'Austrian Grand Prix', 
#         'British Grand Prix', 'German Grand Prix', 'Hungarian Grand Prix', 'Belgian Grand Prix', 'Italian Grand Prix', 
#         'Singapore Grand Prix', 'Russian Grand Prix', 'Japanese Grand Prix', 'Mexican Grand Prix', 'United States Grand Prix', 
#         'Brazilian Grand Prix', 'Abu Dhabi Grand Prix'],
#         2020:['Austrian Grand Prix', 'Styrian Grand Prix', 'Hungarian Grand Prix', 'British Grand Prix', 
#         '70th Anniversary Grand Prix', 'Spanish Grand Prix', 'Belgian Grand Prix', 'Italian Grand Prix', 
#         'Tuscan Grand Prix', 'Russian Grand Prix', 'Eifel Grand Prix', 'Portuguese Grand Prix', 'Emilia Romagna Grand Prix', 
#         'Turkish Grand Prix', 'Bahrain Grand Prix', 'Sakhir Grand Prix', 'Abu Dhabi Grand Prix'],
#         2021:['Bahrain Grand Prix', 'Emilia Romagna Grand Prix', 'Portuguese Grand Prix', 
#         'Spanish Grand Prix', 'Monaco Grand Prix', 'Azerbaijan Grand Prix', 'French Grand Prix', 
#         'Styrian Grand Prix', 'Austrian Grand Prix', 'British Grand Prix', 'Hungarian Grand Prix', 
#         'Belgian Grand Prix', 'Dutch Grand Prix', 'Italian Grand Prix', 'Russian Grand Prix', 
#         'Turkish Grand Prix', 'United States Grand Prix', 'Mexico City Grand Prix', 'São Paulo Grand Prix', 
#         'Qatar Grand Prix', 'Saudi Arabian Grand Prix', 'Abu Dhabi Grand Prix']}

# sessions = ['FP1','FP2','FP3','Q','SQ','R']

# infolst=[]

# for i in range(2018,2022):
#     for j in range(len(dictionary[i])):
#         for k in range(len(sessions)):
# #     db.execute("INSERT INTO tester (year,track) VALUES (?,?)", i, "Australia")
#             try:
#                 laps = ff1.get_session(i, dictionary[i][j], sessions[k]).load_laps()
#                 drivers=pd.unique(laps["Driver"])
#                 for driver in drivers:
#                     infolst.append([i, dictionary[i][j], sessions[k], driver]) 
#                     print(infolst[-1])
#                     db.execute("INSERT INTO f1 (year, track, session, drivers) VALUES (?, ?, ?, ?)", infolst[-1][0],infolst[-1][1],infolst[-1][2],infolst[-1][3])
#                     print("About {}% \done".format(len(infolst)/8100))
#             except:
#                 print("This session didn't happen")


print(db.execute("SELECT DISTINCT(year) FROM f1;"))

