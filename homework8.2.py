
# Создайте минимум два своих собственных исключения, наследуя их от класса Exception.
# Например, InvalidDataException и ProcessingException.
# Напишите функцию, которая генерирует различные исключения в зависимости от передаваемых ей аргументов.
# Добавьте обработку исключений в функции, вызывающие вашу функцию, и передайте исключения дальше
# по стеку вызовов.
# В основной части программы вызовите эти функции и корректно обработай
class InvalidDataException(Exception):
    def __init__(self, message_1, extra_info_1):
        self.message_1 = message_1
        self.extra_info_1 = extra_info_1


class ProcessingException(Exception):
    def __init__(self, message_2, extra_info_2):
        self.message_2 = message_2
        self.extra_info_2 = extra_info_2

list = [2, 45, 12, 56, 8, 9, 31, 58, 345, 13, 67, 95]

def f():
    return a + 3
for a in list:

    def f_1(a):
        if a == 9:
            raise InvalidDataException(Exception)
        print(f'Мое исключение', 'не верные данные')
        if a == 13:
            raise ProcessingException(Exception)
        print('И это мое исключение', ' просто не люблю эту цифру')
    try:
        f()
    except InvalidDataException as e_1:
        print('Сообщение об ошибке:', e_1)
    except InvalidDataException as e_2:
        print(f'Сообщение об ошибке:', e_2)
    rezult = f()
    print(rezult)
else:
    print('задача выполнена')

