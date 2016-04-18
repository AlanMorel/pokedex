class Stats:

    def __init__(self, pokemon):

        self.hp = pokemon['hp']

        self.attack = pokemon['attack']
        self.special_attack = pokemon['sp_atk']

        self.defense = pokemon['defense']
        self.special_defense = pokemon['sp_def']

        self.speed = pokemon['speed']

        self.exp = pokemon['exp']