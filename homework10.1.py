
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
n_1 = [1, 11]
n_2 = ['a', 'j']
res = []
def func(*args, **kwargs):
    for i in range(*args, **kwargs):
        res.append(i)

thr_first = Thread(target=func, args=n_1)
thr_second = Thread(target=func, args=n_2)

thr_first.start(), sleep(1)
thr_second.start(), sleep(1)

thr_first.join()
thr_second.join()

print(res)