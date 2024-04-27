# Создайте новый класс Building с атрибутом total
# Создайте инициализатор для класса Building, который будет увеличивать атрибут количества созданных
# объектов класса Building total (по примеру класса Lemming из урока)
# В цикле создайте 40 объектов класса Building и выведите их на экран командой print
# Полученный код напишите в ответ к домашнему заданию

class Building:
    total = 0

    def __init__(self, total = 1):
        Building.total += 1

for tot in range(1, 41):
    build = Building()
    print('Объект класса № ', tot, build, build.total)