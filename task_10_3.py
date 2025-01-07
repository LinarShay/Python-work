import threading
from threading import Lock
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0  # начальный баланс банка
        self.lock = Lock()  # замок для синхронизации потоков
        self.running = True  # флаг для управления работой потоков

    def deposit(self):
        for _ in range(100):  # 100 транзакций пополнения
            if not self.running:  # Проверяем флаг завершения
                break
            amount = randint(50, 500)  # случайная сумма пополнения
            with self.lock:  # блокируем доступ для изменения баланса
                self.balance += amount
                print(f"Пополнение: {amount}. Баланс: {self.balance}")
            sleep(0.001)  # задержка для имитации реального времени операции

    def take(self):
        for _ in range(100):  # 100 транзакций снятия
            if not self.running:  # Проверяем флаг завершения
                break
            amount = randint(50, 500)  # случайная сумма снятия
            print(f"Запрос на {amount}")
            with self.lock:  # блокируем доступ для проверки и изменения баланса
                if amount <= self.balance:  # проверка, достаточно ли средств
                    self.balance -= amount
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")
                    self.running = False  # Устанавливаем флаг завершения
                    break
            sleep(0.001)  # задержка для имитации реального времени операции


# Создание объекта класса Bank
bk = Bank()

# Создание потоков для методов deposit и take
th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

# Запуск потоков
th1.start()
th2.start()

# Ожидание завершения потоков
th1.join()
th2.join()

# Вывод итогового баланса
print(f"Итоговый баланс: {bk.balance}")
