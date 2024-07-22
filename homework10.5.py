
# Моделирование программы для управления данными о движении товаров на складе и эффективной обработки запросов
# на обновление информации в многопользовательской среде.
#
# Представим, что у вас есть система управления складом, где каждую минуту поступают запросы на обновление
# информации о поступлении товаров и отгрузке товаров.
# Наша задача заключается в разработке программы, которая будет эффективно обрабатывать эти запросы в
# многопользовательской среде, с использованием механизма мультипроцессорности для обеспечения быстрой реакции
# на поступающие данные.

from multiprocessing import Process, Lock
# from threading import Lock
import logging


class ErrorOperation(Exception):
    def __init__(self, message='Operation Error', add_info=None):
        super().__init__()
        self.message = message
        self.add_info = add_info


class ErrorProduct(Exception):
    def __init__(self, message='Product Error', add_info=None):
        super().__init__()
        self.message = message
        self.add_info = add_info


class WarehouseManager():
    lock = Lock()

    def __init__(self, data: dict = None):
        if not data:
            data = {}
        self.data = data

    def __str__(self):
        return str(self.data)

    def process_request(self, request: tuple):
        def create_operation(operation):
            if operation == 'receipt':
                def operation(prod, count):
                    with WarehouseManager.lock:
                        self.data[prod] = self.data[prod] + count if prod in self.data else count

                return operation
            elif operation == 'shipment':
                def operation(prod, count):
                    with WarehouseManager.lock:
                        if prod in self.data:
                            self.data[prod] = self.data[prod] - count if count < self.data[prod] else 0
                        else:
                            raise ErrorProduct(f'Нет такого продукта {prod}')

                return operation
            else:
                raise ErrorOperation(f'Некорректно введена операция {operation}')

        log = logging.getLogger(__name__)
        try:
            func = create_operation(request[1])
            func(request[0], request[2])
        except ErrorProduct as e:
            log.error(e.message)
        except ErrorOperation as e:
            log.error(e.message)
        except Exception as e:
            log.exception(e)
        print(request, ':\t', self)

    def run(self, requests):
        processes = []
        for req in requests:
            proc = Process(target=self.process_request(req))
            processes.append(proc)
        for i in processes:
            i.start()
        for i in processes:
            i.join()

if __name__ == '__main__':

    manager = WarehouseManager()

    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]
    manager.run(requests)
    print()
    print(manager)