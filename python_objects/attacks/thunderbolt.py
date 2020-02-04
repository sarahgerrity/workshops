from python_objects.attacks.attack import Attack


class Thunderbolt(Attack):

    def __init__(self, pokemon):
        super().__init__(pokemon, 80, self.__class__.__name__)
