import matplotlib.pyplot as plt
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

# 1. Чтение данных из CSV-файла
data = pd.read_csv('data.csv')

# 2. Создание графика
plt.figure(figsize=(10, 6))

# 3. Построение scatter plot (точечный график)
plt.scatter(data['Возраст'], data['Зарплата'], color='blue', label='Зарплата')

# 4. Настройка графика
plt.title('Зависимость зарплаты от возраста')
plt.xlabel('Возраст')
plt.ylabel('Зарплата')
plt.legend()

# 5. Сохранение графика в файл
plt.savefig('salary_vs_age.png')

# 6. Отображение графика
plt.show()