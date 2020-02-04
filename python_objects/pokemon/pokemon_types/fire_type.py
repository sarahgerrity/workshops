from python_objects.attacks.ember import Ember
from python_objects.pokemon.pokemon_types.pokemon import Pokemon


class FireType(Pokemon):

    def __init__(self, pokemon, hp, pokedex_description=None):
        super().__init__(hp, pokedex_description=pokedex_description)
        self.ember = Ember(pokemon)
