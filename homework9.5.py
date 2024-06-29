
# Напишите 2 функции:
# Функция, которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым
# числом и "Составное" в противном случае.

def sum_three(a, b, c):
    return a + b + c

def is_prime(func):
    def wrapper(*args, **kwargs):
        n = func(*args, **kwargs)
        if n < 2:
            return f'{n}, Составное число'
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return f'{n}, Составное число'
        return f'{n}, Простое число'
    return wrapper
@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
