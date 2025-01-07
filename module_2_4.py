# Исходный список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Списки для простых и непростых чисел
primes = []
not_primes = []

# Перебор чисел из списка
for number in numbers:
    # Число 1 не является простым или составным
    if number == 1:
        continue

    # Предполагаем, что число простое
    is_prime = True

    # Проверяем, есть ли делители числа
    for i in range(2, int(number**0.5) + 1):  # Достаточно проверить до корня числа
        if number % i == 0:
            is_prime = False  # Найден делитель, число не простое
            break

    # Заполняем соответствующий список
    if is_prime:
        primes.append(number)
    else:
        not_primes.append(number)

# Вывод результатов
print(f"Primes: {primes}")
print(f"Not Primes: {not_primes}")
