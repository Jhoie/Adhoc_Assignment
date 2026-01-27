import json
import pandas as pd
import requests

response = requests.get(
    "https://ddragon.leagueoflegends.com/cdn/14.3.1/data/en_US/champion.json")

champion = response.json()
new_json2 = {}

for item in champion["data"].values(): #loops over values not keys
  if item["info"]["attack"] > 5 and item["info"]["defense"] > 5:

    new_json2.update({item["name"]: {"title": item["title"],
                                     "defense": item["info"]["defense"],
                                     "attack": item["info"]["attack"]}
                                      })
    
with open("./powerful_champions.json", "w") as f:
  json.dump(new_json2, f, indent=4)
