from python_objects.attacks.flamethrower import Flamethrower
from python_objects.pokemon.pokemon_types.fire_type import FireType


class Flareon(FireType):

    def __init__(self, hp):
        self.name = self.__class__.__name__
        super().__init__(self.name, hp)
        self.flamethrower = Flamethrower(self.name)
