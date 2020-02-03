from python_objects.eevee import Eevee


def main():
    my_pokemon = Eevee("Eevee", 60, 80, 100)
    print(my_pokemon.__str__())
    my_pokemon.tackle()
    sparky = my_pokemon.evolve_with_thunder_stone("Sparky")
    print(sparky.__str__())
    sparky.thunder_shock()


if __name__ == '__main__':
    main()
