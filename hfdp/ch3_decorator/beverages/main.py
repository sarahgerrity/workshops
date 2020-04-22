from hfdp.ch3_decorator.beverages.beverages import Espresso, DarkRoast, HouseBlend
from hfdp.ch3_decorator.beverages.condiments import Mocha, Whip, Soy

if __name__ == '__main__':
    beverage = Espresso()
    print(f'{beverage.description} ${beverage.cost:.2f}')

    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(f'{beverage2.description} ${beverage2.cost:.2f}')

    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(f'{beverage3.description} ${beverage3.cost:.2f}')
