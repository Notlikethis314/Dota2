import mysql.connector
from functions import *
import os
from dotenv import load_dotenv
import requests

# API
load_dotenv()

API_KEY = os.getenv("API_KEY")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
USER = os.getenv("USER_DB")

# DB connection
mydb = mysql.connector.connect(
  host=HOST,
  user=USER,
  password=PASSWORD,
  database='dota'
)

cursor = mydb.cursor()

matchStructure = {
 'match_id': 'BIGINT',
 'barracks_status_dire': 'INT',
 'barracks_status_radiant': 'INT',
 'chat': 'JSON',
 'cluster': 'INT',
 'cosmetics': 'JSON',
 'dire_score': 'INT',
 'dire_team_id':'INT',
 'dire_team_name':'VARCHAR(200)',
 'draft_timings': 'JSON',
 'duration': 'INT',
 'engine': 'INT',
 'first_blood_time': 'INT',
 'game_mode': 'INT',
 'human_players': 'INT',
 'leagueid': 'INT',
 'lobby_type': 'INT',
 'match_seq_num': 'BIGINT',
 'negative_votes': 'INT',
 'objectives': 'JSON',
 'picks_bans': 'JSON',
 'positive_votes': 'INT',
 'radiant_gold_adv': 'JSON',
 'radiant_score': 'INT',
 'radiant_team_id':'INT',
 'radiant_win': 'BOOLEAN',
 'radiant_xp_adv': 'JSON',
 'start_time': 'INT',
 'teamfights': 'JSON',
 'tower_status_dire': 'INT',
 'tower_status_radiant': 'INT',
 'version': 'INT',
 'replay_salt': 'INT',
 'series_id': 'INT',
 'series_type': 'INT',
 'radiant_team': 'JSON',
 'dire_team': 'JSON',
 'league': 'JSON',
 'skill': 'INT',
 'players': 'JSON',
 'patch': 'INT',
 'region': 'INT',
 'all_word_counts': 'JSON',
 'my_word_counts': 'JSON',
 'throw': 'INT',
 'comeback': 'INT',
 'loss': 'INT',
 'win': 'INT',
 'replay_url': 'VARCHAR(255)',
 'radiant_team_complete':'INT',
 'dire_team_complete':'INT',
 'radiant_captain':'VARCHAR(50)',
 'dire_captain':'VARCHAR(50)'
 }

teamLeagueInfo = {
    'league_id':'INT',
    'team_id':"BIGINT",
    'rating':'DOUBLE',
    'wins':'INT',
    'losses':'INT',
    'last_match_time':'BIGINT',
    'name':'VARCHAR(50)',
    'tag':'VARCHAR(50)',
    'logo_url':'VARCHAR(200)'
}

leagueInfo = {
    'leagueid':'INT',
    'ticket':'VARCHAR(100)',
    'banner':'VARCHAR(100)',
    'tier':'VARCHAR(20)',
    'name':'VARCHAR(100)'
}

create_table(cursor, "league_team_info", teamLeagueInfo)
create_table(cursor, "league_info", leagueInfo)
create_table(cursor, "match_data", matchStructure)

leagues_url = "https://api.opendota.com/api/leagues"
leagues = requests.get(leagues_url).json()

print('Inserting leagues into DB. Total leagues:', len(leagues))
for league in leagues:
    insert_into_table(cursor, "league_info", league)

mydb.commit()