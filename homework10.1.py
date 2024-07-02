
# Напишите программу, которая создает два потока.
# Первый поток должен выводить числа от 1 до 10 с интервалом в 1 секунду.
# Второй поток должен выводить буквы от 'a' до 'j' с тем же интервалом.
# Оба потока должны работать параллельно.
#                        Примечание:
# Используйте методы: start() для старта потока, join() для заморозки дальнейшей интерпретации, пока
# процессы не завершаться.
# Для установки интервала в 1 секунду используйте функцию sleep() из модуля time, предварительно
# импортировав его.

from threading import Thread
from time import sleep

def print_numbers():
    for i in range(1, 11):
        print(i)
        sleep(1)

def print_letters():
    for char in range(ord('a'), ord('j')):
        print(chr(char))
        sleep(1)

thr_first = Thread(target=print_numbers)
thr_second = Thread(target=print_letters)

thr_first.start()
thr_second.start()

thr_first.join()
thr_second.join()