class Pokemon:

    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Type: {self.__class__.__name__}\n' \
               f'HP: {self.hp}\n' \
               f'Attack: {self.attack}\n' \
               f'Defense: {self.defense}\n'

