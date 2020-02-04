from python_objects.pokemon.flareon import Flareon
from python_objects.pokemon.jolteon import Jolteon
from python_objects.pokemon.pokemon_types.normal_type import NormalType
from python_objects.pokemon.vaporeon import Vaporeon


class Eevee(NormalType):

    def __init__(self, hp):
        super().__init__(self.__class__.__name__, hp)

    def evolve_with_water_stone(self):
        print(f'The water stone is causing Eevee to evolve into a Vaporeon!!\n')
        return Vaporeon(self.hp + 103)

    def evolve_with_thunder_stone(self):
        print(f'The thunder stone is causing Eevee to evolve into a Jolteon!!\n')
        return Jolteon(self.hp + 13)

    def evolve_with_fire_stone(self):
        print(f'The fire stone is causing Eevee to evolve into a Flareon!!\n')
        return Flareon(self.hp + 13)
