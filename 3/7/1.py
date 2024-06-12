from concurrent.futures import ThreadPoolExecutor, as_completed
import random


# Имитация функции обработки данных, которая может вызывать исключения
def process_data(item):
    # Имитация возможности возникновения ошибки
    if random.random() < 0.2:  # 20% шанс на ошибку
        raise ValueError(f"Ошибка обработки элемента {item}", item)
    return item  # Простая обработка данных

# Список данных для обработки
data = [i for i in range(1, 21)]

# Использование ThreadPoolExecutor для обработки данных
with ThreadPoolExecutor(max_workers=len(data)) as executor:
    futures = [executor.submit(process_data, item) for item in data]
    for future in futures:
        try:
            item = future.result()
            #print(f"Элемент {item} обработан успешно.")
        except ValueError as error:
            err = error.args[0]
            item = error.args[1]
            #print(f"Элемент {item} вызвал ошибку: {err}")
