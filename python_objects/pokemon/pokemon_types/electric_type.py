from python_objects.attacks.thunder_shock import ThunderShock
from python_objects.pokemon.pokemon_types.pokemon import Pokemon


class ElectricType(Pokemon):

    def __init__(self, pokemon, hp, pokedex_description=None):
        super().__init__(hp, pokedex_description=pokedex_description)
        self.thunder_shock = ThunderShock(pokemon)
