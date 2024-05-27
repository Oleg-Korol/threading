import os
import psutil
from concurrent.futures import ThreadPoolExecutor

# Получение количества логических процессоров
logical_cpus = os.cpu_count()
print(f"Количество логических CPU: {logical_cpus}")

# Получение количества физических процессоров (требует psutil)
physical_cpus = psutil.cpu_count(logical=False)
print(f"Количество физических CPU: {physical_cpus}")

# Создание пула потоков и проверка количества потоков по умолчанию
with ThreadPoolExecutor() as executor:
    default_threads = executor._max_workers
    print(f"Количество потоков по умолчанию: {default_threads}")