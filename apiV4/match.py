import json
import requests

def matById(_reg, _matchId, _apiKey):
    """Get match by match ID"""

    response = requests.get("https://" + _reg + ".api.riotgames.com/lol/match/v4/matches/"+ _matchId + "?api_key=" + _apiKey)
    data = json.loads(response.text)

    print(json.dumps(data, indent=4))

def allMatch(_reg, _accountId, _apiKey):
    """Get matchlist for games played on given account ID and filtered using given filter parameters, if any"""

    response = requests.get("https://" + _reg + ".api.riotgames.com/lol/match/v4/matchlists/by-account/"+ _accountId + "?api_key=" + _apiKey)
    data = json.loads(response.text)

    print(json.dumps(data, indent=4))

def timeLineById(_reg, _matchId, _apiKey):
    """Get match timeline by match ID"""

    response = requests.get("https://" + _reg + ".api.riotgames.com/lol/match/v4/timelines/by-match/"+ _summonerId + "?api_key=" + _apiKey)
    data = json.loads(response.text)

    print(json.dumps(data, indent=4))

def matIdByTourCode(_reg, _tournamentCode, _apiKey):
    """Get match IDs by tournament code"""

    response = requests.get("https://" + _reg + ".api.riotgames.com/lol/match/v4/matches/by-tournament-code/" + _tournamentCode + "/ids?api_key=" + _apiKey)
    data = json.loads(response.text)

    print(json.dumps(data, indent=4))

def matByIdaTourCode(_reg, _matchId, _tournamentCode, _apiKey):
    """Get match by match ID and tournament code"""

    response = requests.get("https://" + _reg + ".api.riotgames.com/lol/match/v4/matches/" + _matchId + "/by-tournament-code/" + _tournamentCode + "?api_key=" + _apiKey)
    data = json.loads(response.text)

    print(json.dumps(data, indent=4))
