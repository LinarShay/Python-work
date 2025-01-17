import pandas as pd
import os

# Проверка наличия файла
file_path = 'data.csv'
if not os.path.exists(file_path):
    print(f"Файл {file_path} не найден. Создаем тестовый файл...")
    with open(file_path, 'w') as file:
        file.write("Имя,Возраст,Зарплата\n")
        file.write("Алиса,30,50000\n")
        file.write("Роб,25,45000\n")
        file.write("Чарли,35,60000\n")

# Чтение данных из CSV-файла
data = pd.read_csv(file_path)

# Вывод первых 5 строк данных
print("Первые 5 строк данных:")
print(data.head())

# Простой анализ данных
print("\nОсновная информация о данных:")
print(data.info())

print("\nСтатистика по числовым столбцам:")
print(data.describe())