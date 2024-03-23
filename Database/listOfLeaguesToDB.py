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

leagueIDS = ["16169"]


for leagueID in leagueIDS:
    # Get info for teams for this league
    url = "https://api.opendota.com/api/leagues/{}/teams".format(leagueID)
    league = requests.get(url).json()

    for team in league:
        team['league_id'] = int(leagueID)
        insert_into_table(mycursor, "league_team_info", team)   

    # Get info about matches for this league
    url2 = "https://api.opendota.com/api/leagues/{}/matches".format(leagueID)

    league = requests.get(url2).json()

    for match in league:
        matchID = match['match_id']
        url = "https://api.opendota.com/api/matches/{}".format(matchID)
        matchData = requests.get(url).json()
        del matchData["pre_game_duration"]
        del matchData["flags"]
        del matchData["radiant_name"]
        del matchData["radiant_logo"]
        del matchData["dire_name"]
        del matchData["dire_logo"]
        del matchData["od_data"]
        del matchData["metadata"]
        try:
            del matchData["stomp"]
        except:
            print('xd')

        insert_into_table(mycursor, "match_data", matchData)
        print(' Inserted into DB')
        print(matchID)
    

db.commit()