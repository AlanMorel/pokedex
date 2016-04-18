from flask import Flask, render_template, request, url_for
from pokemon import Pokemon

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pokemon')
def pokemon():
    #pokemon = Pokemon('bulbasaur')

    if (request.args.get('name')):
        pokemon = Pokemon(request.args.get('name'))

    return render_template('pokemon.html',
                           id=pokemon.id,
                           name=pokemon.name,
                           description=pokemon.description,
                           sprite=pokemon.sprite,
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
                           background_color=pokemon.get_background_color())

app.debug = True
app.run(threaded = True)
