def apply_all_func(int_list, *functions):
    results = {}

    # Перебираем все переданные функции
    for func in functions:
        # Вызываем функцию с переданным списком int_list и добавляем результат в словарь
        results[func.__name__] = func(int_list)

    return results


# Примеры использования и вывод результата в одну строку:

# Пример 1: применяем функции max и min
result_1 = apply_all_func([6, 20, 15, 9], max, min)

# Пример 2: применяем функции len, sum и sorted
result_2 = apply_all_func([6, 20, 15, 9], len, sum, sorted)

# Выводим все результаты в одну строку
print(f"{result_1} {result_2}")
