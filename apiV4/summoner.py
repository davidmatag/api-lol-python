import json
import requests

def sumByAId(_reg, _aId, _apiKey):
    """Get a summoner by account ID"""

    response = requests.get("https://" + _reg + ".api.riotgames.com/lol/summoner/v4/summoners/by-account/"+ _aId + "?api_key=" + _apiKey)
    data = json.loads(response.text)

    print(json.dumps(data, indent=4))

def sumByName(_reg, _sumName, _apiKey):
    """Get a summoner by summoner name"""

    response = requests.get("https://" + _reg + ".api.riotgames.com/lol/summoner/v4/summoners/by-name/"+ _sumName + "?api_key=" + _apiKey)
    data = json.loads(response.text)

    print(json.dumps(data, indent=4))

def sumByPid(_reg, _puuid, _apiKey):
    """Get a summoner by PUUID"""

    response = requests.get("https://" + _reg + ".api.riotgames.com/lol/summoner/v4/summoners/by-puuid/"+ _puuid + "?api_key=" + _apiKey)
    data = json.loads(response.text)

    print(json.dumps(data, indent=4))

def sumBySId(_reg, _sumId, _apiKey):
    """Get a summoner by summoner ID"""

    response = requests.get("https://" + _reg + ".api.riotgames.com/lol/summoner/v4/summoners/"+ _sumId + "?api_key=" + _apiKey)
    data = json.loads(response.text)

    print(json.dumps(data, indent=4))
