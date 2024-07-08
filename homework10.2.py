
# Напишите программу с использованием механизмов многопоточности, которая создает два потока-рыцаря.
#
# Каждый рыцарь должен иметь имя (name) и умение(skill). Умение рыцаря определяет, сколько времени
# потребуется рыцарю, чтобы выполнить свою защитную миссию для королевства.
# Враги будут нападать в количестве 100 человек. Каждый день рыцарь может ослабить вражеское войско
# на skill-человек.
# Если у рыцаря skill равен 20, то защищать крепость он будет 5 дней (5 секунд в программе).
# Чем выше умение, тем быстрее рыцарь защитит королевство.

from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name, skill):
        Thread.__init__(self)
        self.name = name
        self.skill = skill
    def run(self):
        battle(self)


def battle (n):
    enemies = 100
    print(f"{n.name}, на нас напали!")
    days = 0
    while enemies > 0:
        if enemies > n.skill:
            enemies = enemies - n.skill
        else:
            enemies = 0
        days += 1
        print(f"{n.name}, сражается {days} день(дня)..., осталось {enemies} воинов.")

        sleep(1)
    print(f"{n.name} одержал победу спустя {days} {'день' if days == 1 else 'дней'}!")

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
second1_knight = Knight("Sir Galahad", 100)


first_knight.start()
second_knight.start()
second1_knight.start()

first_knight.join()
second_knight.join()
second1_knight.join()