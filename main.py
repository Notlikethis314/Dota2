import requests

match_id = 7195515861  # Replace with the actual match ID you want to retrieve

  # Replace with your OpenDota API key
url = f"https://api.opendota.com/api/matches/{match_id}"

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    draft_order = data["picks_bans"]
    print(draft_order)
else:
    print("Failed to retrieve match data.")