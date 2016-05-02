class Stats:

    red = "#c0392b"
    yellow = "#f1c40f"
    green = "#27ae60"
    purple = "#8e44ad"

    def __init__(self, pokemon):

        self.attack = pokemon['attack']
        self.special_attack = pokemon['sp_atk']

        self.defense = pokemon['defense']
        self.special_defense = pokemon['sp_def']

        self.hp = pokemon['hp']
        self.speed = pokemon['speed']
        self.exp = pokemon['exp']

    def get_bar_values(self):
        return (
                get_bar_value(self.attack),
                get_bar_value(self.special_attack),
                get_bar_value(self.defense),
                get_bar_value(self.special_defense),
                )

    def get_bar_colors(self):
        return [Stats.red if value < 30 else
                (Stats.yellow if value < 50 else
                    (Stats.green if value < 65 else
                        Stats.purple))
                for value in self.get_bar_values()]


def get_bar_value(value):
    return min(int(float(value / 180) * 100), 100)
