class House():

    def __init__(self):
        self.numberOfFloors = 0
    def setNewNumberOfFloors(self, floors=3):
        self.numberOfFloors = floors
        print("Number of Floors: ", self.numberOfFloors)

home = House()

print(home.numberOfFloors)
home.setNewNumberOfFloors(10)
home.setNewNumberOfFloors()