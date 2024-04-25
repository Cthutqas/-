# Создайте новый класс Building
# Создайте инициализатор для класса Building, который будет задавать целочисленный атрибут этажности
# self.numberOfFloors и строковый атрибут self.buildingType
# Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors и buildingType для сравнения
# Полученный код напишите в ответ к домашему заданию

class Building():
    def __init__(self, num, type):
        self.numberOfFloors = num
        self.buildingType = type

        def __eq__(self, other):
            return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

build_1 = Building(9, "Панельный")
build_2 = Building(5, "Кирпичный")
build_3 = Building(9, "Панельный")

print(build_1 == build_2)
print(build_1 != build_3)
print(build_2 == build_3)