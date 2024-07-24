
                  # Задача "Проверка на выносливость":
# В первую очередь скачайте исходный код, который нужно обложить тестами с GitHub. (Можно скопировать)
# В этом коде сможете обнаружить класс Runner, объекты которого вам будет необходимо протестировать.
#
# Напишите класс RunnerTest, наследуемый от TestCase из модуля unittest. В классе пропишите следующие методы:
# test_walk - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод walk у
# этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 50.
# test_run - метод, в котором создаётся объект класса Runner с произвольным именем. Далее вызовите метод run у
# этого объекта 10 раз. После чего методом assertEqual сравните distance этого объекта со значением 100.
# test_challenge - метод в котором создаются 2 объекта класса Runner с произвольными именами. Далее 10 раз у
# объектов вызываются методы run и walk соответственно. Т.к. дистанции должны быть разными, используйте метод
# assertNotEqual, чтобы убедится в неравенстве результатов.
# Запустите кейс RunnerTest. В конечном итоге все 3 теста должны пройти проверк

import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        run1 = Runner('Вася')
        a = 0
        for i in range(0, 10):
            a += 1
            run1.walk()
        dist1 = run1.distance
        self.assertEqual(dist1, 50)

    def test_run(self):
        run2 = Runner('Петя')
        a = 0
        for _ in range(0, 10):
            a += 1
            run2.run()
        self.assertEqual(run2.distance, 100)

    def test_challenge(self):
        run3 = Runner('Коля')
        run4 = Runner('Юра')
        a = 0
        for _ in range(0, 10):
            a += 1
            run3.run()
            run4.walk()
        self.assertNotEqual(run3.distance, run4.distance, )

if __name__ == '__main__':
    unittest.main
