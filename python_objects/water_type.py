from python_objects.pokemon import Pokemon


class WaterType(Pokemon):

    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense)

    def water_gun(self):
        print(f'{self.name} uses water gun!\n')
        return self.attack
