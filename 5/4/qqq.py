import threading
import time
from threading import Lock,RLock,current_thread

lock =Lock()
lock = RLock()



def funk(name):
    current_thread().name = name
    current_thrd = current_thread().name
    lock.acquire()
    print(f"Выпоняется поток  - {current_thrd}")
    print(f'Блокировка захвачена потоком - {current_thrd}')
    time.sleep(5)
    if lock.locked():
        lock.release()
        print(f'Блокировка освобождена')



def main():
    main_thrd = threading.main_thread().name
    print(f"Главный поток - {main_thrd}")
    thread1 = threading.Thread(target=funk, args= ('Поток-1',), daemon=True)
    thread2 = threading.Thread(target=funk, args=('Поток-2',), daemon=True)
    thread1.start()
    lock.release()
    thread2.start()
    thread1.join()
    thread2.join()

main()