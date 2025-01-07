def all_variants(text):
    """
    Генератор, который возвращает все подпоследовательности строки text.
    """
    length = len(text)
    for start in range(length):  # Внешний цикл для выбора начального символа
        for end in range(start + 1, length + 1):  # Внутренний цикл для определения длины последовательности
            yield text[start:end]  # Возвращаем подпоследовательность


# Пример использования
print("Результат работы генератора:")
a = all_variants("abc")

for i in a:
    print(i)
