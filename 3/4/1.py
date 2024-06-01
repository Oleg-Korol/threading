from concurrent.futures import ThreadPoolExecutor, as_completed
import time



# Имена и время для таймеров
names = {'77b7-5': 5, 'q4z1-2': 2, 'g8s4-9': 9, 'b606-7': 7, 'ad21-6': 6,
           'b806-4': 4, '4x9d-3': 3, '411a-8': 8, 'g8s4-10': 10, 'e3ce-1': 1}
# Функция таймера, которая "спит" указанное количество секунд
def timer(name, seconds):
    if seconds > 5:
        raise TimeoutError(f"Таймер {name} отменён из-за превышения времени, состояние CANCELLED.")
    time.sleep(seconds)
    return name

# Создание пула потоков
with ThreadPoolExecutor(max_workers=len(names)) as executor:

    futures = [(name,executor.submit(timer,name, seconds)) for name, seconds in names.items()]
    for future in as_completed(futures,timeout=5):
        
        print(name)
        if not future.running() and future.done():
            print(f"Таймер {future} ожидает запуска, состояние PENDING.")
        if not future.cancelled() and future.done():
            print(f"Таймер {name} запущен, состояние RUNNING: {future.running()}")
        if future.exception():
            print(future.result())
        time.sleep(5)
        if future.cancelled():
            future.cancal()
            print(f"Таймер {name} завершил работу, состояние FINISHED: {future.done()}")
        else:
            future.cancal()
            print(f"Таймер {name} завершил работу, состояние FINISHED: {future.done()}")
