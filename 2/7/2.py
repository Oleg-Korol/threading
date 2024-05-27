import time
from concurrent.futures import ThreadPoolExecutor
from threading import current_thread, Lock


def get_unique_thread_id():
    unique_thread_ids = ['KFD34',
                         'DGS6D',
                         'F7F9S',
                         'SDG0D',
                         'WQ9WE',
                         '29AXC',
                         'AF632',
                         'DCV13',
                         'Q9ETF',
                         '1D0S3']

    for id in unique_thread_ids:
        yield id

    # Допишите возврат уникального значения из списка unique_thread_ids при обращении к функции


# Функция инициализации потока, должна выводить определённое сообщения
def thread_initializer():
    current_thread().name = next(id_generator)
    print(f"Инициализация потока {current_thread().name}")


# Задача worker, должна выводить два сообщение
def thread_task(num):
    print(f'Задача {num} запущена')
    time.sleep(0.1)
    print(f'Задача {num} выполнеа')

# Создайте пул потоков с инициализацией потоков и их запуском
with ThreadPoolExecutor(max_workers=10, initializer=thread_initializer) as executor:
    id_generator = get_unique_thread_id()
    for num in range(10):
        executor.submit(thread_task, num )
