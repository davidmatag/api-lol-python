import json
import requests

def challenLeaByQueue(_reg, _queue, _apiKey):
    """Get the challenger league for given queue"""
    #RANKED_SOLO_5x5, RANKED_FLEX_SR, RANKED_FLEX_TT

    response = requests.get("https://" + _reg + ".api.riotgames.com/lol/league/v4/challengerleagues/by-queue/"+ _queue + "?api_key=" + _apiKey)
    data = json.loads(response.text)

    print(json.dumps(data, indent=4))

def granMasLeaByQueue(_reg, _queue, _apiKey):
    """Get the grandmaster league of a specific queue"""
    #RANKED_SOLO_5x5, RANKED_FLEX_SR, RANKED_FLEX_TT

    response = requests.get("https://" + _reg + ".api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/"+ _queue + "?api_key=" + _apiKey)
    data = json.loads(response.text)

    print(json.dumps(data, indent=4))

def leaById(_reg, _idLeague, _apiKey):
    """Get league with given ID, including inactive entries"""
    #Consistently looking up league ids that don't exist will result in a blacklist

    response = requests.get("https://" + _reg + ".api.riotgames.com/lol/league/v4/leagues/"+ _idLeague + "?api_key=" + _apiKey)
    data = json.loads(response.text)

    print(json.dumps(data, indent=4))

def masLeaByQueue(_reg, _idLeague, _apiKey):
    """Get the master league for given queue"""
    #RANKED_SOLO_5x5, RANKED_FLEX_SR, RANKED_FLEX_TT

    response = requests.get("https://" + _reg + ".api.riotgames.com/lol/league/v4/masterleagues/by-queue/"+ _idLeague + "?api_key=" + _apiKey)
    data = json.loads(response.text)

    print(json.dumps(data, indent=4))

def leaPosAllQueBySumId(_reg, _summonerId, _apiKey):
    """Get league positions in all queues for a given summoner ID"""

    response = requests.get("https://" + _reg + ".api.riotgames.com/lol/league/v4/positions/by-summoner/"+ _summonerId + "?api_key=" + _apiKey)
    data = json.loads(response.text)

    print(json.dumps(data, indent=4))
