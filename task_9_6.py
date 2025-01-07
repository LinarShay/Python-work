def is_prime(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)  # Вызываем исходную функцию и получаем результат

        # Проверяем, является ли число простым
        if result > 1:
            for i in range(2, int(result**0.5) + 1):
                if result % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        else:
            print("Составное")

        return result

    return wrapper


@is_prime
def sum_three(a, b, c): #Функция складывает три числа.

    return a + b + c


# Пример использования
result = sum_three(2, 3, 6)
print(result)
