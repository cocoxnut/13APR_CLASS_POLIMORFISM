class Human:
    default_name = 'no name'
    default_age = 0

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = 0

    def info(self):
        print(f'name : {self.name}')
        print(f'age : {self.age}')
        print(f'money : {self.__money}')
        print(f'house : {self.__house}')

    @staticmethod
    def default_info():
        print(f'name : {Human.default_name} age : {Human.default_age}')

    def __make_deal(self, house, money):
        self.__house = house
        self.__money = money

    def earn_money(self, salary):
        self.__money += salary
        print(f'You earned {salary} money, your budget is {self.__money}')

    def buy_house(self, house=0, price=0):
        house_price = house.final_price(price)
        if self.__money >= house_price:
            self.__make_deal(house, house_price)
            print('You bought a house')
        else:
            print('Money is not enough')


class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = round(self._price * (100 - discount) / 100, 2)
        print(f'Price with discount {final_price}')
        return final_price


class SmallHouse(House):
    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)


bakyt = Human('Bakyt', 16)
bakyt.info()
bakyt.default_info()
bakyt.earn_money(100000)
bakyt.info()
house = House(100, 100000)
small_house = SmallHouse(50000)
bakyt.info()
print('Bakyt is joined to Google')
bakyt.earn_money(50000)
bakyt.buy_house(small_house, 30)
print('Bakyt is joined to Amazon')
print('Bakyt and Elon Musk are best friends')
bakyt.earn_money(1000000)
bakyt.buy_house(house, 20)
bakyt.info()
