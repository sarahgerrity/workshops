from python_objects.flareon import Flareon
from python_objects.jolteon import Jolteon
from python_objects.normal_type import NormalType
from python_objects.vaporeon import Vaporeon


class Eevee(NormalType):

    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense)

    def evolve_with_water_stone(self):
        print(f'The water stone is causing {self.name} to evolve into a Vaporeon!!\n')
        return Vaporeon(self.name, self.hp + 20, self.attack + 20, self.defense + 20)

    def evolve_with_thunder_stone(self):
        print(f'The thunder stone is causing {self.name} to evolve into a Jolteon!!\n')
        return Jolteon(self.name, self.hp + 20, self.attack + 20, self.defense + 20)

    def evolve_with_fire_stone(self):
        print(f'The fire stone is causing {self.name} to evolve into a Flareon!!\n')
        return Flareon(self.name, self.hp + 20, self.attack + 20, self.defense + 20)
