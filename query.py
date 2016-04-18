import json
import requests

API_URL = 'http://pokeapi.co'


def query(uri):

    response = requests.get(API_URL + uri)

    if response.status_code == 200:
        return json.loads(response.text)

    return None
