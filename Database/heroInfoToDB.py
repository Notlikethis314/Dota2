import requests
import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "dota2"
    )

mycursor = db.cursor()


url = f"https://api.opendota.com/api/matches/"

response = requests.get(url)
data = response.json()

print(data)

for hero in data:
    infoTuple = (hero["id"], hero["name"], hero["localized_name"], hero["primary_attr"], hero["attack_type"])

    mycursor.execute("INSERT INTO hero_data (id, name, localized_name, primary_attr, attack_type) VALUES (%s,%s,%s,%s,%s)",infoTuple)
    db.commit()
