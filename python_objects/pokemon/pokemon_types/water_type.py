from python_objects.attacks.water_gun import WaterGun
from python_objects.pokemon.pokemon_types.pokemon import Pokemon


class WaterType(Pokemon):

    def __init__(self, pokemon, hp, pokedex_description=None):
        super().__init__(hp, pokedex_description=pokedex_description)
        self.water_gun = WaterGun(pokemon)
