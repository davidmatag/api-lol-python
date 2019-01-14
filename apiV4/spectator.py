import json
import requests

def cGameBySumId(_reg, _summonerId, _apiKey):
    """Get current game information for the given summoner id"""

    response = requests.get("https://" + _reg + ".api.riotgames.com/lol/spectator/v4/active-games/by-summoner/"+ _summonerId + "?api_key=" + _apiKey)
    data = json.loads(response.text)

    print(json.dumps(data, indent=4))

def featGames(_reg, _apiKey):
    """Get list of featured games"""

    response = requests.get("https://" + _reg + ".api.riotgames.com/lol/spectator/v4/featured-games?api_key=" + _apiKey)
    data = json.loads(response.text)

    print(json.dumps(data, indent=4))
