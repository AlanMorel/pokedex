from PIL import Image
from query import query
from stats import Stats

API = '/api/v1/pokemon/'


class Pokemon:

    cache = {}

    def __init__(self, identifier):

        identifier = identifier.lower()
        pokemon = query(API + identifier)

        national_id = pokemon['national_id']

        self.id = get_id(national_id)
        self.name = pokemon['name']

        self.description = get_description(pokemon)
        self.sprite = "./static/images/art/" + str(national_id) + ".png"
        self.sound = "./static/sound/" + str(national_id) + ".ogg"

        self.weight = float(int(pokemon['weight']) / 10)
        self.height = float(int(pokemon['height']) / 10)

        self.type1 = pokemon['types'][0]["name"]
        self.type2 = pokemon['types'][1]["name"] if len(pokemon['types']) > 1 else "none"

        self.stats = Stats(pokemon)

        Pokemon.cache[int(self.id)] = self
        Pokemon.cache[self.name.lower()] = self

        print("Added " + self.name + " to cache")
        print(Pokemon.cache)

    def get_silhouette(self):
        image = Image.open(self.sprite)

        width, height = image.size
        pixels = image.load()

        for x in range(width):
            for y in range(height):
                pixel = pixels[x, y]

                try:
                    if pixel[3] is not 255:
                        continue
                except:
                    continue

                pixels[x, y] = (0, 0, 0)

        return image

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
    elif national_id < 100:
        return "0" + str(national_id)
    else:
        return str(national_id)


def get_description(pokemon):
    uri = pokemon['descriptions'][-1]['resource_uri']
    return query(uri)['description']


def load_from_cache(key):
    if key.isdigit():
        key = int(key)
    else:
        key = key.lower()
    return Pokemon.cache.get(key)
