from python_objects.attacks.attack import Attack


class Tackle(Attack):

    def __init__(self, pokemon):
        super().__init__(pokemon, 5, self.__class__.__name__)
