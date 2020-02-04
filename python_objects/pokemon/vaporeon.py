from python_objects.attacks.hydro_pump import HydroPump
from python_objects.pokemon.pokemon_types.water_type import WaterType


class Vaporeon(WaterType):

    def __init__(self, hp):
        self.name = self.__class__.__name__
        pokedex = 'Vaporeon, the Bubble Jet Pokémon. Vaporeon is made up of molecules similar to water, which ' \
                  'allows it to melt and vanish.'
        super().__init__(self.name, hp, pokedex_description=pokedex)
        self.hydro_pump = HydroPump(self.name)
