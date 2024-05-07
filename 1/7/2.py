import threading
import time

# Список идентификаторов для именования потоков
name_threads = ['OF95RK', 'VH61DX', 'NB03WA', 'WO40ZF', 'NJ48EG', 'SX21ET', 'AT01PA', 'MR36DD', 'DD84HR', 'MI81QY']
all_threds = []

def worker()->None:
    # Получите имя текущего потока, не передавая аргументов, и верните необходимое сообщение
    thread_name =threading.current_thread().name
    print(f"Name_{thread_name} начал работу.")
    time.sleep(1)
    print(f"Name_{thread_name} завершил работу.")

# Создайте и запустите 10 потоков
def main()->None:
    for name in name_threads:
        thred = threading.Thread(target=worker, name=name)
        thred.start()
        all_threds.append(thred)

main()
[trd.join() for trd in all_threds]