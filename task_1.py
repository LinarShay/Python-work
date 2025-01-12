import time
from datetime import datetime
from multiprocessing import Pool

def read_info(name):
    """
    Функция для чтения данных из файла.
    :param name: Имя файла.
    :return: Список строк из файла.
    """
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:  # Если строка пустая, завершаем чтение
                break
            all_data.append(line.strip())  # Добавляем строку в список
    return all_data

def linear_read(filenames):
    """
    Линейное чтение файлов.
    :param filenames: Список имен файлов.
    """
    start_time = datetime.now()
    for filename in filenames:
        read_info(filename)
    end_time = datetime.now()
    print(f"Линейное выполнение: {end_time - start_time}")

def multiprocess_read(filenames):
    """
    Многопроцессное чтение файлов.
    :param filenames: Список имен файлов.
    """
    start_time = datetime.now()
    with Pool() as pool:  # Создаем пул процессов
        pool.map(read_info, filenames)  # Параллельное выполнение
    end_time = datetime.now()
    print(f"Многопроцессное выполнение: {end_time - start_time}")

if __name__ == '__main__':
    # Создаем список файлов
    filenames = [f'./data/file {number}.txt' for number in range(1, 5)]

    # Линейный подход
    print("Запуск линейного подхода...")
    linear_read(filenames)

    # Многопроцессный подход
    print("Запуск многопроцессного подхода...")
    multiprocess_read(filenames)