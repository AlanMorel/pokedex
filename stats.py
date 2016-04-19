class Stats:

    red = "#c0392b"
    yellow = "#f1c40f"
    green = "#27ae60"
    purple = "#8e44ad"

    def __init__(self, pokemon):

        self.hp = pokemon['hp']

        self.attack = pokemon['attack']
        self.special_attack = pokemon['sp_atk']

        self.defense = pokemon['defense']
        self.special_defense = pokemon['sp_def']

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
        return [Stats.red if i < 30 else
                (Stats.yellow if i < 50 else
                    (Stats.green if i < 65 else
                        Stats.purple))
                for i in self.get_bar_values()]


def get_bar_value(value):
    return min(int(float(value / 180) * 100), 100)
