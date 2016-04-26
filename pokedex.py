from flask import Flask, render_template, request
from random import randint
from data import load_pokemon

app = Flask(__name__)

max_pokemon_id = 647
name_cache = []

@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/pokemon')
def pokemon_page():

    query = request.args.get('name')

    if query in 'random':
        query = str(randint(1, max_pokemon_id))

    pokemon = load_pokemon(query)

    return pokemon_profile("pokemon.html", pokemon)


@app.route('/guess')
def guess_page():

    query = str(randint(1, max_pokemon_id))
    pokemon = load_pokemon(query)

    return pokemon_profile("guess.html", pokemon)

@app.route('/hint')
def hint_page():

    hint = request.args.get('pokemon')

    if len(hint) < 1:
        return ""

    hints = ""
    size = 0

    for pokemon in name_cache:
        a = pokemon.lower().strip()
        b = hint.lower()
        if a.find(b) == 0:
            hints += pokemon.strip() + ", "
            size += 1
            if size > 30:
                break

    return str(hints[:-2])


def pokemon_profile(html_page, pokemon):
    return render_template(html_page,
                           id=pokemon.id,
                           name=pokemon.name,
                           description=pokemon.description,
                           sprite=pokemon.sprite,
                           sound=pokemon.sound,
                           kg=pokemon.get_kilograms(),
                           pounds=pokemon.get_pounds(),
                           meters=pokemon.get_meters(),
                           feet=pokemon.get_feet(),
                           inches=pokemon.get_inches(),
                           type1=pokemon.type1,
                           type2=pokemon.type2,
                           ability1=pokemon.ability1,
                           ability2=pokemon.ability2,
                           ability3=pokemon.ability3,
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


def load_name_cache():
    with open("./static/data/pokemon/name_list.txt") as f:
        global name_cache
        name_cache = f.readlines()

load_name_cache()

app.debug = True
app.run(threaded=True)
