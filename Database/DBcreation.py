import mysql.connector
from functions import *

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "dota2"
    )

mycursor = db.cursor()


#mycursor.execute("""CREATE TABLE hero_data (
#    id INTEGER COMMENT 'The ID value of the hero played',
#    name VARCHAR(255) COMMENT 'Dota hero command name',
#    localized_name VARCHAR(255) COMMENT 'Hero name',
#    primary_attr VARCHAR(10) COMMENT 'Hero primary shorthand attribute name, e.g., "agi"',
#    attack_type VARCHAR(10) COMMENT 'Hero attack type, either "Melee" or "Ranged"')
#""")
"""
mycursor.execute(CREATE TABLE match_data (
    match_id BIGINT COMMENT 'The ID number of the match assigned by Valve',
    barracks_status_dire INTEGER COMMENT 'Bitmask representing the standing status of Dire barracks',
    barracks_status_radiant INTEGER COMMENT 'Bitmask representing the standing status of Radiant barracks',
    dire_score INTEGER COMMENT 'Number of kills the Dire team had when the match ended',
    draft_timings TEXT COMMENT 'Array containing information on the draft timings',
    duration INTEGER COMMENT 'Duration of the game in seconds',
    first_blood_time INTEGER COMMENT 'Time in seconds at which first blood occurred',
    game_mode INTEGER COMMENT 'Integer corresponding to the game mode played',
    leagueid INTEGER COMMENT 'League ID',
    lobby_type INTEGER COMMENT 'Integer corresponding to the lobby type of the match',
    match_seq_num BIGINT COMMENT 'Match sequence number',
    negative_votes INTEGER COMMENT 'Number of negative votes the replay received in the in-game client',
    objectives TEXT COMMENT 'Array containing information on objectives',
    picks_bans TEXT COMMENT 'Array containing information on the draft picks and bans',
    positive_votes INTEGER COMMENT 'Number of positive votes the replay received in the in-game client',
    radiant_gold_adv INTEGER COMMENT 'Array of the Radiant gold advantage at each minute in the game',
    radiant_score INTEGER COMMENT 'Number of kills the Radiant team had when the match ended',
    radiant_win BOOLEAN COMMENT 'Boolean indicating whether Radiant won the match',
    radiant_xp_adv INTEGER COMMENT 'Array of the Radiant experience advantage at each minute in the game',
    start_time INTEGER COMMENT 'The Unix timestamp at which the game started',
    teamfights TEXT COMMENT 'Array containing information on teamfights',
    tower_status_dire INTEGER COMMENT 'Bitmask representing the standing status of Dire towers',
    tower_status_radiant INTEGER COMMENT 'Bitmask representing the standing status of Radiant towers',
    version INTEGER COMMENT 'Parse version used internally by OpenDota',
    replay_salt INTEGER COMMENT 'Replay salt',
    series_id INTEGER COMMENT 'Series ID',
    series_type INTEGER COMMENT 'Series type',
    radiant_team TEXT COMMENT 'Radiant team',
    dire_team TEXT COMMENT 'Dire team',
    league TEXT COMMENT 'League',
    skill INTEGER COMMENT 'Skill bracket assigned by Valve',
    players TEXT COMMENT 'Array of information on individual players',
    patch INTEGER COMMENT 'Information on the patch version the game is played on',
    region INTEGER COMMENT 'Integer corresponding to the region the game was played on',
    all_word_counts TEXT COMMENT 'Word counts of the all chat messages in the players games',
    my_word_counts TEXT COMMENT 'Word counts of the players all chat messages',
    throw INTEGER COMMENT 'Maximum gold advantage of the players team if they lost the match',
    comeback INTEGER COMMENT 'Maximum gold disadvantage of the players team if they won the match',
    loss INTEGER COMMENT 'Maximum gold disadvantage of the players team if they lost the match',
    win INTEGER COMMENT 'Maximum gold advantage of the players team if they won the match',
    replay_url VARCHAR(255) COMMENT 'Replay URL'
)
)"""

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
 'radiant_team_name':'VARCHAR(200)',
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

#drop_table(mycursor, "match_data")

#create_table(mycursor, "match_data", matchStructure)

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

#create_table(mycursor, "league_team_info", teamLeagueInfo)
#drop_table(mycursor, "league_info")
create_table(mycursor, "league_info", leagueInfo)