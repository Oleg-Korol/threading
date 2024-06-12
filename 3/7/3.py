from concurrent.futures import ThreadPoolExecutor, as_completed
import random

# Имитация функции обработки данных, которая может вызывать исключения
def process_data(item):
    # Имитация возможности возникновения ошибки
    if random.random() < 0.2:  # 20% шанс на ошибку
        raise ValueError(f"Ошибка обработки элемента {item}")
    return item # Простая обработка данных

# Список данных для обработки
data = [i for i in range(1, 21)]



with ThreadPoolExecutor(max_workers=5) as executor:
    # Отправка задач на обработку данных
    future_to_data = {executor.submit(process_data, item): item for item in data}
    print(future_to_data)

    # Обработка завершенных задач
    for future in as_completed(future_to_data):
        print(future)
        item = future_to_data[future]
        print(item)