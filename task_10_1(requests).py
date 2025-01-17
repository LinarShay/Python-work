import requests

# 1. Выполнение GET-запроса
response = requests.get('https://api.github.com')

# 2. Проверка статуса ответа
if response.status_code == 200:
    print("Успешный запрос!")
else:
    print("Ошибка запроса:", response.status_code)

# 3. Вывод данных в консоль
print("Заголовки ответа:", response.headers)
print("Текст ответа:", response.text[:100])  # Выводим первые 100 символов