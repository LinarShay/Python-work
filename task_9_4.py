# Задача 1: Lambda-функция для сравнения символов в двух строках

# Данные
first = 'Мама мыла раму'
second = 'Рамена мало было'

# Lambda-функция для сравнения символов строк на одинаковых позициях
result = list(map(lambda f, s: f == s, first, second))

# Вывод результата
print("Задача 1: Результат lambda-функции")
print(result)


# Задача 2: Замыкание (функция для записи данных в файл)

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as file:
            for data in data_set:
                file.write(str(data) + '\n')  # Преобразуем в строку и записываем с новой строки
    return write_everything

# Пример использования замыкания
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

print("\nЗадача 2: Функция записи в файл выполнена.")
print("Данные записаны в файл 'example.txt'.")


# Задача 3: Метод __call__ в классе (Мистическая Шар)

from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = words  # Коллекция строк, переданных при создании объекта

    def __call__(self):
        return choice(self.words)  # Возвращаем случайное слово

# Пример использования
first_ball = MysticBall('Да', 'Нет', 'Наверное')

print("\nЗадача 3: Результаты случайного выбора:")
print(first_ball())  # Пример случайного выбора
print(first_ball())  # Пример случайного выбора
print(first_ball())  # Пример случайного выбора
