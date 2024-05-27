import time
from concurrent.futures import ThreadPoolExecutor
from threading import current_thread, local
from  a import numbers

count = 0
local_storage = local()

def setup_environment():
   global count
   current_thread().name = f'environment_{count}'
   local_storage.count = 0
   count+=1

def process_task(num):
    local_storage.count+=1
    time.sleep(0.1)
    return current_thread().name, local_storage.count


# Создайте пул потоков с инициализацией потоков и их запуском
with ThreadPoolExecutor(max_workers=10, initializer=setup_environment) as executor:
    numbers = list(filter(lambda x: x % 2 == 0, numbers))
    results = executor.map(process_task,numbers)

    for thrd_name,count in results:
        print(f'{thrd_name} - Чисел обработано: {count}')
