class House():

    def __init__(self):
        self.numbersOfFloors = 10

print(House().numbersOfFloors)
my_house = House()
for floor in range(1, my_house.numbersOfFloors +1):
    print('Вы поднялись на ', floor, 'этаж')


        # for floor in range = 10