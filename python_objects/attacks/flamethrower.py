from python_objects.attacks.attack import Attack


class Flamethrower(Attack):

    def __init__(self, pokemon):
        super().__init__(pokemon, 70, self.__class__.__name__)
