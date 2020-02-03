from python_objects.pokemon import Pokemon


class NormalType(Pokemon):

    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense)

    def tackle(self):
        print(f'{self.name} uses tackle!\n')
        return self.attack
