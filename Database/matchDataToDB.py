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



class apiCall():
    def __init__(self):
        self.s = requests.Session()
        # self.s.headers = {'Authorization':'388b64da-d6a6-47d2-a166-c00c938b8a88'}

    def getProMatchInfo(self, id):
        
        return  self.s.get('https://api.opendota.com/api/matches/{}'.format(id)).json()  



# P = apiCall()

matchIDS = open("C:/Users/ondra/backup/Python/Dota2/Database/matchesIds.json")
matchIDS = json.load(matchIDS)

#url = "https://api.opendota.com/api/matches/7239927928"

leagueID = "15438"

url = "https://api.opendota.com/api/leagues/{}/matches".format(leagueID)

print(url)

league = requests.get(url).json()

for match in league:
    insert_into_table(mycursor, "match_data", match)
    db.commit()