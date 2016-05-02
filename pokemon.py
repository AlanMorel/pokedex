from PIL import Image
import data
from stats import Stats
from description import Description


class Pokemon:

    def __init__(self, pokemon):

        national_id = pokemon['national_id']

        self.id = get_id(national_id)
        self.name = pokemon['name'].replace("-", " ").title()
        self.description = Description(pokemon)

        self.sprite = "./static/images/art/" + str(national_id) + ".png"
        self.svg = "./static/images/svg/" + str(national_id) + ".svg"
        self.sound = "./static/sound/" + str(national_id) + ".ogg"

        self.weight = float(int(pokemon['weight']) / 10)
        self.height = float(int(pokemon['height']) / 10)

        self.types = [type['name'] for type in pokemon['types']]
        self.abilities = [ability['name'].replace("-", " ").title() for ability in pokemon['abilities']]
        self.moves = sorted([move['name'].replace("-", " ").title() for move in pokemon['moves']])

        self.stats = Stats(pokemon)

        data.pokemon_cache[int(self.id)] = self
        data.pokemon_cache[self.name.lower()] = self

        print("Added " + self.name + " to cache")
        print(data.pokemon_cache)

    def get_kilograms(self):
        return str(self.weight)

    def get_pounds(self):
        return str(round(self.weight * 2.2, 1))

    def get_meters(self):
        return str(self.height)

    def get_inches(self):
        inches = self.height * 100 * 0.39
        return int(inches % 12)

    def get_feet(self):
        inches = self.height * 100 * 0.39
        return int(inches / 12)

    def get_background_color(self):

        image = Image.open(self.sprite).convert('RGB')

        width, height = image.size
        pixels = image.load()

        r, g, b, count = 0, 0, 0, 0

        for x in range(width):
            for y in range(height):
                pixel = pixels[x, y]

                if pixel[0] < 50 and pixel[1] < 50 and pixel[2] < 50:
                    continue

                if pixel[0] > 200 and pixel[1] > 200 and pixel[2] > 200:
                    continue

                r += int(pixel[0])
                g += int(pixel[1])
                b += int(pixel[2])

                count += 1

        return int(r / count), int(g / count), int(b / count)


def get_id(national_id):
    if national_id < 10:
        return "00" + str(national_id)
    if national_id < 100:
        return "0" + str(national_id)
    return str(national_id)
