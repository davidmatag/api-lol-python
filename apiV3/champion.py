import json
import requests

def champRotation(_reg, _apiKey):
    """Returns champion rotations, including free-to-play rotations(REST)"""

    response = requests.get("https://" + _reg + ".api.riotgames.com/lol/platform/v3/champion-rotations?api_key=" + _apiKey)
    data = json.loads(response.text)

    print(json.dumps(data, indent=4))
