from python_objects.attacks.attack import Attack


class Ember(Attack):

    def __init__(self, pokemon):
        super().__init__(pokemon, 10, self.__class__.__name__)
