from flask import Flask, render_template, request
from pokemon import Pokemon, load_from_cache
from random import randint

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pokemon')
def pokemon():

    query = request.args.get('name')

    if query in 'random':
        query = str(randint(1, 647))

    pokemon = load_from_cache(query)

    if pokemon is None:
        pokemon = Pokemon(query)

    return render_template('pokemon.html',
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

@app.route('/guess')
def guess():
    id = str(randint(1, 647))

    pokemon = load_from_cache(id)

    if pokemon is None:
        pokemon = Pokemon(id)

    return render_template('guess.html',
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

app.debug = True
app.run(threaded=True)
