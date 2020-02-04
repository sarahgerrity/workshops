from python_objects.attacks.thunderbolt import Thunderbolt
from python_objects.pokemon.pokemon_types.electric_type import ElectricType


class Jolteon(ElectricType):

    def __init__(self, hp):
        self.name = self.__class__.__name__
        pokedex = 'Jolteon, the Lightning Pokémon. Jolteon becomes enveloped in lightning when angered.'
        super().__init__(self.name, hp, pokedex_description=pokedex)
        self.thunderbolt = Thunderbolt(self.name)
