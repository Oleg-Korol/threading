# Словарь имен потоков и их миссий
# Полный словарь вшит в задачу
import threading
import time
import random

missions = {
    "Thread-Scan": "Сканирование данных",
    "Thread-Hack": "Взлом системы",

}
list_threads = []

# Описание задачи для потоков
def mission(mission_name):
    print(f"[{mission_name}] Миссия началась.")
    time.sleep(random.randint(1, 3))
    print(f"[{mission_name}] Миссия успешно выполнена!")


def main():
    for name, mission_name in missions.items():
        thread = threading.Thread(target = mission, name = name, args=(mission_name,))
        thread_name = thread.name
        print(f"[{thread_name} ({mission_name})] Статус миссии до запуска: {thread.is_alive()}")
        thread.start()
        list_threads.append(thread)
        print(f"[{thread_name} ({mission_name})] Миссия активна: {thread.is_alive()}")
        print(f"[{thread.name} ({missions[thread.name]})] Статус миссии после завершения: {not thread.is_alive()}")
        thread = threading.current_thread()
        for thr in list_threads:
            thr.join()
            print(f"[{thread.name} ({missions[thread.name]})] Статус миссии после завершения: {not thread.is_alive()}")


main()