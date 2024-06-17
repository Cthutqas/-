
# Дан список целых чисел, примените функции map и filter так,
# чтобы в конечном списке оставить нечётные квадраты чисел

def func_1(x):
    return x ** 2

def func_2(x):
    return x % 2

my_namber = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

result = map(func_1, filter(func_2, my_namber))

print(list(result))

