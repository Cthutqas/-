
# Создайте минимум два своих собственных исключения, наследуя их от класса Exception.
# Например, InvalidDataException и ProcessingException.
# Напишите функцию, которая генерирует различные исключения в зависимости от передаваемых ей аргументов.
# Добавьте обработку исключений в функции, вызывающие вашу функцию, и передайте исключения дальше
# по стеку вызовов.
# В основной части программы вызовите эти функции и корректно обработай
class InvalidDataException(Exception):
    def __init__(self, message_1, extra_info_1):
        super().__init__(message_1)
        self.extra_info_1 = extra_info_1


class ProcessingException(Exception):
    def __init__(self, message_2, extra_info_2):
        super().__init__(message_2)
        self.extra_info_2 = extra_info_2

list = [2, 45, 12, 56, 8, 9, 31, 58, 345, 13, 67, 95]

def f(a):
    return a + 3


def f_1(a):
    if a == 9:
        raise InvalidDataException('мое исключение 1', 'extra_info_1')
        # print(f'Мое исключение', 'не верные данные')
    if a == 13:
        raise ProcessingException('мое исключение 2', 'extra_info_2')
        # print('И это мое исключение', ' просто не люблю эту цифру')

for a in list:

    try:
        f_1(a)
    except InvalidDataException as e_1:
        print('Сообщение об ошибке:', e_1)
    except ProcessingException as e_2:
        print(f'Сообщение об ошибке:', e_2)
    else:
        rezult = f(a)
        print(rezult)
print('задача выполнена')

