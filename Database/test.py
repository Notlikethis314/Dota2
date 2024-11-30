import pandas as pd
import json
df = pd.read_json('D:/Python/Dota2/Database/leagues.json')

df = df.sort_values('leagueid')


print(df)

