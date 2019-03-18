import json
import requests

def allChampMast(_reg, _summonerId, _apiKey):
    """Get all champion mastery entries sorted by number of champion points descending"""

    response = requests.get("https://" + _reg + ".api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + _summonerId +"?api_key=" + _apiKey)
    data = json.loads(response.text)

    print(json.dumps(data, indent=4))

def champMast(_reg, _summonerId, _championId):
    """Get a champion mastery by player ID and champion ID"""

    response = requests.get("https://" + _reg + ".api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/" + _summonerId +"/by-champion/" + _championId +"?api_key=" + _apiKey)
    data = json.loads(response.text)

    print(json.dumps(data, indent=4))

def totalScoreChampMast(_reg, _summonerId, _apiKey):
    """Get a player's total champion mastery score, which is the sum of individual champion mastery levels"""

    response = requests.get("https://" + _reg + ".api.riotgames.com/lol/champion-mastery/v4/scores/by-summoner/" + _summonerId + "?api_key=" + _apiKey)
    data = json.loads(response.text)

    print(json.dumps(data, indent=4))
