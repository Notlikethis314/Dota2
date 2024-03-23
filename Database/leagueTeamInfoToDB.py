import requests
import json
import mysql.connector
from functions import *

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "dota2"
    )

mycursor = db.cursor()

league_id = "15438"

url = "https://api.opendota.com/api/leagues/{}/teams".format(league_id)
league = requests.get(url).json()


for team in league:
    team['league_id'] = int(league_id)
    insert_into_table(mycursor, "league_team_info", team)
    db.commit()

