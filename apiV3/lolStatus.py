import json
import requests

def currenStatus(_reg, _apiKey):
    """Get League of Legends status for the given shard"""

    response = requests.get("https://" + _reg + ".api.riotgames.com/lol/status/v3/shard-data?api_key=" + _apiKey)
    data = json.loads(response.text)

    print(json.dumps(data, indent=4))
