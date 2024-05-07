from threading import Thread
import time

def task():
    time.sleep(3)
    print("Задача выполнена")

thread = Thread(target=task)
thread.start()
thread.join(timeout=1)
print("Основной поток завершен")