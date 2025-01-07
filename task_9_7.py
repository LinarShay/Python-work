class StepValueError(ValueError):
    """
    Класс исключения для проверки шага итерации.
    """
    pass


class Iterator:
    """
    Класс итератора, который реализует пользовательскую логику range.
    """
    def __init__(self, start, stop, step=1):
        """
        Инициализация объекта итератора.
        :param start: Начальное значение.
        :param stop: Конечное значение.
        :param step: Шаг итерации (по умолчанию 1).
        """
        if step == 0:
            raise StepValueError("шаг не может быть равен 0")
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

    def __iter__(self):
        """
        Метод для получения итератора.
        Сбрасывает pointer на start и возвращает текущий объект.
        """
        self.pointer = self.start
        return self

    def __next__(self):
        """
        Метод для перехода к следующему элементу итерации.
        Увеличивает pointer на step и проверяет, достиг ли конец итерации.
        """
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration
        current_value = self.pointer
        self.pointer += self.step
        return current_value


# Пример использования
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=" ")
except StepValueError:
    print("Шаг указан неверно")

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

# Вывод результатов итерации
for i in iter2:
    print(i, end=" ")
print()

for i in iter3:
    print(i, end=" ")
print()

for i in iter4:
    print(i, end=" ")
print()

for i in iter5:
    print(i, end=" ")
print()
