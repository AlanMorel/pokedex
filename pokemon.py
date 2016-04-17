from query import query
from PIL import Image

API = '/api/v1/pokemon/'


class Pokemon:

    def __init__(self, identifier):

        identifier = identifier.lower()

        pokemon = query(API + identifier)

        description_uri = pokemon['descriptions'][-1]['resource_uri']

        id = pokemon['national_id']

        if id < 10:
            self.id = "00" + str(id)
        elif id < 100:
            self.id = "0" + str(id)
        else:
            self.id = str(id)

        self.name = pokemon['name']
        self.sprite = "./static/images/art/" + str(id) + ".png"
        self.description = query(description_uri)['description']

        weight = float(int(pokemon['weight']) / 10)

        self.kg = str(weight)
        self.pounds = str(round(weight * 2.2, 1))

        height = float(int(pokemon['height']) / 10)
        self.meters = str(height)

        total_inches = height * 100 * 0.39

        self.inches = int(total_inches % 12)
        self.feet = int(total_inches / 12)

        self.type1 = pokemon['types'][0]["name"]
        self.type2 = pokemon['types'][1]["name"] if len(pokemon['types']) > 1 else "none"

        self.hp = pokemon['hp']

        self.attack = pokemon['attack']
        self.special_attack = pokemon['sp_atk']

        self.defense = pokemon['defense']
        self.special_defense = pokemon['sp_def']

        self.speed = pokemon['speed']

        self.exp = pokemon['exp']

        self.background_color = get_background_color(self.sprite)


def get_background_color(path):

    image = Image.open(path)
    image = image.convert('RGB')

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

    return int(r/count), int(g/count), int(b/count)
