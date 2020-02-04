class Attack:

    def __init__(self, pokemon, power, attack_name):
        self.pokemon = pokemon
        self.power = power
        self.name = attack_name

    def attack(self):
        print(f'{self.pokemon} uses {self.name.lower()} for {self.power}!\n')
        return self.power
