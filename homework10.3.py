
# Реализуйте программу, которая имитирует доступ к общему ресурсу с использованием механизма блокировки потоков.
# Класс BankAccount должен отражать банковский счет с балансом и методами для пополнения и снятия денег.
# Необходимо использовать механизм блокировки, чтобы избежать проблемы гонок (race conditions) при модификации
# общего ресурса.

from threading import Thread, Lock

lock = Lock()

class BankAccount(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        deposit_task(self)
        withdraw_task(self)

account = BankAccount()

def deposit_task(account, amount):
    for i in range(5):
        with lock:
            account.deposit(amount)
    print(f'Deposited {account.deposit}, new balance is {1000 + account.deposit}')

def withdraw_task(account, amount):
    for i in range(5):
        with lock:
            account.withdraw(amount)
    print(f'Withdrew {account.withdraw}, new balance is {1500 - account.withdraw}')

deposit_thread = Thread(target=deposit_task, args=(account, 100))
withdraw_thread = Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
