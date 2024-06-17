
# Задача 1: Фабрика Функций
# Написать функцию, которая возвращает различные математические функции (например, деление, умножение)
# в зависимости от переданных аргументов.
#
# Задача 2: Лямбда-Функции
# Использовать лямбда-функцию для реализации простой операции и написать такую же функцию
# с использованием def. Например, возведение числа в квадрат
#
# Задача 3: Вызываемые Объекты
# Создать класс с Rect c полями a, b которые задаются в __init__ и методом __call__, который
# возвращает площадь прямоугольника, то есть a*b.


# Задача 1
def create_operation(operation):
    if operation == "/":
        def add(x, y):
            return x / y
        return add
    elif operation == "*":
        def subtract(x, y):
            return x * y
        return subtract
my_func_subtract = create_operation("*")
my_func_add = create_operation("/")

print(my_func_add(27,3))
print(my_func_subtract(3,2))
print()

# Задача 2
multiply = lambda x: x ** 2
print(multiply(3))

def multiply_def(x):
   return x ** 2
print(multiply_def(25))
print()

# Задача 3
class Rect:
   def __init__(self, value):
       self.value = value
   def __call__(self, n):
       return self.value * n

rect = Rect(3)
print(rect(15))
