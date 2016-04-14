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
                           kg=pokemon.kg,
                           pounds=pokemon.pounds,
                           meters=pokemon.meters,
                           feet=pokemon.feet,
                           inches=pokemon.inches,
                           type1=pokemon.type1,
                           type2=pokemon.type2,
                           hp=pokemon.hp,
                           attack=pokemon.attack,
                           special_attack=pokemon.special_attack,
                           defense=pokemon.defense,
                           special_defense=pokemon.special_defense,
                           speed=pokemon.speed,
                           exp=pokemon.exp,
                           background_color=pokemon.background_color)

app.debug = True
app.run(threaded = True)
