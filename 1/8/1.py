# Функция задачи для потоков
import time
import threading

threads_list = []

def task(code_name):
    thread = threading.current_thread()
    thread.name = code_name
    time.sleep(1)
    print(f"Задача выполнена для {threading.current_thread().name}")

def main():
    for name in code_names:
        thread = threading.Thread(target=task,args=(name,))
        print(f"Исходное имя потока: {thread.name}")
        thread.start()
        threads_list.append(thread)
        print(f"Новое имя потока: {thread.name}")

    for thr in threads_list:
        thr.join()

main()