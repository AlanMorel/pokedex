from pokemon import Pokemon
import json
import requests

API_URL = 'http://pokeapi.co'

POKEMON_API = '/api/v1/pokemon/'

pokemon_cache = {}


def query(uri):
    response = requests.get(API_URL + uri)

    if response.status_code == 200:
        return json.loads(response.text)

    return None


def load_pokemon(query):
    query = query.lower()

    pokemon = load_from_cache(query)

    try:
        if pokemon is None:
            data = load_from_json(query)
            pokemon = Pokemon(data)

        if pokemon is None:
            data = load_from_api(query)
            pokemon = Pokemon(data)

        return pokemon
    except:
        return None


def load_from_cache(key):
    if key.isdigit():
        key = int(key)
    return pokemon_cache.get(key)


def load_from_json(key):
    try:
        if key.isdigit():
            with open('./static/data/pokemon/id/' + str(key) + '.json') as file:
                return json.load(file)
        else:
            with open('./static/data/pokemon/name/' + key + '.json') as file:
                return json.load(file)
    except:
        pass

    return None


def load_from_api(id):
    return query(POKEMON_API + id)
