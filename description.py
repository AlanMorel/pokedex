import data


class Description:

    def __init__(self, pokemon):
        self.name = pokemon['name']
        try:
            uri = pokemon['descriptions'][-1]['resource_uri']
            self.data = data.query(uri)['description']
        except:
            self.data = "Description of Pokémon goes here. API is down! :("


    def get_cleaned_description(self):
        description = self.data.replace("POKMON", "Pokémon")
        description = description.replace("Pokmon", "Pokémon")
        description = description.replace("Pokmons", "Pokémon's")
        return description

    def get_normal_description(self):
        normal_description = self.get_cleaned_description()
        normal_description = normal_description.replace(self.name.upper(), self.name)
        return normal_description

    def get_hidden_description(self):
        hidden_description = self.get_cleaned_description()
        hidden_description = hidden_description.replace(self.name.upper(), "(Pokémon)")
        return hidden_description
