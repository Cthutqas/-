
# Моделирование работы сети кафе с несколькими столиками и потоком посетителей, прибывающих для заказа пищи и
# уходящих после завершения приема.
#
# Есть сеть кафе с несколькими столиками. Посетители приходят, заказывают еду, занимают столик, употребляют еду
# и уходят. Если столик свободен, новый посетитель принимается к обслуживанию, иначе он становится в очередь на
# ожидание.
#
# Создайте 3 класса:
# Table - класс для столов, который будет содержать следующие атрибуты: number(int) - номер стола,
# is_busy(bool) - занят стол или нет.
#
# Cafe - класс для симуляции процессов в кафе. Должен содержать следующие атрибуты и методы:
# Атрибуты queue - очередь посетителей (создаётся внутри init), tables список столов (поступает из вне).
# Метод customer_arrival(self) - моделирует приход посетителя(каждую секунду).
# Метод serve_customer(self, customer) - моделирует обслуживание посетителя. Проверяет наличие свободных
# столов, в случае наличия стола - начинает обслуживание посетителя (запуск потока), в противном
# случае - посетитель поступает в очередь. Время обслуживания 5 секунд.
# Customer - класс (поток) посетителя. Запускается, если есть свободные столы.
#
# Так же должны выводиться текстовые сообщения соответствующие событиям:
# Посетитель номер <номер посетителя> прибыл.
# Посетитель номер <номер посетителя> сел за стол <номер стола>. (начало обслуживания)
# Посетитель номер <номер посетителя> покушал и ушёл. (конец обслуживания)
# Посетитель номер <номер посетителя> ожидает свободный стол. (помещение в очередь)

import threading
import time
from queue import Queue

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False

class Cafe:
    def __init__(self, num_tables):
        self.queue = Queue()
        self.tables = Queue()
        for i in range(num_tables):
            self.tables.put(Table(i + 1))
        self.customers_served = 0  # Счетчик обслуженных посетителей
        self.customer_number = 1    # Счетчик прибывших посетителей
        self.max_customers = 20     # Максимальное количество посетителей

    def customer_arrival(self):
        while self.customer_number <= self.max_customers:
            print(f"Посетитель номер {self.customer_number} прибыл.")
            customer_thread = Customer(self.customer_number, self)
            customer_thread.start()
            self.customer_number += 1
            time.sleep(1)

    def serve_customer(self, customer):
        table = self.tables.get()
        while table.is_busy:
            self.tables.put(table)
            table = self.tables.get()

        table.is_busy = True
        print(f"Посетитель номер {customer.number} сел за стол {table.number}.")
        time.sleep(5)
        table.is_busy = False
        print(f"Посетитель номер {customer.number} покушал и ушёл.")
        self.tables.put(table)
        self.customers_served += 1  # Увеличиваем счетчик обслуженных посетителей

    def enqueue_customer(self, customer):
        self.queue.put(customer)
        print(f"Посетитель номер {customer.number} ожидает свободный стол.")

    def dequeue_customer(self):
        if not self.queue.empty():
            customer = self.queue.get()
            self.serve_customer(customer)

class Customer(threading.Thread):
    def __init__(self, number, cafe):
        super().__init__()
        self.number = number
        self.cafe = cafe

    def run(self):
        self.cafe.enqueue_customer(self)
        self.cafe.dequeue_customer()

# Создаем столики в кафе
num_tables = 3
cafe = Cafe(num_tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы всех потоков-посетителей
customer_arrival_thread.join()

# Дожидаемся завершения обслуживания всех 20 посетителей
while cafe.customers_served < cafe.max_customers:
    time.sleep(1)

print("Обслуживание всех посетителей завершено.")