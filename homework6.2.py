# Создайте родительский(базовый) класс Vehicle, который имеет свойство vehicle_type = "none"
# Создайте родительский(базовый) класс Car, который имеет свойство price = 1000000 и функцию
# def horse_powers, которая возвращает количество лошидиных сил для автомобиля
# Создайте наследника класса Car и Vehicle - класс Nissan и переопределите свойство price и vehicle_type,
# а также переопределите функцию horse_powers
# Создайте экзмепляр класса Nissan и распечайте через функцию print vehicle_type, price

class Vehicle ():
    def __init__(self):
        self.vehicle_type = "none"


class Car():
    def __init__(self):
        self.prise = 1000000
        self.powerofcars = 190

    def horse_powers(self):
        return 'мощность', self.PowerOfCars


class Nissan(Vehicle, Car):
    def __init__(self):
        super().__init__()
        self.vehicle_type = "off-road vehicle"
        self.prise = 1058930
        self.powerofcars = 200

    def horse_powers(self):
        return 'мощность', self.powerofcars

car = Nissan()
print('Ниссан')
print(car.horse_powers())
print('тип', car.vehicle_type)
print('цена', car.prise)


