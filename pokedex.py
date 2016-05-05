from flask import Flask, render_template, request, redirect, url_for
from random import randint
from data import load_pokemon

app = Flask(__name__)

name_cache = []


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/pokemon')
def pokemon_page():

    query = request.args.get('name')

    if query is None:
        return redirect(url_for('index_page'))

    pokemon = load_pokemon(query)
    if pokemon is None:
        return redirect(url_for('index_page'))

    return pokemon_profile("pokemon.html", pokemon)


@app.route('/guess')
def guess_page():

    max_pokemon_id = 647
    query = str(randint(1, max_pokemon_id))

    pokemon = load_pokemon(query)
    if pokemon is None:
        return redirect(url_for('index_page'))

    return pokemon_profile("guess.html", pokemon)


@app.route('/api')
def api_page():

    query = request.args.get('q').lower()

    if query is None or len(query) < 1:
        return ""

    suggestions = ["<a href='/pokemon?name=" + pokemon.strip().lower() + "'>" + pokemon.strip() + "</a>" for pokemon in name_cache if pokemon.lower().strip().find(query) == 0]

    return " ".join(suggestions)


def pokemon_profile(html_page, pokemon):
    return render_template(html_page,
                           id=pokemon.id,
                           name=pokemon.name,
                           normal_description=pokemon.description.get_normal_description(),
                           hidden_description=pokemon.description.get_hidden_description(),
                           sprite=pokemon.sprite,
                           svg=pokemon.svg,
                           sound=pokemon.sound,
                           kg=pokemon.get_kilograms(),
                           pounds=pokemon.get_pounds(),
                           meters=pokemon.get_meters(),
                           feet=pokemon.get_feet(),
                           inches=pokemon.get_inches(),
                           types=pokemon.types,
                           abilities=pokemon.abilities,
                           moves=pokemon.moves,
                           hp=pokemon.stats.hp,
                           attack=pokemon.stats.attack,
                           special_attack=pokemon.stats.special_attack,
                           defense=pokemon.stats.defense,
                           special_defense=pokemon.stats.special_defense,
                           speed=pokemon.stats.speed,
                           exp=pokemon.stats.exp,
                           background_color=pokemon.get_background_color(),
                           bar_values=pokemon.stats.get_bar_values(),
                           bar_colors=pokemon.stats.get_bar_colors(),
                           )


with open("./static/data/pokemon/name_list.txt") as f:
    name_cache = f.readlines()

app.debug = True
app.run(threaded=True)