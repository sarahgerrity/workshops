from python_objects.pokemon.eevee import Eevee
from python_objects.pokemon.jolteon import Jolteon


def main():
    my_pokemon = Eevee(127)
    my_pokemon.tackle.attack()
    rainer = my_pokemon.evolve_with_water_stone()
    rainer.hydro_pump.attack()

    my_jolteon = Jolteon(140)


if __name__ == '__main__':
    main()
