from python_objects.attacks.attack import Attack


class HydroPump(Attack):

    def __init__(self, pokemon):
        super().__init__(pokemon, 130, self.__class__.__name__)
