import json
import requests

BASE_URL = 'http://pokeapi.co'


def query(resource_url):
    url = '{0}{1}'.format(BASE_URL, resource_url)
    response = requests.get(url)

    if response.status_code == 200:
        return json.loads(response.text)
    return None
