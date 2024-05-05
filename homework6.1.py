
# Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и функцию
# def horse_powers, которая возвращает количество лошидиных сил для автомобиля
# Создайте наследника класса Car - класс Nissan и переопределите свойство price, а также переопределите
# функцию horse_powers
# Дополнительно создайте класс Kia, который также будет наследником класса Car и переопределите также
# свойство price, а также переопределите функцию horse_powers

class Car :
    def __init__(self):
        self.price = 1000000
    def horse_powers(self):
        self.horse_powers = 150

class Nissan (Car):
    def __init__(self):
        self.price = 1324557
    def horse_powers(self):
        self.horse_powers = 190

class Kia(Car):
    def __init__(self):
        self.price = 1582900
    def horse_powers(self):
        self.horse_powers = 140

car = Car ()
print('машина')
print('цена', car.price)
print('мощность', car.horse_powers)

terrano = Nissan ()
print('Ниссан')
print('цена', terrano.price)
print('мощность', terrano.horse_powers)

kia = Kia ()
print('Киа')
print('цена', kia.price)
print('мощность', kia.horse_powers)
