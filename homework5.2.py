class House():

    def __init__(self):
        self.numberOfFloors = 12
    def elevator(self):
        for floor in range(1, self.numberOfFloors + 1):
            print('Текущий этаж равен ', floor)

my_house = House()
my_house.elevator()
