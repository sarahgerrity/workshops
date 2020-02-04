class Pokemon:

    def __init__(self, hp, pokedex_description=None):
        self.hp = hp
        self.pokedex = pokedex_description
        self.catch()

    def __str__(self):
        return f'Type: {self.__class__.__name__}\n' \
               f'HP: {self.hp}\n' \
               f'{self.get_pokedex_description()}\n'

    def catch(self):
        print(f'You caught a pokemon!\n{self.__str__()}')

    def get_pokedex_description(self):
        if self.pokedex is None:
            return f'There\'s no information about this Pokemon in your Pokedex.'
        else:
            return self.pokedex
