from python_objects.pokemon import Pokemon


class FireType(Pokemon):

    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense)

    def ember(self):
        print(f'{self.name} uses ember!\n')
        return self.attack
