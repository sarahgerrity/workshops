from python_objects.pokemon import Pokemon


class ElectricType(Pokemon):

    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense)

    def thunder_shock(self):
        print(f'{self.name} uses thunder shock!\n')
        return self.attack
