from python_objects.attacks.tackle import Tackle
from python_objects.pokemon.pokemon_types.pokemon import Pokemon


class NormalType(Pokemon):

    def __init__(self, pokemon, hp, pokedex_description=None):
        super().__init__(hp, pokedex_description=pokedex_description)
        self.tackle = Tackle(pokemon)
