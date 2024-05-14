#                       Домашнее задание по уроку "Try и Except".

# Реализуйте следующую функцию:
# add_everything_up, будет складывать числа(int, float) и строки(str)

def add_everything_up(a, b):
    return (a, b)

try:
    print(sum())
except TypeError as exc:
    print('a и b разного типа ', exc)
else:
    print('ура, все получилось')
finally:
    print('задание выполнено')

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
