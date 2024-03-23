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

url = "https://api.opendota.com/api/leagues"
leagues = requests.get(url).json()


for league in leagues:
    insert_into_table(mycursor, "league_info", league)
    
db.commit()